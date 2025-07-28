from PIL import Image
import os

#crop image

i = "IMG_6747.JPG"

if os.path.exists(i):
    img = Image.open(i)
    crp_image = img.crop((100,100,100,100))
    crp_image.save("cropped-image.JPG")
    print("cropped image")
else:
    print("ERROR")