#Decision and repetition in python

#DECISION ESTRUCT

# if/else/elif

vnr = eval(input("enter a number: "))
print("value entered: ", vnr)
print("before if")

if vnr <= 100:
    print("into if")
elif  100<= vnr <= 500:
    print("into elif")
else:
    print("the number is greater then 500")

print("out of if/else/elif")