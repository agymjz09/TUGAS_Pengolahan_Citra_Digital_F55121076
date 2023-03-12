# Nama  : Agym Mahaputra Romy Barlianta
# NIM   : F55121076
# Kelas : B

import cv2
import numpy as np

# Baca citra
gambar = cv2.imread('prototype.jpg')

# Konversi ke grayscale
abu = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)

# Terapkan min filter dengan kernel 3x3
kernel = np.ones((3,3), np.uint8)
min_filter1 = cv2.erode(abu, kernel, iterations=1)
min_filter2 = cv2.erode(min_filter1, kernel, iterations=1)
min_filter3 = cv2.erode(min_filter2, kernel, iterations=1)

# Tampilkan citra asli dan hasil min filter
cv2.imshow('Original', abu)
cv2.imshow('Min Filter 1', min_filter1)
cv2.imshow('Min Filter 2', min_filter2)
cv2.imshow('Min Filter 3', min_filter3)

# Tunggu hingga tombol keyboard ditekan
cv2.waitKey(0)

# Tutup semua jendela
cv2.destroyAllWindows()