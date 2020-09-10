def metod5(age):
    if int(age)<18:
        return False
    return True
age=input("Mata in din ålder, heltal -> ")
if age.isdigit():
    if metod5(age):
        print("Du är myndig")
    else:
        print("Du är inte myndig")
else:
    print("Fel tal")