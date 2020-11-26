"""
The below programs can be used for converting units.
"""

def milesToKilometer(miles):
    """Can be used to convert miles to kilometers"""
    kilometer = miles * 1.6
    return (f"kilometer = {round(kilometer, 2)}")

def kilometerToMiles(kilometer):
    """Can be used to convert kilometers to miles"""
    miles = kilometer/1.6
    return (f"miles = {round(miles, 2)}")

def poundsTokilograms(pounds):
    """Can be used to convert pounds to kilograms"""
    kilograms = pounds/2.2
    return (f"kilogram = {round(kilograms, 2)}")

def kilogramsToPound(kilograms):
    """Can be used to convert kilograms to pounds"""
    pounds = kilograms*2.2
    return (f"pounds = {round(pounds,2)}")

def celsiusToFahrenheit(celsius):
    """Can be used to convert celsius to fahrenheit"""
    fahrenheit = (celsius * (9/5)) + 32
    return (f"fahrenheit = {round(fahrenheit,2)}") 

def fahrenheitToCelsius(fahrenheit):
    """Can be used to convert fahrenheit to celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return (f"celsius = {round(celsius,2)}")

def celsiusToKelvin(celsius):
    """Can be used to convert celsius to Kelvin"""
    kelvin = celsius + 273.15
    return (f"kelvin = {round(kelvin,2)}")

def kelvinToCelsius(kelvin):
    """Can be used to convert kelvin to celsius"""
    celsius = kelvin - 273.15
    return (f"celsius = {round(celsius,2)}")

def fahrenheitTokelvin():
    """Can be used to convert fahrenheit to kelvin"""
    while True:
        try:
            fahrenheit = float(input("Please enter a value: "))
        except ValueError:
            print("Please input a valid integer.\n")
            continue
        kelvin = ((fahrenheit - 32) * 5/9) + 273.15
        return (f"kelvin = {round(kelvin, 2)}")

def kelvinToFahrenheit(kelvin):
    """Can be used to convert kelvin to fahrenheit"""
    fahrenheit = ((kelvin - 273.15) * 9/5) + 32
    return (f"fahrenheit = {round(fahrenheit, 2)}")

# print(milesToKilometer(value)) #! Please add value of your choice and remove the word value.
# print(kilometerToMiles(value)) #! Please add value of your choice and remove the word value.
# print(poundsTokilograms(value)) #! Please add value of your choice and remove the word value.
# print(kilogramsToPound(value)) #! Please add value of your choice and remove the word value.
# print(celsiusToFahrenheit(value)) #! Please add value of your choice and remove the word value.
# print(fahrenheitToCelsius(value)) #! Please add value of your choice and remove the word value.
# print(celsiusToKelvin(value)) #! Please add value of your choice and remove the word value.
# print(kelvinToCelsius(value)) #! Please add value of your choice and remove the word value.
# print(fahrenheitTokelvin()) #! Please add value of your choice and remove the word value.
# print(kelvinToFahrenheit(value)) #! Please add value of your choice and remove the word value.
