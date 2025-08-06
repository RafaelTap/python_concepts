
text = open("file.txt", 'w')

text.write("welcome to the data manipulation course with python\n"
           "\nhere you will learn how to manipulate binary datas,\n"
           "\ntexts, audios and strings.\n"
           "\nEnjoy this moment and make the difference for your life !!")

text = open("file.txt", 'r')

content = text.read()
content_2 = text.readlines()
content_3 = text.readline()
print(repr(content), type(content), "\n")
print(repr(content_3), "\n")

text.close()




