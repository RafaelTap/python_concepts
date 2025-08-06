# that are three exception in python around data manipulation
# PermissionError, FileExceptionError, FileNotFoundError

# FileExistsError

try:
    with open("n_file.txt", 'w') as doc:
        doc.write("new document.")
except FileExistsError as error:
    print("file already exists")

