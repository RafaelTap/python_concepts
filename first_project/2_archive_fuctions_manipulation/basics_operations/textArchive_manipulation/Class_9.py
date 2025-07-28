archive = open("doc_5.txt", 'w')
archive.write("Python version: 3.10\nIDE: Eclipse:\nData base: postgreSQL\ndbms: Dbeaver")

archive = open("doc_5.txt", 'r')
a1 = archive.read()

print(repr(a1))
print("\n", a1)

archive.close()

archive_r = open("doc_5.txt", 'r')


