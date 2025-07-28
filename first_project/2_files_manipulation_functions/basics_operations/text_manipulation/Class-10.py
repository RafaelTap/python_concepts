archive = open("doc_6.txt", 'w')
archive.write("data manipulation with  python\nan initial approach")

archive = open("doc_6.txt", 'r')
a1 = archive.read()
print("using write() method: ", a1)

archive.close()


