archive = open("doc_2.txt", 'w')
archive.write("software analysis and development\nstudying the basics operations to manipulate datas in archive.")

archive = open("doc_2.txt", 'r')

c3 = archive.read()

print("archive type: ", type(archive.name))
print("\narchive.read()", c3)
print(repr(c3))

archive.close()