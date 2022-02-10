
#? How to find the number of occurance of a letter in a string. Given requirement that the previous letter matches the current letter.
#! Using only one variable a at a time and comment out others.
# a = "aaabbbhhhddeeekkkssss"

# a = "hhhhfjjjjjjddbbbbeeennnnsskkkkklllaaassrrffggdddbbbggeeeehhhhhssssmmmm"

a ="gggggggddddddddggggggggggeettttttttttttjjjjjjjjjjgggggggsssssswlllllllllllllllllwwwwwwwwwwwwiiiiiiiiiiiiiddddeeeefffffffggggggrrrrrrrrrrrssssssss"

#? Finding the length of a string, creating an empty dictionary b, creating a variable num with value 0. 
print(len(a))
b = dict()
num = 0

#? Creating a loop and assigning the current letter and previous letter to a variable.
for w in range(0, len(a)):
    q = a[w - 1]
    s = a[w]
    
    #? Comparing if the previous letter matches to current letter.
    if q == s:
        #? If the current letter matches to previous letter and if it exist in the dictionary then incrementing the its occurance, Otherwise creating a new key.
        #? Also assigning the number next to the letter for tracking as where the letter is in the string.
        if f"{q}{num}" in b:
            b[f"{q}{num}"] += 1
        else:
            b[f"{q}{num}"] = 1
    #? If current letter doesn't matches to previous letter then incrementing the num variable and moving to the next letter.
    else:
        num += 1

print(b)

