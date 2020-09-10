#Skapa en array som skall innehålla temperaturmätningar. Användaren får först upp
#en fråga om hur många mätningar som skall registreras. Sedan får denne ange
#värde för varje mätning. Detta skall vara decimaltal. Skriv sedan ut alla mätningar
#och avsluta med att ange en max och en medeltemperatur. 

import math

num=int(input("hur många mätningar som skall registreras? -> "))
templist=[]
while True:
    try:
        temp=float(input("Ange värde för mätning -> "))
        templist.append(temp)
    except:
        print("Fel värde ! Detta skall vara decimaltal !")
    if len(templist)==num:
        ave = round(math.fsum(templist)/len(templist), 2)
        print(f"Alla mätningar: {templist}")
        print(f"Max värdet: {max(templist)}")
        print(f"Medelvärdet: {ave}")
    