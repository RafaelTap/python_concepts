#data types in python

#sequences and dictionary

#strings

#strings delimiters

s_1 = 'apostrophes' #apostrophe

s_2 = "double quotes"

s_3 = '''triple apostrophes'''

s_4 = """triple quotes"""

print(f'{s_1}\n{s_2}\n{s_3}\n{s_4}\n')

#creating string

text = "hello, world !"
print(text, "\n")

#accessing characters with index

first_char = text[0]
second_char = text[1]
third_char = text[2]
last_char = text[-1]
print(f'{first_char}\n{second_char}\n{third_char}\n{last_char}')

#cutting the string

sub_text = text[3:6]
print("Substring: ", sub_text, "\n")

#string concatenation

text_1 = "Hey " + "hoy " + "Let's go" + "!"
print(text_1, "\n")

#splitting a string (words list)

words_list = text.split()
print("Words list: ", words_list, "\n")

#modifying parts of the string

modified_text = text.replace("world", "fellas")
print(f'new text {modified_text}')

# putting string in upper case or lower case

text_2 = "COME ON every body"
print("original text", text_2, "\n")

lower_text = text_2.lower()
upper_text = text_2.upper()
print(f'text in lower case: {lower_text}\n')
print(f'text in upper casa: {upper_text}\n')

#removing blanc spaces (trim)

text_3 = "  hello,  world ! "
print(text_3,"\n")
trim_text = text_3.strip()
print("No extra spaces: ", trim_text, "\n")

#checking if there is a specific word in the text

if "fellas" in text_3:
    print("the word world is in the text")
else:
    print("the word world is not in the text\n")

#string formatting(TO FORMAT)
age = 35
name = "rafael"
text_formatted = f'my name is {name} and i am {age}\n'
text_formatted_2 = "my name is {} and i'm {}".format(name, age)
print(text_formatted)
print(text_formatted_2)
