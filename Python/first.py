students_counts = int(input("Tedad Daneshjoo Vared Konid: "))

student = 1

while student <= students_counts:
    print("\n--- Etela`at Daneshjoo " + str(student) + " ---")

    name = input("\nName Daneshjoo: ")
    id = input("ID Daneshjoo: ")

    total = 0
    tedad_dars = int(input("Tedad Dars Daneshjoo: "))

    for i in range(tedad_dars):
        nomre = float(input("\nNomre Dars " + str(i + 1) + " Vared Konid: "))
        total += nomre

    average = total / tedad_dars

    print("\n--- Gozaresh Daneshjoo " + str(student + 1) + " ---")

    print("\nName: " + name)
    print("ID: " + id)
    print("Average: " + str(average))

    if(average >= 10):
        print("\nGhabooli: Pass")
    else:
        print("\nGhabooli: Failed")

    student += 1

print("\nTamam Daneshjooyan Sabt Shodand!")
