# Nama  : Agym Mahaputra Romy Barlianta
# NIM   : F55121076
# Kelas : B

import cv2
import numpy as np

# Baca citra
img = cv2.imread('prototype.jpg')

# Konversi ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Terapkan max filter dengan kernel 3x3 sebanyak 3 kali
kernel = np.ones((3,3), np.uint8)
max_filter1 = cv2.dilate(gray, kernel, iterations=1)
max_filter2 = cv2.dilate(max_filter1, kernel, iterations=1)
max_filter3 = cv2.dilate(max_filter2, kernel, iterations=1)

# Tampilkan citra asli dan hasil max filter sebanyak 3 kali
cv2.imshow('Original', gray)
cv2.imshow('Max Filter 1', max_filter1)
cv2.imshow('Max Filter 2', max_filter2)
cv2.imshow('Max Filter 3', max_filter3)

# Tunggu hingga tombol keyboard ditekan
cv2.waitKey(0)

# Tutup semua jendela
cv2.destroyAllWindows()