"""
Below program returns the amount of cash to be returned to the customer,
when the customer pays for a product. It only calculated amount of cents to be returned.
Doesn't count notes, therfore the difference can't be more than $1.
It's ask the person the amount of cash received from the customer and the cost of the product.
"""
while True:
    cash_rec = float(input("Cash received: "))
    price = float(input("Cost of the product: "))
    if cash_rec >= price:
        print("System processing...")
        break
    else:
        print("Price is higher than cash received. Please collect more cash")
change = cash_rec - price
change = round(change, 2)
# print(change)
change = int(change * 100)
# print(change)

return_amount = dict()

cents = [50, 10, 5, 1]
while change != 0.00:
    if change >= cents[0]:
        if cents[0] in return_amount:
            return_amount[cents[0]] += 1
        else:
            return_amount[cents[0]] = 1
        change = change - cents[0]
    elif change >= cents[1]:
        if cents[1] in return_amount:
            return_amount[cents[1]] += 1
        else:
            return_amount[cents[1]] = 1
        change = change - cents[1]
    elif change >= cents[2]:
        if cents[2] in return_amount:
            return_amount[cents[2]] += 1
        else:
            return_amount[cents[2]] = 1
        change = change - cents[2]
    elif change >= cents[3]:
        if cents[3] in return_amount:
            return_amount[cents[3]] += 1
        else:
            return_amount[cents[3]] = 1
        change = change - cents[3]
print(return_amount)