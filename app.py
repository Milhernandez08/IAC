from flask import Flask, request, redirect, url_for, send_from_directory
from flask_cors import CORS
from correo import Correo

import os
import time
import Colores
import Carteciano_a_Polar
import RED.Modelo as Modelo

UPLOAD_FOLDER = os.path.abspath("./uploads/")

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def index():
    return "Hola mundo"

@app.route("/upload/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if "ourfile" not in request.files:
            return "El campo esta vacio"

        f = request.files["ourfile"]

        if f.filename == "":
            return "Ningun archivo seleccionado"

        extencion = f.filename.split(".")
        filename = "time_" + time.strftime("%b") + time.strftime("%d") + time.strftime("%Y") + "_" + time.strftime("%H") + "_" + time.strftime("%M") + "_" + time.strftime("%S") + "." + extencion[1]

        f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        c = Carteciano_a_Polar.obtener_Imagen(filename)



        valor = Modelo.Resultado(Colores.Encontrar_Caracteristicas(c))
        # valor = Modelo.Resultado([0., 1., 0., 1., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.])

        print(valor)

        return str(valor) #filename + str(valor)  #redirect(url_for("get_file", filename=filename))

    return """
    <form method="POST" enctype="multipart/form-data">
    <input type="file" name="ourfile">
    <input type="submit" name="UPLOAD">
    </form>
    """
@app.route("/enviarcorreo/<correo>", methods=["POST"])
def send(correo):
    res = Correo(correo)
    return res.enviar()

@app.route("/uploads/<filename>")
def get_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
