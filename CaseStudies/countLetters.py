"""
The below program counts letters in a sentence or paragraph
"""

import string

#? User input
sentence = str(input("""Please input a single or multiple line sentences below: \n \n"""))

#? Converting all the characters in lower.
sentence = sentence.lower()

allLetters = string.ascii_lowercase

#? Counting all the characters in a sentence and storing it in the dictionary.
countedLetters = dict()
for char in sentence:
    for letter in allLetters:
        if char == letter:
            if char in countedLetters:
                countedLetters[char] += 1
            else:
                countedLetters[char] = 1
print("\n")
print(countedLetters)
