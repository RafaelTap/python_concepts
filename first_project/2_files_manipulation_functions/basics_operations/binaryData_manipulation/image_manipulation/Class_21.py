import cv2
from PIL import Image

# save image in specific archive

img = cv2.imread("IMG_6747.JPG")
if img is not None:
    cv2.imwrite("my-image-cv2.JPEG", img)
    print("Saved image using OpenCV")

img_2 = Image.open("my-image-cv2.JPEG")
img_2.show()