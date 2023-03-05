#Nama : Agym Mahaputra Romy Barlianta
#NIM  : F55121076
import cv2
import numpy as np

img1 = cv2.imread('musim1.jpg')
img2 = cv2.imread('musim2.jpg')
img3 = cv2.imread('musim3.jpg')

gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray_img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

img = np.array([gray_img1, gray_img2, gray_img3])
avg_img = np.average (img, axis=0)
avg_imgs = avg_img.astype(np.uint8)

cv2.imshow('Avegared Image', avg_imgs)
cv2.waitKey(0)
cv2.destroyAllWindows()

