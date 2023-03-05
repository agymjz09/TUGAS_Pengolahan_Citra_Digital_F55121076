#Nama : Agym Mahaputra Romy Barlianta
#NIM  : F55121076
import cv2
import matplotlib.pyplot as plt
#low Contrast Picture
img_low_contrast = cv2.imread('low.png', 0)
histogram_low = cv2.calcHist ([img_low_contrast], [0], None, [256], [0, 256])
plt.subplot(1, 3, 1)
plt.plot(histogram_low, color='gray')
plt.title("Histogram kontras rendah")
plt.xlabel('Intensitas pixels')
plt.ylabel('jumlah pixels')

#normal Contrast picture
img_normal_contrast = cv2.imread('normal.png', 0)
histogram_normal = cv2.calcHist ([img_normal_contrast], [0], None, [256], [0, 256])
plt.subplot(1, 3, 2)
plt.plot(histogram_normal, color='gray')
plt.title("Histogram kontras normal")
plt.xlabel('Intensitas pixels')
plt.ylabel('jumlah pixels')

#high Contrast picture
img_high_contrast = cv2.imread('high.png', 0)
histogram_high = cv2.calcHist ([img_high_contrast], [0], None, [256], [0, 256])
plt.subplot(1, 3, 3)
plt.plot(histogram_high, color='gray')
plt.title("Histogram kontras tinggi")
plt.xlabel('Intensitas pixels')
plt.ylabel('jumlah pixels')

plt.show()