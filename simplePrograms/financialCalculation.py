def compoundInterest(principal, rate, term):
    """
    This function calculates compound interest.
    Term and rate are assumed annunally.
    """
    rate = rate/100
    totalPayment = int(principal * ((1 + rate) ** (term)))
    interest = totalPayment - principal
    monthlyPayment = int(totalPayment / (term * 12))
    return (f"""Interest to be paid in {term} years = ${interest:,d}
Total amount to be paid in {term} years = ${totalPayment:,d}
Monthly Payment = ${monthlyPayment:,d}\n""")

def simpleInterest(principal, rate, term):
    """
    This function calculates simple interest.
    Term and rate are assumed annunally.
    """
    rate = rate/100
    interest = int(principal * rate * (term))
    totalAmount = int(principal + interest)
    monthlyPayment = int(totalAmount/(term*12))
    return (f"""Interest to be paid in {term} years = ${interest:,d}
Total amount to be paid in {term} years = ${totalAmount:,d}
Monthly Payment = ${monthlyPayment:,d}\n""")

print(compoundInterest(100000, 3, 10))
print(simpleInterest(100000, 3, 10))
