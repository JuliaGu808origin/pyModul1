#Utöka uppgift 2 med en inledande fråga där användaren får ange hur många tal den
#vill mata in. Gör sedan samma sak för att ta fram det största talet

num=int(input("Ange hur många tal du ska mata in -> "))
maxlist=[]
while True:
    tal=input("Mata in ett tal -> ")
    if tal.isdigit():
        maxlist.append(tal)
        if len(maxlist)==num:
            print(f"Max tal är : {max(maxlist)}")
            break
    else:
        print("Fel tal, typ Integer !")