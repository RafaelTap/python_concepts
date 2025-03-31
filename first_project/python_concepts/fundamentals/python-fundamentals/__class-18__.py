#Decision and repetition in python

#DECISION ESTRUCT

# if/else/elif

vnr = eval(input("enter a number: "))
print("value entered: ", vnr)
print("before if")

if vnr <= 100:
    print("into if")
elif  100<= vnr <= 500:
    print("into first elif")
elif 500<= vnr <= 1000:
    print("into second elif")
else:
    print("the number is greater then 1000")

print("out of if/else/elif")