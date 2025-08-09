import os

# directory manipulation
# create

try:
    os.mkdir("new_directory_2")
    print("directory deleted")
except PermissionError as error:
    print("do not permission to create directory")
    print("description: ", error)
except FileExistsError as error:
    print("directory already exists")
    print("description: ", error)


