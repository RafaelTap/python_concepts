# repetition struct and auxiliary instruction in python

# while

print("before the while block")

word = input( "Enter a word: ")

"""
while word isn't 'exit', you are inside while block, 
on the other hand, if word is 'exit", you're out of the
block while.

"""
while word != "exit":
    print("inside while block")
    word = input("Enter exit to out of the while block.")

print("out of the block while.")

