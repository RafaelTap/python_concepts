#good practice when we are manipulating data

with open("doc_7.text", 'r') as archive:
    for lines in archive:
        print(lines)

print("\nend of archive", archive.name)