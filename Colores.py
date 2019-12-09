import numpy as np
import Metodos as Mt
import cv2

def Encontrar_Caracteristicas(imagen):
    Blanco_Unico          = np.array( [0,0,255], np.uint8 )

    Amarillo_Ligero = np.array( [20,100,20], np.uint8 )
    Amarillo_Oscuro = np.array( [32,255,255], np.uint8 )

    Cafe_Ligero     = np.array( [13,143,26], np.uint8 )
    Cafe_Oscuro     = np.array( [21,145,59], np.uint8 )

    Rojo_Ligero1    = np.array([0,65,75], np.uint8)
    Rojo_Oscuro1    = np.array([12,255,255], np.uint8)
    Rojo_Ligero2    = np.array([240,65,75], np.uint8)
    Rojo_Oscuro2    = np.array([255,255,255], np.uint8)

    Naranja_Ligero  = np.array( [14,191,255], np.uint8 )
    Naranja_Oscuro  = np.array( [14,255,204], np.uint8 )

    Gris_Ligero     = np.array( [0,0,194], np.uint8 )
    Gris_Oscuro     = np.array( [0,0,125], np.uint8 )

    Violeta_Ligero  = np.array( [130,100,20], np.uint8 )
    Violeta_Oscuro  = np.array( [145,255,255], np.uint8 )

    Verde_Ligero    = np.array( [36,100,20], np.uint8 )
    Verde_Oscuro    = np.array( [70,255,255], np.uint8 )

    Azul_Ligero     = np.array( [100,65,75], np.uint8 )
    Azul_Oscuro     = np.array( [130, 255, 255], np.uint8 )


    # imagen          = cv2.imread('Paso_4.jpg')
    imagenHSV       = cv2.cvtColor( imagen, cv2.COLOR_BGR2HSV )

    # Partes de zonas
    Partes          = int(imagenHSV.shape[0]/4)

    # Zonas de la imagen
    Zona_Central    = imagenHSV[0:Partes, 0:imagenHSV.shape[1]]
    Zona_Interna    = imagenHSV[Partes:Partes*2, 0:imagenHSV.shape[1]]
    Zona_Intermedia = imagenHSV[Partes*2:Partes*3, 0:imagenHSV.shape[1]]
    Zona_Periferica = imagenHSV[Partes*3:Partes*4, 0:imagenHSV.shape[1]]

    maskBlanco      = cv2.inRange( Zona_Central, Blanco_Unico, Blanco_Unico )

    maskAmarillo    = cv2.inRange( imagenHSV, Amarillo_Ligero, Amarillo_Oscuro )

    maskCafe        = cv2.inRange( imagenHSV, Cafe_Ligero, Cafe_Oscuro )

    maskRojo1       = cv2.inRange( imagenHSV, Rojo_Ligero1, Rojo_Oscuro1 )
    maskRojo2       = cv2.inRange( imagenHSV, Rojo_Ligero2, Rojo_Oscuro2 )
    maskRojo        = cv2.add(maskRojo1,maskRojo2)

    maskNaranja     = cv2.inRange( imagenHSV, Naranja_Ligero, Naranja_Oscuro )

    maskGris        = cv2.inRange( imagenHSV, Gris_Ligero, Gris_Oscuro )

    maskVioleta     = cv2.inRange( imagenHSV, Violeta_Ligero, Violeta_Oscuro )

    maskVerde       = cv2.inRange( imagenHSV, Verde_Ligero, Verde_Oscuro )

    maskAzul        = cv2.inRange( imagenHSV, Azul_Ligero, Azul_Oscuro )

    Blanco          = cv2.findContours(maskBlanco, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]   
    # Blanco          = cv2.findContours(Zona_Central, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]   
    Amarillo        = cv2.findContours(maskAmarillo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]       
    Cafe            = cv2.findContours(maskCafe, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]       
    Rojo            = cv2.findContours(maskRojo, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]       
    Naranja         = cv2.findContours(maskNaranja, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]       
    Gris            = cv2.findContours(maskGris, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]       
    Violeta         = cv2.findContours(maskVioleta, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]       
    Verde           = cv2.findContours(maskVerde, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]       
    Azul            = cv2.findContours(maskAzul, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]       

    datos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    if Blanco is not None:
        for contorno in Blanco:
            area = cv2.contourArea(contorno)
            if area > 20:
                datos[0] = 1

    if Amarillo is not None:
        for contorno in Amarillo:
            area = cv2.contourArea(contorno)
            if area > 20:
                datos[1] = 1

    if Cafe is not None:
        for contorno in Cafe:
            area = cv2.contourArea(contorno)
            if area > 20:
                datos[2] = 1

    if Rojo is not None:
        for contorno in Rojo:
            area = cv2.contourArea(contorno)
            if area > 20:
                datos[3] = 1
                
    if Naranja is not None:
        for contorno in Naranja:
            area = cv2.contourArea(contorno)
            if area > 20:
                datos[4] = 1

    if Gris is not None:
        for contorno in Gris:
            area = cv2.contourArea(contorno)
            if area > 20:
                datos[9] = 1

    if Violeta is not None:
        for contorno in Violeta:
            area = cv2.contourArea(contorno)
            if area > 20:
                datos[10] = 1

    if Verde is not None:
        for contorno in Verde:
            area = cv2.contourArea(contorno)
            if area > 20:
                datos[11] = 1

    if Azul is not None:
        for contorno in Azul:
            area = cv2.contourArea(contorno)
            if area > 20:
                datos[12] = 1

    imgGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    datos[13] = Mt.buscar_dientes(imagen, imgGris)
    datos[5]  = Mt.detectar_lineas(imagen)

    return datos

# imagen          = cv2.imread('Paso_4.jpg')
# respuesta = Encontrar_Caracteristicas(imagen)

# print( respuesta )

# cv2.imshow( "Imagen",respuesta[0] )
# cv2.waitKey()