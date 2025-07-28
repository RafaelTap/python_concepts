import cv2
from PIL import Image

#resize image
# interpolation: how pixels will be resized
# preserve the quality and make soft

img = cv2.imread("IMG_6747.JPG")
if img is not None:
    rsz_image = cv2.resize(img, (300, 200), interpolation=cv2.INTER_AREA)
    cv2.imwrite("resized-image-cv2.JPG", rsz_image)

img_2 = Image.open("resized-image-cv2.JPG")
img_2.show()
