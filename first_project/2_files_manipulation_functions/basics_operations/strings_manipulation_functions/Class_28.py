#countig words from the document with .count()
with open("file.txt", 'r') as doc:
    text = doc.read()
    counter = text.count("you")
    counter_2 = text.count("python")
    print("total of 'you': ", counter)
    print("total of 'python': ", counter_2)