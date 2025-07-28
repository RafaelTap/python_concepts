# binary data manipulation (image)

from PIL import Image
import numpy as np

def main():

    #open the image
    img = Image.open("IMG_6748.JPG")
    img.show()

    # convert image in binary data
    img_data = np.array(img)
    binary_data = img_data.tobytes()

    # save binary datas in archive
    with open("original_img.bin", "wb") as file:
        file.write(binary_data)

    # copy the binary file
    with open("original_img.bin", "rb") as original_file:
        data = original_file.read()

    with open("copy_img.bin", "rb") as copy_file:
        copy_file.write(data)

    #manipulate binary datas archive
    with open("copy_img.bin", "rb") as file:
        data = bytearray(file.read())

    data  = data[::-1]

    with open("copy_image.bin", "wr") as file:
        file.write(data)

    #load the manipulated image
    modified_data = np.frombuffer(data, dtype=np.uint8).reshape(img_data.shape)
    modified_img = Image.fromarray(modified_data)
    modified_img.show()

if __name__ == "__main__":
    main()