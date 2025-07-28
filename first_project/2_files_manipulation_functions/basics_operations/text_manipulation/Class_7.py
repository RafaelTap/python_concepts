archive = open("doc_4.txt", 'w')
archive.write("step 1: open\nstep 2: read\nstep 3: close")

archive = open("doc_4.txt", 'r')
c3 = archive.readlines()

print("archive type: ", type(archive.name))
print("\narchive.readlines()", c3)
print(repr(c3))

archive.close()