
archive = open("doc_1.txt", 'r')

content = archive.read()
content2  = archive.readline()
content3 = archive.readlines()


print("type: ", type(content))

print("archive.read()\n", content)
print("\narchive.readline()\n", content2)
print("\narchive.readlines()\n",content3)

archive.close()



