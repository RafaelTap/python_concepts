from PIL import Image
import cv2

# converts an image in from colors space to other
# BGR TO GRAY SCALE.

img = cv2.imread("IMG_6747.JPG", cv2.IMREAD_GRAYSCALE)
if img is not None:
    ret, binary_image = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite("binary-image.JPG", binary_image)
    print("binary image")

img_2 = Image.open("binary-image.JPG")
img_2.show()