import cv2
import numpy as np
import matplotlib
import math
from matplotlib.pyplot import imshow
from matplotlib import pyplot as plt

def buscar_dientes(imgColor, imgGray): 
    # cv2.imshow( "Titulo", imgColor )
    # cv2.waitKey()
    #kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(8,8))                    
    #Binarizacion
    umbral = cv2.threshold(imgGray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[0]   
    imgBinarizada = cv2.threshold(imgGray, umbral, 255, cv2.THRESH_BINARY)[1]        
    cv2.imwrite('binarizada.png', imgBinarizada)    
    erocion = cv2.erode(imgBinarizada, kernel, iterations=7)     
    contours = cv2.findContours(erocion,1,2)[0]
    i = 0
    for cnt in contours:
        # cnt_len = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True), True)
        # print ( cnt )
        # approx = cv2.approxPolyDP(cnt,0.01*cnt_len,True)        
        if len(approx)==5: 
            i+=1           
            cv2.drawContours(imgColor,[cnt],0,(0,0,255),-1)
        elif len(approx)==3:
            i+=1
            cv2.drawContours(imgColor,[cnt],0,(0,0,255),-1)
        elif len(approx) == 9:
            i+=1
            cv2.drawContours(imgColor,[cnt],0,(0,0,255),-1)            
    cv2.imwrite('erosion.png', erocion) 
    # cv2.imwrite('dientes.png', imgColor)
    if (i > 5):
        return 1
    else:
        return 0
     

def detectar_lineas(imgColor): 
    #img = cv2.imread('ImgMejoradas/1.jpg',0)    
    #converted = convert_hls(img)
    image = cv2.cvtColor(imgColor,cv2.COLOR_BGR2HLS)
    lower = np.uint8([0, 200, 0])
    upper = np.uint8([255, 255, 255])
    white_mask = cv2.inRange(image, lower, upper)
    # yellow color mask
    lower = np.uint8([10, 0,   100])
    upper = np.uint8([40, 255, 255])
    yellow_mask = cv2.inRange(image, lower, upper)
    # combine the mask
    mask = cv2.bitwise_or(white_mask, yellow_mask)
    result = imgColor.copy()
    # cv2.imwrite('ImgGeneradas/lineas_detectadas/mask.jpg',mask) 
    #cv2.imwrite('ImgGeneradas/lineas_detectadas/hls.jpg',image) 

    height,width = mask.shape
    skel = np.zeros([height,width],dtype=np.uint8)      #[height,width,3]
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    temp_nonzero = np.count_nonzero(mask)
    while(np.count_nonzero(mask) != 0 ):
        eroded = cv2.erode(mask,kernel)
        #cv2.imwrite('ImgGeneradas/lineas_detectadas/erode.jpg',eroded)     
        temp = cv2.dilate(eroded,kernel)    
        #cv2.imwrite('ImgGeneradas/lineas_detectadas/dilate.jpg',temp) 
        temp = cv2.subtract(mask,temp)
        skel = cv2.bitwise_or(skel,temp)
        mask = eroded.copy()

    # cv2.imwrite('ImgGeneradas/lineas_detectadas/skel.jpg',skel) 

    edges = cv2.Canny(skel, 50, 150)
    cierre = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    cierre = cv2.morphologyEx(cierre, cv2.MORPH_CLOSE, kernel)
    dilatacion = cv2.dilate(cierre, kernel, iterations=2)
    erosion= cv2.erode(dilatacion, kernel, iterations=1)    
    cierre = cv2.morphologyEx(erosion, cv2.MORPH_CLOSE, kernel)
    apertura = cv2.morphologyEx(cierre, cv2.MORPH_OPEN, kernel)
    median = cv2.medianBlur(apertura,5)
    # cv2.imwrite('ImgGeneradas/lineas_detectadas/cany.jpg',edges) 
    # cv2.imwrite("ImgGeneradas/lineas_detectadas/Open.jpg", apertura)
    # cv2.imwrite("ImgGeneradas/lineas_detectadas/Close.jpg", cierre) 
    # cv2.imwrite("ImgGeneradas/lineas_detectadas/erosion.jpg", erosion) 
    # cv2.imwrite("ImgGeneradas/lineas_detectadas/dilatacion.jpg", dilatacion) 
    # cv2.imwrite('ImgGeneradas/lineas_detectadas/median-blur.png', median)    
    
    # Buscamos las lineas
    contornos = cv2.findContours(median, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    
    # cv2.polylines(result,contornos,1, (0,255,0))    
    # cv2.imwrite('ImgGeneradas/lineas_detectadas/result.jpg',result)

    if (len(contornos) > 500):
        return 1
    else:
        return 0


# a = cv2.imread('01.jpg',0)
# b = cv2.imread('01.jpg')

# print(buscar_dientes(b,a))