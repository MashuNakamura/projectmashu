import numpy as np
import cv2 as cv

## Ambil Gambar yang ingin di gunakan
image = cv.imread('/home/mashu/Pictures/hima.jpg')
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
median = cv.medianBlur(image, 5)
# cv.imshow('Median Image', median)

inverse_image = cv.bitwise_not(image)

# cv.imshow('Original Image', image)
# cv.imwrite('original_image.bmp', image)

# cv.imshow('Inverse Image', inverse_image)
# cv.imwrite('inverse_image.bmp', inverse_image)

## Tampilkan Gambar setelah dilakukan perubahan pada gambar

experience_image = np.zeros((300, 300, 3), dtype=np.uint8)
# experience_image[:] = (128, 0, 128)

for i in range(300):
    experience_image[i, :] = (min(i // 2, 255), 0, min(i, 255))

cv.imwrite('Purple_Image.bmp', experience_image)
cv.imshow('Purple Image', experience_image)
cv.waitKey(0)
cv.destroyAllWindows()
