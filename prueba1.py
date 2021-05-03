import cv2
import numpy as np

img = cv2.imread('Finn.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (2,81,95), (2,73,67))

cv2.imshow("Mascara", mask)
cv2.imshow("Imagen", img)
cv2.waitKey(0)
cv2.destroyAllWindows()