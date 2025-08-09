import os
import shutil

#organizing files according its extension

#creating a new directory
def newDirectories(directories):
    for directory in directories:
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
                print("directory created")
            except PermissionError as error:
                print("error: ", error)
            except Exception as e:
                print("error: ", e)

#moving files
def moveFile(or_directory):
    for file in os.listdir(or_directory):
        file_path = os.path.join(or_directory, file)
        if os.path.isfile(file_path):
           # extension = file.split('.')[-1].lower()
            extension = file.split('.')[-1]
            if extension in ['pdf', 'txt', 'JPG']:
                directory_destination = os.path.join(or_directory, extension)
                try:
                    shutil.move(file_path, directory_destination)
                    print(f"file {file} moved to {directory_destination}")
                except PermissionError as error:
                    print("error", error)
                except Exception as e:
                    print("error: ", e)
            else:
                print(f"extension {extension} from {file} is not supported")

def main():

    #create directory if not exist
    work_directory = "files"
    directories = [(os.path.join(work_directory, 'pdf')),
                   (os.path.join(work_directory, 'txt')),
                   (os.path.join(work_directory, 'jpg'))]

    #move file to correspondent directory
    moveFile(work_directory)

if __name__ == "__main__":
    main()

