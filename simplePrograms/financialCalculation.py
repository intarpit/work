"""
Below are the programs, which can do finacial calculations for the user.
"""
def compoundInterest(amount, rate, term):
    """
    This function calculates compound interest.
    Term and rate are assumed annunally.
    """
    rate = rate/100
    totalPayment = int(amount * ((1 + rate) ** (term)))
    interest = totalPayment - amount
    monthlyPayment = int(totalPayment / (term * 12))
    return (f"""Interest to be paid in {term} years = ${interest:,d}
Total amount to be paid in {term} years = ${totalPayment:,d}
Monthly Payment = ${monthlyPayment:,d}\n""")

def simpleInterest(amount, rate, term):
    """
    This function calculates simple interest.
    Term and rate are assumed annunally.
    """
    rate = rate/100
    interest = int(amount * rate * (term))
    totalAmount = int(amount + interest)
    monthlyPayment = int(totalAmount/(term*12))
    return (f"""Interest to be paid in {term} years = ${interest:,d}
Total amount to be paid in {term} years = ${totalAmount:,d}
Monthly Payment = ${monthlyPayment:,d}\n""")

def carLoanCalculator(amount, rate, term):
    """
    This function calculates compound interest.
    Rate is assumed annunally and term is assumed monthly.
    """
    rate = rate/(100 * 12)
    discountRate = (((1 + rate) ** term) - 1) / (rate * (1 + rate) ** term)
    monthlyPayment = (amount / discountRate)
    monthlyPaymentInterger = int(round(amount / discountRate))
    totalCost = int(round(monthlyPayment * term))
    interest = totalCost - amount
    
    return (f"""Interest to be paid in {term} months = ${interest:,d}
Total amount to be paid in {term} months = ${totalCost:,d}
Monthly Payment = ${monthlyPaymentInterger:,d}\n""")

def homeMortgageCalculator(amount, rate, term):
    """
    This function calculates compound interest.
    Rate is assumed annunally and term is assumed monthly.
    """
    rate = rate/(100 * 12)
    tim = term * 12
    discountRate = (((1 + rate) ** tim) - 1) / (rate * (1 + rate) ** tim)
    monthlyPayment = (amount / discountRate)
    monthlyPaymentInterger = int(round(amount / discountRate))
    totalCost = int(round(monthlyPayment * tim))
    interest = totalCost - amount
    
    return (f"""Interest to be paid in {term} years = ${interest:,d}
Total amount to be paid in {term} years = ${totalCost:,d}
Monthly Payment = ${monthlyPaymentInterger:,d}\n""")


# print(compoundInterest(amount, rate, term)) #! Please add value of your choice instead of amount, rate and term (please enter term in years).
# print(simpleInterest(amount, rate, term)) #! Please add value of your choice instead of amount, rate and term (please enter term in years).
# print(carLoanCalculator(amount, rate, term)) #! Please add value of your choice instead of amount, rate and term (please enter term in months).
# print(carLoanCalculator(amount, rate, term)) #! Please add value of your choice instead of amount, rate and term (please enter term in years).