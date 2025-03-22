#data types in python

#sequences and dictionary

#sequence

#list

list_ = [10, 20, 30, 40, 50] # list, as a vector in java.
print("List: ", list_, "\n")

#accessing the elements through the index.

first_number = list_[0]
second_number = list_[1]
third_number = list_[2]
fourth_number = list_[3]
fifth_number = list_[4]

#printing the elements

print(f"{first_number}")
print(f"{second_number}")
print(f"{third_number}")

#adding elements to the list

list_.append(60)

print("List with new element: ", list_)

#inserting element in a specific position, through index.

list_.insert(2, 11)
print("New element in a specific postion: ", list_,"\n")

#removing element from the list: the element removed is the first founded inside the list with the same value.

list_.remove(50)
print("List without element '50': ", list_, "\n")

#removing the last element of the list

last_element = list_.pop() #identify the last element
print(f'the last element:  {last_element}')
print("Removing the last element: ", list_)

#acessing a subgroup of the list

sub_list = list_[1:4]
print(f'Subgroup(index 1,2,3): {sub_list} \n')

#iterating on the elements of the list

for element in list_:
    print(element)