"""
The below program takes a word or sentence and return the decoded message.
It increases or decreases the position of the letter in the alphabetic order based on the input(code key) provided.
"""
import string

#? Collecting the input from the user.
code = str(input("Please enter the coded message: "))
codekey = int(input("Please enter the code key: "))

#? Creating a dictionary of all the small letters, capital letters and space.
letters = string.ascii_letters + " "
i = 0
dictLetters = dict()
for letter in letters:
    dictLetters[i] = letter
    i += 1
# print(dictLetters)

#? Decoding the user provided message to the original message.
orignalCode = ""
for character in code:
    for key, value in dictLetters.items():
        if character == value:
            newCodeKey = ((key - codekey) % 53)
            orignalCode += dictLetters[newCodeKey]
# print(orignalCode)

#? Printing the original message.
print(f"The orignal message is {orignalCode}")