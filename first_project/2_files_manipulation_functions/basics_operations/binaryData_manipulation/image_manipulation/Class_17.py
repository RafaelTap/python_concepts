from PIL import Image
import os
#image resizing

i = ("IMG_6747.JPG")

if os.path.exists(i):
    img = Image.open(i)
    rs_image = img.resize((800, 800))
    rs_image.save("resized-image.JPG")
    print("resized image.")
else:
    print("image do not exist.")

