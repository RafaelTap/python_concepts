try:
    with open("n_file_2.txt", 'r') as doc:
        document = doc.read()
        print(document)
except FileExistsError as error:
    print(error)
except FileNotFoundError as error:
    print(error)
except PermissionError as error:
    print(error)
