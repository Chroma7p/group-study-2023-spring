import cv2
import matplotlib.pyplot as plt

plt.figure(figsize=(20,20))
img1=cv2.imread("body.enc.ppm")
ax1=plt.subplot(2,1,1)
ax1.imshow(img1)
img2=cv2.imread("body.dec.ppm")
ax2=plt.subplot(2,1,2)
ax2.imshow(img2)
plt.show()
cv2.imwrite("result.png",img2)