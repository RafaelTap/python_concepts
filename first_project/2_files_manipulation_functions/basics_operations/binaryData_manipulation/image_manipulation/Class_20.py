from PIL import Image

#rotate image

img = Image.open("IMG_6747.JPG")
rtt_image = img.rotate(90)
rtt_image.save("rotated-image.JPG")
print("rotated image")

rtt_image.show()
