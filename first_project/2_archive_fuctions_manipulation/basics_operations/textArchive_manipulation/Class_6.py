archive = open("doc_3.txt", 'w')
archive.write("Name: Rafael Lucas\nAge: 35\ngender: male")

archive = open("doc_3.txt", 'r')

c3 = archive.readline()

print("archive type: ", type(archive.name))
print("\narchive.readline()", c3)
print(repr(c3))

c3 = archive.readline()
print("\narchive.readline()", c3)
print(repr(c3))

c3 = archive.readline()
print("\narchive.readline()", c3)
print(repr(c3))

archive.close()