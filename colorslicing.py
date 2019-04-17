import cv2
import numpy as np

color_component, w = [255, 0, 0], 20

img = cv2.imread('Lenna.png')
height, width = img.shape[0], img.shape[1]
s = np.zeros(img.shape)
for i in range(height):
    for j in range(width):
        pixel = img[i][j]
        s[i][j] = [128 if abs(color_component[index]-pixel[index]) > w/2 else pixel[index] for index in range(3)]

cv2.imwrite('output.png', s)
