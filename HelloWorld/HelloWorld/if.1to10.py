tal = int(input("mata in ett tal -> "))
if tal>10:
    print("Talet är större än 10")
elif tal<10:
    print("Talet är mindre än 10")
else:
    print("Jag vet inte")

milk = int(input("Mata in hur många paket mjölk som finns kvar -> "))
if milk < 10:
    print("Beställ 30 paket.")
elif milk >20:
    print("Du behöver inte beställa någon mjölk")
else:
    print("Beställ 20 paket")

tempen = float(input("Mata in temperaturen tagen från en febertermometer -> "))
if tempen >= 37.8:
    if tempen >= 39.5:
        print("Du bör uppsöka läkare")
    else:
        print("Du har feber")
else:
    print("Du har inte feber")

try:
    age = int(input("Mata in din ålder (typ Integer) -> "))
    if age<18:
        print("Du är ej myndig")
    elif age>65:
        print("Du är pensionär")
    else:
        print("Du är myndig men inte pensionär")
except:
    print("Du har ar matat in en felaktig ålder, typ Integer")

katagori = input("Vilken kategori du tillhör ?\nv -> vuxen\np -> pensionär\ns -> student\n")
if katagori.lower()=="s" or katagori.lower()=="p":
    print("Kostar resan 20 kr")
elif katagori.lower()=="v":
    print("kostar resan 30 kr")
else:
    print("Du har angett en felaktig kategori")

birth = int(input("Mata in ditt födelse år -> "))
if 1980<=birth<1990:
    print("Du är född på 1980-talet")
elif 1990<=birth<2000:
    print("Du är född på 1990-talet")
else:
    print("Du är inte född på 1990 eller 1980-talen")

import  getpass
name=input("Skapa användarnamn -> ")
password=getpass.getpass("Skapa lösenord -> ")
user = input("Ange användarnamn -> ")
userpw = getpass.getpass("Ange lösenord -> ")
print("Log in ...")
if user==name and userpw==password:
    print("Du är inloggad")
else:
    print("fel lösenord eller fel användarnamn")

land = input("Mata in namnet på ett land där den bor").lower()
if land in ['sverige','danmark','norge']:
    print("Du bor i Skandinavien")
else:
    print("Du bor inte i Skandinavien")

car = input("Mata in ett bilmärke -> ").lower()
if car != "volvo":
    if car in ['volkswagen','bmw','audi']:
        print("Bilen är tysk")
    elif car in ['renault','peugeot','citroen']:
        print("Bilen är fransk")
    else:
        print("Bilen inte är tysk eller fransk eller svensk")

money=float(input("Summa pengar -> "))
disc=input("Rabatt, j / n ?-> ")
if 15<=money<=25 and disc=="n":
    print("Du kan köpa en liten hamburgare")
elif 15<=money<=25 and disc=="j":
    print("Du kan köpa en liten hamburgare och en pommes frites")
elif 25<money<=50 and disc=="n":
    print("Du kan köpa en stor hamburgar")
elif 25<money<=50 and disc=="j":
    print("kan köpa en stor hamburgare och pommes frites")
elif money>60 or (50<money<60 and disc=="j"):
    print("Du kan köpa ett meal med dryck")
else:
    pass