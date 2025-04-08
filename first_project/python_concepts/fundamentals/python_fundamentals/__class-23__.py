#Decision and repetition in python

# repetition estruct

# for

text = "development"

letter_to_count = "e"
counter = 0

for letter in text:
    if letter == letter_to_count:
        counter += 1

print(f'the letter "{letter_to_count}" appear {counter} times in the the word development')