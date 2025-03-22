#data types in python

#sequences and dictionary

#dictionary

#key:value, as a json

dictionary = {
    "name": "rafael",
    "age": 35,
    "city": "Rio de Janeiro"
}

print(dictionary, "\n")

#acessing the values through the keys

name = dictionary ["name"]
age = dictionary ["age"]
city = dictionary ["city"]

print("Name: ", name)
print("Age", age)
print("City: ", city, "\n")

#adding value to the dictionary

dictionary ["profession"] = "software developer"

print(dictionary, "\n")

#modifyng the value associated with a key of dictionary

dictionary["age"] = 36
print("Age modified: ", dictionary, "\n")

#removing a data from dictionary(key:value)

del dictionary["city"]
print("Dictionary without city: ", dictionary, "\n")

#acessing all keys and values from dictionary

keys = dictionary.keys()
print("Dictionary Keys: ", keys, "\n")

values = dictionary.values()
print("Dictionary values: ", values, "\n")

#iterationg in dictionary

for key, value in dictionary.items():
    print(f'{key}:{value}')

#cheking if value is in the dictionary

if "name" in dictionary:
    print(f'\nThe name in dictionary is: {dictionary["name"]}')
else:
    print("The key (name) isn't on dictionary.")

#using the method get() to access values in security

profession = dictionary.get("profession", "unknown") #unknown is in case the profession has not a value.
print("\nProfession: ", profession)

#clearing the dictionary

dictionary.clear()
print(dictionary)

