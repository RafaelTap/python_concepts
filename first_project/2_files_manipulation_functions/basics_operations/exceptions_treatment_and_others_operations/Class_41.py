import os

#scandir() -> scan all files from directory

with os.scandir("new_directory_2") as entries:
    for entry in entries:
        print(entry.name)


