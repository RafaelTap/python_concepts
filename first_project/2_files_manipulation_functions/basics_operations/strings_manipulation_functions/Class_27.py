with open("file.txt", 'r') as text:
    print("total of lines in document")
    counter = 0
    for line in text:
        if line:
            counter += 1
    print("total", counter)

with open("file.txt", 'r') as doc:
    print("real total of lines in document")
    counter = 0
    for line in doc:
        if line.strip():
            counter += 1
    print("total: ", counter)
