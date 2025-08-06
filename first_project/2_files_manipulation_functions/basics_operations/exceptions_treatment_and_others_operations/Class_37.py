import os
from logging import exception

# functions remove and rename

# remove

file_to_remove = "n_file_.txt"
try:
    os.remove(file_to_remove)
except FileNotFoundError as error:
    print(error)
except exception as e:
    print({e})

