# that is three exception in python around data manipulation
# PermissionError, FileExceptionError, FileNotFoundError

# PermissionError

try:
    with open("n_file", 'r') as doc:
        document = doc.read()
        print(document)
except PermissionError as error:
    print(error)