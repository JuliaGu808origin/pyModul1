#Skapa ett program där användaren får mata in en inköpslista. Börja med att fråga
#användaren hur många varor den skall ha på sin lista. Gör en loop som gås igenom
#det antal gånger som användaren angivit. Inne i loopen skall tre frågor anges- Vilken
#vara som användaren vill lägga till- Vilket pris varan har – Vilket produktnummer.
#Spara alla dessa värden i en array. Loopa sedan igenom arrayen och skriv ut alla
#varor som användaren har angivit med alla uppgifter på skärmen.

num=int(input("Hur många varor skall ha på din lista ? -> "))
listor=[]
for x in range(0,num):
    name=input("Vara namn du vill lägga till -> ")
    price=float(input("Vilket pris varan har -> "))
    number=input("Vilket produktnummer -> ")
    obj={"name":name, "price":price, "productNum":number}
    listor.append(obj)
print("Din listor : ")
for x in listor:
    print(x)