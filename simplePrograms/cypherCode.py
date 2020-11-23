"""
The below program takes a word or sentence and return a new coded message.
It increases or decreases the position of the letter in the alphabetic order based on the input(code key) provided.
"""
import string

#? Taking input from the user.
text = str(input("Please enter uncoded message: "))
codeKey = int(input("Please enter the key: "))

#? Creating a dictionary of all the small, capital letters including spaces.
letters = string.ascii_letters + " "
i = 0
dictLetters = dict()
for letter in letters:
    dictLetters[i] = letter
    i += 1
# print(listLetters)

#? Converting the user input text into new code based on the key provided by the user.
newCode = ""
for word in text:
    for key, value in dictLetters.items():
        if word == value:
            newCodeKey = ((key + codeKey)% 53) 
            newCode += dictLetters[newCodeKey]
# print(newCode)

#? Printing the new code.
print(f"The new code is {newCode}")
