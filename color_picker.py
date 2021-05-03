import cv2
import numpy as np

def color_picker(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		colorsBGR = img[y, x]
		colorsRGB=tuple(reversed(colorsBGR))
		print("Posicion:({} , {})".format(x,y))
		print("Color en RGB:{} ".format(colorsRGB))

	if event == cv2.EVENT_RBUTTONDOWN:
		colorsBGR = img[y, x]
		colorsRGB=tuple(reversed(colorsBGR))

		r = colorsRGB[0]
		g = colorsRGB[1]
		b = colorsRGB[2]

		r, g, b = r/255, g/255, b/255
		mx = max(r, g, b)
		mn = min(r, g, b)
		df = mx-mn
		if mx == mn:
			h = 0
		elif mx == r:
			h = (60 * ((g-b)/df) + 360) % 360
		elif mx == g:
			h = (60 * ((b-r)/df) + 120) % 360
		elif mx == b:
			h = (60 * ((r-g)/df) + 240) % 360
		if mx == 0:
			s = 0
		else:
			s = (df/mx)*100
		v = mx*100

		print("Posicion:({} , {})".format(x,y))
		print("Color en HSV:{} {} {}".format(h,s,v))


img = cv2.imread('img_tarea.png')
cv2.imshow('IMAGEN TAREA OPENCV', img)

cv2.setMouseCallback("IMAGEN TAREA OPENCV", color_picker)

cv2.waitKey(0)
cv2.destroyAllWindows()