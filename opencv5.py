import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("ruchit.png")
mask = np.zeros(img.shape[:2], np.uint8)

bgModel = np.zeros((1,65), np.float64)
fgModel = np.zeros((1,65), np.float64)

rect = (300, 30, 421, 378)

cv2.grabCut(img, mask, rect, bgModel, fgModel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask ==2 )| (mask ==0), 0, 1).astype('uint8')
img = img*mask2[:, :, np.newaxis]

plt.subplot(121)
plt.title("GrabCut")
plt.xticks([], plt.yticks([]))
plt.imshow(img)
plt.subplot(122)
plt.imshow(cv2.cvtColor(cv2.imread("ruchit.png"), cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.xticks([]), plt.yticks([])
plt.show()