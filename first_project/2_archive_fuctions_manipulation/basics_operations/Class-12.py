#using append 'a'

archive = open("doc_7.text", 'a')
archive.write("\nnew content (line) to archive.")

archive = open("doc_7.text", 'r')
print(archive.read())

archive.close()