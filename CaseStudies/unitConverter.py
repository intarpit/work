"""
The below programs can be used for converting units.
"""

def milesToKilometer(miles):
    """Can be used to convert miles to kilometers"""
    kilometer = miles * 1.6
    return round(kilometer, 2)

def kilometerToMiles(kilometer):
    """Can be used to convert kilometers to miles"""
    miles = kilometer/1.6
    return round(miles, 2)

def poundsTokilograms(pounds):
    """Can be used to convert pounds to kilograms"""
    kilograms = pounds/2.2
    return round(kilograms, 2)

def kilogramsToPound(kilograms):
    """Can be used to convert kilograms to pounds"""
    pounds = kilograms*2.2
    return round(pounds,2)

# print(miles_to_kilometer(5))
# print(kilometer_to_miles(8))
# print(poundsTokilograms(187))
# print(kilogramsToPound(85))
