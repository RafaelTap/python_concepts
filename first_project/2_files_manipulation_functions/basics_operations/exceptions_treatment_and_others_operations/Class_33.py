# that are three exception in python around data manipulation
# PermissionError, FileExceptionError, FileNotFoundError

 #FileNotFoudError

try:
    with open("n_file_1.txt", 'r') as doc:
        document = doc.read()
        print(document)
except FileNotFoundError as error:
    print("")
    print(error)


