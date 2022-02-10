#? How to slice a string and to figure out all the valid ip address from that string.
#! Activate only one value of variable s at a time.
# s = "25525511135"

# s = "1000253"

s = "73515189"

# print(type(int(s)))
# print(len(s))

#? Slicing the string into 4 pieces.
for r in range(1, len(s)):
    first = s[0:r]
    for d in range(r, len(s)):
        second = s[r:d]
        for w in range(len(s)):
            third = s[d:w]
            fourth = s[w:]
            
            #? Getting rid of all the blank strings or string, which has a value 0.
            if first != "" and second != "" and third != "" and fourth != "":
                first_int = int(first)
                second_int = int(second)
                third_int = int(third)
                fourth_int = int(fourth)

                #? Checking if each slice of the string in within the required range of 0 to 255, where is 0 is avioded and 255 is included.
                if first_int > 0 and first_int <= 255:
                    if second_int > 0 and second_int <= 255:
                        if third_int > 0 and third_int <= 255:
                            if fourth_int > 0 and fourth_int <= 255:
                                print(f"{first}.{second}.{third}.{fourth}")
