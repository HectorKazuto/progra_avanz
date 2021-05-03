import cv2
import numpy as np

img = cv2.imread('img1.png')

cv2.imshow('Mostrar imagen OPENCV', img)

color_bajo = (15, 0, 0)
color_alto = (30, 255, 255)

img_salida = img.copy()
img_salida_rgb = cv2.cvtColor(img_salida, cv2.COLOR_BGR2RGB)
img_salida_hsv = cv2.cvtColor(img_salida_rgb, cv2.COLOR_RGB2HSV)
mask = cv2.inRange(img_salida_hsv, color_bajo, color_alto)
resultado = cv2.bitwise_and(img_salida, img_salida, mask = mask)


cv2.imshow('PROCESADO POR OPENCV', resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()