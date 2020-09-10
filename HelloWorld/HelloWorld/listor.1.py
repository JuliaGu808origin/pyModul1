#Skapa ett program där användaren får upp fyra frågor om att mata in ett tal. Spara
#alla talen i en array. Loopa igenom arrayen och ta fram det tal som är störst. Skriv
#tillbaka resultatet på skärmen för användaren 

maxlist=[]
while True:
    tal=input("Mata in ett tal -> ")
    if tal.isdigit():
        maxlist.append(tal)
        if len(maxlist)==4:
            print(f"Max tal är : {max(maxlist)}")
            break
    else:
        print("Fel tal, typ Integer !")

    