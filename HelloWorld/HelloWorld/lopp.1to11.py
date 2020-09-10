for x in range(0,11):
    print(x)

tal1 = int(input("tal 1 : "))
tal2 = int(input("tal 2 : "))
if tal1<tal2:
    for x in range(tal1, tal2+1):
        print(x)
elif tal2<tal1:
    for x in range(tal2, tal1+1):
        print(x)
else:
    print(tal1)

while True:
    tal1 = int(input("tal 1 : "))
    tal2 = int(input("tal 2 : "))
    print(f"Total : {tal1+tal2}")
    conti = input("Vill du fortsätta (J/N) ? ->")
    if conti.lower()=="n":
        break

tal = int(input("Mata in ett tal för summa 10 gånger -> "))
sum = 0
for x in range(0,10):
    sum = sum + tal
print(f"Total : {sum}")

while True:
    loopTal = int(input("Mata in ett tal som >0 för loop -> "))
    if loopTal>0:
        for x in range(1,loopTal):
            print(x)
        break
    else:
        print("Fel tal, tal > 0")

while True:
    tal10 = int(input("Mata tal för 10: "))
    if tal10>10:
        print("Högre än 10")
    elif tal10<10:
        print("Värdet är för lågt")
    else:
        print("Rätt tal")
        break

print([x for x in range(1,100) if x%2==1])

tal30 = input("Mata ett tal <= 30: ")
if tal30.isdigit():
    if int(tal30)<=30:
        print([x for x in range(0,int(tal30)+1)])
    else:
        print("Du har matat in ett felaktigt tal, tal <=30")
else:
    print("Du har matat in ett ogiltigt tal")

name = input("Ditt namn: ").strip()
address = input("Ditt gatuadress :").strip()
post = input("Ditt postnummer: ").strip()
ort = input("Ditt postort: ").strip()
while True:    
    if name=="":
        print("Namn är tom ... ")
        name = input("Ditt namn: ").strip()
        continue
    if address=="":
        print("gatuadress är tom ... ")
        address = input("Ditt gatuadress :").strip()
        continue
    if post=="":
        print("postnummer är tom ... ")
        post = input("Ditt postnummer: ").strip()
        continue
    if ort=="":
        print("postort är tom ... ")
        ort = input("Ditt postort: ").strip()
        continue
    else:
        print("Alla uppgifter ifyllda")
        break

import math
templist=[]
while True:
    temp = float(input("matar in värden (temperatur) -> "))
    templist.append(temp)
    print(f"Total värde : {templist}")
    if len(templist)>=3:
        print(f"\tlast three värde : {templist[-3:]}")
        if math.fsum(templist[-3:])>25:
            print("\t\tAlarm !!! ")
            break

import random
while True:
    print("Rolling the dices...")
    print("The values are....")
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    print(f"{dice1}\n{dice2}")
    again=input("Rolling the dices again (y/n) ?").lower()
    if again!="y":
        break


