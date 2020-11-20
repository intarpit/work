"""
The below program analysis a credit card number and return the name of the company, which issued the card.
"""
#? Collect card number from customer.
card_number = str(input("What's your card number?\n"))

#? Condition for a particular card provider type.
amex = [[3, 4], [3, 7]]
master_card = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]
visa = 4

#? Anaysis the card number and return the name of the card provider.
check = [int(card_number[0]), int(card_number[1])]
if check in amex:
    print("AMEX")
elif check in master_card:
    print("MASTER CARD")
elif check[0] == visa:
    print("VISA")
else:
    print("INVALID CARD")