import os

archive1 = open("doc_1.txt", 'w')
print(os.path.abspath(archive1.name))

archive1.write("python version: 3.10")
archive1.write("\nclass about archive functions manipulation")

print(os.path.relpath(archive1.name))
print(archive1)

archive1.close()