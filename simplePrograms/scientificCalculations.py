"""
The below programs are for making scientific calculations
"""

def newtonSecondLaw():
    """
    This function can calculate either force, mass or acceleration.
    Will ask for the other two values to calculate one of the above.
    """
    while True:
        #? Getting input from the user and validating it. Asking what user would like to calculate.
        try:
            print("""
            Please type one from the below for the below question.
            For Force = f
            For Mass of the object = m
            For Acceleration = a \n
            """)    
            find = str(input("What would you like to find? "))
            find = find.strip()
            find = find.lower()
            inp = ["f", "m", "a"]
            if find in inp:
                pass
            else:
                print("Please enter a valid value.")
                continue
        except ValueError:
            continue

        def force():
            """This function calculates force and asks for mass and acceleration."""
            while True:
                #? Getting input from the user and validating it.
                try:
                    mas = float(input("Please enter the mass of the object: "))
                    acc = float(input("Please enter the acceleration of the object: "))
                except ValueError:
                    print("Please enter interger or decimal number only.\n")
                    continue
                forc = mas * acc
                return (f"Force = {round(forc, 2)}")
                break

        def mass():
            """This function calculates mass and asks for force and acceleration."""
            while True:
                #? Getting input from the user and validating it.
                try:
                    forc = float(input("Please enter the force applied to the object: "))
                    acc = float(input("Please enter the acceleration of the object: "))
                except ValueError:
                    print("Please enter interger or decimal number only.\n")
                    continue
                mas = forc / acc
                return (f"Mass = {round(mas, 2)}")
                break

        def acceleration():
            """This function calculates acceleration and asks for force and mass."""
            while True:
                #? Getting input from the user and validating it.
                try:
                    forc = float(input("Please enter the force applied to the object: "))
                    mas = float(input("Please enter the mass of the object: "))
                except ValueError:
                    print("Please enter interger or decimal number only.\n")
                    continue
                acc = forc / mas
                return (f"Acceleration = {round(acc, 2)}")
                break

        #? Calling the above functions based on user's input as what he/she would like to calculate.
        if find == "f":
            print(force())
        elif find == "m":
            print(mass())
        else:
            print(acceleration())


#? Calling the function.
newtonSecondLaw()