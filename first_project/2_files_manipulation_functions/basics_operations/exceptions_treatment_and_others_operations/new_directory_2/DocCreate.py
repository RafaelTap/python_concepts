with open("new_doc.txt", 'w') as doc:
    document = doc.write("new document exemple")

with open("new_doc.txt", 'r') as doc:
    document_1 = doc.read()
    print(f"type: {type(document_1)}\n{repr(document_1)}\n{document_1}")