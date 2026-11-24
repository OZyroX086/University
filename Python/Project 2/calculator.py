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

def absolute(a):
    if a < 0:
        return -a
    return a

def square_root(a):
    if a < 0:
        print("Khata: Jazr adad manfi emkan pazir nist!")
        return None

    return a ** 0.5

def percentage(a, b):
    return (a * b) / 100

def average(a, b):
    return (a + b) / 2

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
    print("7. Ghadr Motlagh")
    print("8. Jazr")
    print("9. Darsad")
    print("10. Miyangin (Average)")
    print("11. Namayesh tarikhche")
    print("12. Pak kardan tarikhche (Clear History)")
    print("0. Khorooj")

    choice = input("\nYek gozine entekhab konid: ")

    match choice:
        case "0":
            print("Barname be payan resid.")
            break

        case "11":
            print("\n--- Tarikhche ---")

            if len(history) == 0:
                print("Hich mohasebei sabt nashode!")
            else:
                for item in history:
                    print(item)

            check_for_user()

        case "12":
            history.clear()
            print("\nTarikhche ba movafaghiat pak shod!")

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

        case "7" | "8":
            try:
                num = float(input("\nAdad ra vared konid: "))

                match choice:
                    case "7":
                        result = absolute(num)
                        operator = "Ghadr Motlagh"

                    case "8":
                        result = square_root(num)
                        operator = "Jazr"

                if result is not None:
                    print("\nNatije: ", result)
                    history.append(f"{operator} ({num}) = {result}")

                check_for_user()

            except ValueError:
                print("Khata: Lotfan faghat adad vared konid!")

        case "9":
            try:
                num1 = float(input("\nAdad ra vared konid: "))
                num2 = float(input("Darsad ra vared konid: "))

                result = percentage(num1, num2)

                print("\nNatije: ", result)

                history.append(f"{num2}% of {num1} = {result}")

                check_for_user()

            except ValueError:
                print("Khata: Lotfan faghat adad vared konid!")

        case "10":
            try:
                num1 = float(input("\nAdad aval ra vared konid: "))
                num2 = float(input("Adad dovom ra vared konid: "))

                result = average(num1, num2)

                print("\nNatije: ", result)

                history.append(f"Average ({num1}, {num2}) = {result}")

                check_for_user()

            except ValueError:
                print("Khata: Lotfan faghat adad vared konid!")

        case _:
            print("Gozine Entekhab shode eshtebah ast!")