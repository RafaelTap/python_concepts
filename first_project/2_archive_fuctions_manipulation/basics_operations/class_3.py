import os

image = open("IMG_6748.JPG", 'wb')

print(os.path.relpath(image.name))
print(os.path.abspath(image.name))

image.close()

print("archive name ", image.name)
print("archive mode ", image.mode)
print("archive is closed ? ", image.closed)
