import os
from PIL import Image

i = "IMG_6747.JPG"

print(os.getcwd())
print(os.listdir())

if os.path.exists(i):
    img = Image.open(i)
    img.show()
    print("format: ", img.format)
    print("image mode: ", img.mode)
    print("size: ", img.size)
else:
    print("image do not exist")

