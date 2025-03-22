# repetition struct and auxiliary instruction in python

# while

# while block inside while block

while True:
    print("You are inside the first while block.")
    option_1 = input("Wanna go out of block ? Enter 'YES' to go out. ")
    if option_1 == 'YES':
        break
    else:
        while True:
            print("you are inside the second while block. ")
            option_2 = input("Wanna go out of block ? Enter 'YES' to go out. ")
            if option_2 == 'YES':
                break
        print("you are out of second block. ")

print("you are out of first block. ")
