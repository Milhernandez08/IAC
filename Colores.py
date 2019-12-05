import numpy as np
import cv2

def Convercio_BGR_a_HSV(Color_Ligero, Color_Oscuro):
    c1 = cv2.cvtColor( np.uint8( [ [Color_Ligero] ] ), cv2.COLOR_BGR2HSV ) [0][0]
    c2 = cv2.cvtColor( np.uint8( [ [Color_Oscuro] ] ), cv2.COLOR_BGR2HSV ) [0][0]
    
    minHSV = np.array( [ c1[0], c1[1], c1[2] ] )
    maxHSV = np.array( [ c2[0], c2[1], c2[2] ] )

    return minHSV, maxHSV

Blanco          = [255, 255, 255]

Amarillo_Ligero = [64, 255, 255]
Amarillo_Oscuro = [0, 204, 204]

Cafe_Ligero     = [0, 80, 161]
Cafe_Oscuro     = [0, 51, 102]

Rojo_Ligero     = [64, 64, 255]
Rojo_Oscuro     = [0, 0, 204]

Naranja_Ligero  = [64, 159, 255]
Naranja_Oscuro  = [0, 102, 204]

Gris_Ligero     = [194, 194, 194]
Gris_Oscuro     = [125, 125, 125]

Violeta_Ligero  = [196, 69, 120]
Violeta_Oscuro  = [130, 40, 76]

Verde_Ligero    = [14, 179, 36]
Verde_Ligero    = [9, 115, 21]

Azul_Ligero     = [255, 64, 64]
Azul_Oscuro     = [204, 0, 0]