import cv2
import matplotlib.pyplot as plt

img2=cv2.imread("body.dec.2.ppm")

plt.imshow(img2)

plt.show()

cv2.imwrite("result2222.png",img2)