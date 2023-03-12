# Nama  : Agym Mahaputra Romy Barlianta
# NIM   : F55121076
# Kelas : B

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Baca citra
img = cv2.imread('prototype.jpg', cv2.IMREAD_GRAYSCALE)

# Konversi citra ke float32
f = np.float32(img)

# Terapkan FFT
f_fft = np.fft.fft2(f)

# Geser frekuensi nol ke tengah
f_fft_shift = np.fft.fftshift(f_fft)

# Hitung magnitudo dan konversi ke dB
magnitude_spectrum = 20*np.log(np.abs(f_fft_shift))

# Tampilkan citra dan spektrum frekuensi
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Citra asli'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Spektrum frekuensi'), plt.xticks([]), plt.yticks([])
plt.show()