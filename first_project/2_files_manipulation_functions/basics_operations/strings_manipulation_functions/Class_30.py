#.join() to add characters 
my_list = ["rice", "bean", "potato"]

text_1 = ",".join(my_list)
with open("file_2", 'w') as doc:
    doc.write(text_1)

text_2 = "\n".join(my_list)
with open("file_3", 'w') as doc:
    doc.write(text_2)