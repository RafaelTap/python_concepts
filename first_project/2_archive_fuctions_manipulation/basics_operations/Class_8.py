archive = open("doc_5.txt", 'w')
archive.write("step 1: open\nstep 2: read\nstep 3: close")

archive = open("doc_5.txt", 'r')

for line in archive:
    print(repr(line))

archive.close()