import errno
import os

# directory manipulation
#remove
try:
    os.rmdir("new_directory") #creat new directory
    print("directory removed")
except OSError as error:
    print(error.errno)
    if error.errno == errno.ENOTEMPTY:
        print("directory not empty")
    else:
        print("unexpected error")
    print("description: ", error)

