
#? How to find the number of occurance of a letter/number/symbol in a string. Given requirement that the previous letter/number/symbol matches the current letter/number/symbol.
#! Using only one variable a at a time and comment out others.
# a = "aaa@@@@@@bbbhhh########dd@@@@@@@@@eeekkkssss######"

# a = "hhhhfjjjjjjddbbbbeeennnnsskkkkklllaaassrrffggdddbbbggeeeehhhhhssssmmmm"

# a ="gggggggddddddddggggggggggeettttttttttttjjjjjjjjjjgggggggsssssswlllllllllllllllllwwwwwwwwwwwwiiiiiiiiiiiiiddddeeeefffffffggggggrrrrrrrrrrrssssssss"

a = "kkkkjjjjjiiiiiiiiiiu88888888jjjjjjjjj7777777uuuuu8888888888kkkkkkkkkkk77777iiiiiii"

#? Finding the length of a string, creating an empty dictionary b, creating a variable num with value 0. 
print(len(a))
b = dict()
num = 0

#? Creating a loop and assigning the current letter/number/symbol and previous letter/number/symbol to a variable.
for w in range(0, len(a)):
    q = a[w - 1]
    s = a[w]
    
    #? Comparing if the previous letter/number/symbol matches to current letter.
    if q == s:
        #? If the current letter/number/symbol matches to previous letter/number/symbol and if it exist in the dictionary then incrementing the its occurance, Otherwise creating a new key.
        #? Also assigning the number next to the letter for tracking as where the letter/number/symbol is in the string.
        if f"{q}.{num}" in b:
            b[f"{q}.{num}"] += 1
        else:
            b[f"{q}.{num}"] = 1
    #? If current letter/number/symbol doesn't matches to previous letter/number/symbol then incrementing the num variable and moving to the next letter/number/symbol.
    else:
        num += 1

#? There is two parts to a key in the dictionary (result) printed.
#? First the letter/number/symbol in the string and second part (after ".") is the position of the letter/number/symbol in the string.
#? Value in the dictionary is the number of the occurance of the letter/number/symbol, when the conditions are met.
print(b)

