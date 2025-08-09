import os

# exceptions and os module

def processFile(or_file, des_file):
    try:
        with open(or_file, 'r') as or_doc:
            content = or_doc.read()
    except FileNotFoundError as error:
        print("error: ", error)
        return
    except FileExistsError as error:
        print("error: ", error)
        return
    except Exception as e:
        print("error: ", e)
        return

    try:
        with open(des_file, 'w') as doc:
            doc.write("head: file content\n")
            doc.write(content)
            print("content added in: ", des_file)
    except PermissionError as error:
        print("error: ", error)
    except Exception as e:
        print("error: ", e)


def main():
    work_directory = "new_directory_2"
    or_file = os.path.join(work_directory, "new_doc.txt")
    des_file = os.path.join(work_directory, "des_file.txt")

    processFile(or_file, des_file)


if __name__ == "__main__":
    main()

