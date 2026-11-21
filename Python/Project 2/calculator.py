history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Khata: Taghsim bar sefr emkan pazir nist@")
        return None

    return a / b

def power(a, b):
    return a ** b

def reminder(a, b):
    if b == 0:
        print("Khata: Taghsim bar sefr emkan pazir nist@")
        return None
    
    return a % b

def check_for_user():
    input("\nBaraye bazgasht be menu Enter bezanid...")

while True:

    print("\n===== CALCULATOR =====")
    print("1. Jam (+)")
    print("2. Tafriq (-)")
    print("3. Zarb (*)")
    print("4. Taghsim (/)")
    print("5. Tavan (**)")
    print("6. Baghi Mande (%)")
    print("7. Namayesh tarikhche")
    print("0. Khorooj")

    choice = input("\nYek gozine entekhab konid: ")


    match choice:
        case "0":
            print("Barname be payan resid.")
            break

        case "7":
            print("\n--- Tarikhche ---")

            if len(history) == 0:
                print("Hich mohasebei sabt nashode!")
            else:
                for item in history:
                    print(item)

            check_for_user()

            
            

        case "1" | "2" | "3" | "4" | "5" | "6":
            try:
                num1 = float(input("\nAdad aval ra vared konid: "))
                num2 = float(input("Adad dovom ra vared konid: "))

                match choice:
                    case "1":
                        result = add(num1, num2)
                        operator = "+"

                    case "2":
                        result = subtract(num1, num2)
                        operator = "-"

                    case "3":
                        result = multiply(num1, num2)
                        operator = "*"

                    case "4":
                        result = divide(num1, num2)
                        operator = "/"

                    case "5":
                        result = power(num1, num2)
                        operator = "**"

                    case "6":
                        result = reminder(num1, num2)
                        operator = "%"

            

                if result is not None:
                    print("\nNatije: ", result)

                    history.append(f"{num1} {operator} {num2} = {result}")

                    check_for_user()



            except ValueError:
                print("Khata: Lotfan faghat adad vared konid!")
        
        case _:
            print("Gozine Entekhab shode eshtebah ast!")