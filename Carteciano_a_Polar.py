import cv2
import numpy as np

def obtener_Imagen(Nombre_Imagen_Nueva):
    URL      = "uploads/" + Nombre_Imagen_Nueva # Direccion donde se almacenan las imagenes
    RESPALDO = "Pasos/"                         # Direccion donde se almadenaran las imagenes como evidencia

    # --------- Lectura de la imagen que se encuentra almacenada en el servidor -------------

    img_Contorno = cv2.imread(URL)    # Imagen que servira para obtner contornos, area y centro del circulo
    img_Polar    = cv2.imread(URL,1)  # Imagen que se transformara de Carteciano a Polar O -> ---

    # -------- Resaltar los detalles de la imagen mejorandola ---------

    madian       = cv2.medianBlur(img_Contorno, 25)                  # Filtro
    gris         = cv2.cvtColor(madian, cv2.COLOR_BGR2GRAY) # Convertir la imagen a escala de grises
    clahe        = cv2.createCLAHE(clipLimit=75.0, tileGridSize=(128,128))
    gris         = clahe.apply(gris)

    # -------- Busqueda de contornos --------

    gris         = cv2.Canny(gris, 10, 150)
    gris         = cv2.dilate(gris, None, iterations=1)
    gris         = cv2.erode(gris, None,iterations=1)
    contornos, _ = cv2.findContours(gris, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # ------- Busqueda de un contorno con el area mas grande ------

    for contorno in contornos:
        area     = cv2.contourArea(contorno) # Esta variable almacena el area de cada contorno encotrado
        x,y,w,h  = cv2.boundingRect(contorno)# Estas variables almacenan los valores del tamaño de la imagen

        if area > 3000:
            M    = cv2.moments(contorno)
            if (M["m00"]==0): M["m00"] = 1
            xcentro = int(M["m10"]/M["m00"])
            ycentro = int(M["m01"]/M["m00"])
            radio   = xcentro-x

            # -------- Dibujamos el centro y el contorno del croma --------

            cv2.circle(img_Contorno, (xcentro, ycentro), 100, (0,255,0), -1)
            cv2.drawContours(img_Contorno, contorno, -1, (0,255,0), 10)

            # -------- Primer Paso Terminado, Guardar evidencia -----------

            cv2.imwrite(RESPALDO+"Paso_1.jpg", img_Contorno)

            # -------- Convercion de carteciano a polar --------

            img_Polar = img_Polar.astype(np.float32)

            value     = np.sqrt((ycentro**2.0)+(xcentro**2.0)) # Variable que almacena la redimencion de la imagen nueva
            polar_img = cv2.linearPolar(img_Polar, (xcentro, ycentro), value, cv2.WARP_FILL_OUTLIERS)

            polar_img = polar_img.astype(np.uint8)
            
            # -------- Segundo Paso Termiando, Guardar evidencia --------

            cv2.imwrite(RESPALDO+"Paso_2.jpg", polar_img)

            # -------- Ajuste de la imagen modificada, quitando lo no util --------
            
            crop_img  = polar_img[0:3408, 0:2400] # Area que es util de la imagen

            # -------- Tercer Paso Terminado, Guardar evidencia --------

            cv2.imwrite(RESPALDO+"Paso_3.jpg", crop_img)

            # -------- Ajuste horizontal de la imagen --------

            horizontal_img = cv2.rotate(crop_img, cv2.ROTATE_90_CLOCKWISE)

            # -------- Cuarto Paso Terminado, Guardar evidencia --------

            cv2.imwrite(RESPALDO+"Paso_4.jpg", horizontal_img)

            return horizontal_img