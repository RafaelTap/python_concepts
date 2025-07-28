from PIL import Image
import os

i = "resized-image.JPG"

if os.path.exists(i):
        img = Image.open(i)
        img.show()
        print("Image size: ", img.size)
else:
    print("ERROR")

