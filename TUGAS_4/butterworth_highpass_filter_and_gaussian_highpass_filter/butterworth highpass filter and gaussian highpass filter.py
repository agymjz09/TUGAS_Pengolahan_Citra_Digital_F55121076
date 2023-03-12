# Nama  : Agym Mahaputra Romy Barlianta
# NIM   : F55121076
# Kelas : B

import cv2
import numpy as np

# Load image
img = cv2.imread('prototype1.jpg', 0)

# Get image shape
rows, cols = img.shape

# Create butterworth highpass filter mask
butterworth_mask = np.zeros((rows, cols, 2), np.float32)
crow, ccol = rows/2 , cols/2
radius = 30
n = 2

for i in range(rows):
    for j in range(cols):
        butterworth_mask[i,j] = 1 / (1 + ((np.sqrt((i-crow)**2 + (j-ccol)**2)) / radius) ** (2*n))

# Apply butterworth highpass filter
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
dft_shift_highpass = dft_shift * butterworth_mask
dft_highpass = np.fft.ifftshift(dft_shift_highpass)
img_highpass_butterworth = cv2.idft(dft_highpass)
img_highpass_butterworth = cv2.magnitude(img_highpass_butterworth[:,:,0], img_highpass_butterworth[:,:,1])

# Create gaussian highpass filter mask
gaussian_mask = np.zeros((rows, cols, 2), np.float32)
crow, ccol = rows/2 , cols/2
radius = 30

for i in range(rows):
    for j in range(cols):
        gaussian_mask[i,j] = 1 - np.exp(-((i-crow)**2 + (j-ccol)**2) / (2*radius**2))

# Apply gaussian highpass filter
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
dft_shift_highpass = dft_shift * gaussian_mask
dft_highpass = np.fft.ifftshift(dft_shift_highpass)
img_highpass_gaussian = cv2.idft(dft_highpass)
img_highpass_gaussian = cv2.magnitude(img_highpass_gaussian[:,:,0], img_highpass_gaussian[:,:,1])

# Display images
cv2.imshow('Original Image', img)
cv2.imshow('Butterworth Highpass Filter', img_highpass_butterworth)
cv2.imshow('Gaussian Highpass Filter', img_highpass_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
