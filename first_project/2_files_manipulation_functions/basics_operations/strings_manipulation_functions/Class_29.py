# splitting string in words
text_1 = "i love lemon, apple, pineapple"
text_2 = "car, bike, skate, snowboard"
text_3 = "ball pen pencil"

print(text_1.split())
print(text_2.split())
print(text_3.split())

with open("file.txt", 'r') as doc:
    text = doc.read()
    split = text.split()
    splitCount = text.split().count("data")
    print(split)
    print("total of word 'data' using split() and count(): ", splitCount)