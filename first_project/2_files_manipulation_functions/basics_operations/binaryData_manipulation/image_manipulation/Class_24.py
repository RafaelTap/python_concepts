import cv2
from PIL import Image

img = cv2.imread("IMG_6747.JPG", cv2.IMREAD_GRAYSCALE)
if img is not None:
    ret, bnr_image = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite("my-binary-image-cv2_2.JPG", bnr_image)

img_2 = Image.open("my-binary-image-cv2_2.JPG")
img_2.show()

