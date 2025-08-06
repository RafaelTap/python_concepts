text = open("file.txt", 'r')

for line in text:
    print(line.strip()) #remove character in begin and in the end of line .strip()