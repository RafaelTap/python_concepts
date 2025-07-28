import os

archive = open("basics_operations/hello_world.txt", 'w')
print(os.path.abspath(archive.name))

archive.write("hello world !!")
archive.write("\nlet's get it on !")

print(os.path.relpath(archive.name))
print(archive)

archive.close()