import os

# method os.DirEntry
# is_dir() -> check if is a directory
# is_file() -> check if is an archive
# stat() -> return attributes from archive/directory
# stat().st_size() -> file size.
# .path() ->

with os.scandir("new_directory_2") as entries:
    for entry in entries:
        print(f"{entry.name} is a directory: {entry.is_dir()}")
        print(f"\n{entry.name} is a file: {entry.is_file()}")
        print(f"\n{entry.name} attribute: {entry.path}")
        print(f"\n{entry.name} size: {entry.stat().st_size}")
