import os

# functions remove and rename

# rename

my_file = "n_file.txt"
my_file_newName = "n_file_new.txt"

try:
    os.rename(my_file, my_file_newName)
    print("file renamed")
except FileNotFoundError as error:
    print(error)
except Exception as e:
    print("file not renamed: ", e)
