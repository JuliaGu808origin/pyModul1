#Skapa ett program där användaren skall mata in kontaktuppgifter. Ta emot alla
#värden i variabler. Skapa ett objekt (Person) och sätt värden. Lagra i LISTA!
#Fråga om användaren vill mata in en ny person(J/N) Om J återupprepa.
#Detta kan göras max 5 gånger.
#Svarar användaren N eller om 5 personer matats in- skriv ut alla personers uppgifter på
#skärmen. 

class Person():
    def __init__(self, firstname, lastname, age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
    def __str__(self):
        return self.firstname.title()+" "+self.lastname.title()+" är "+self.age+" år."
personlist=[]
while True:
    first=input("Ditt förstname -> ")
    last=input("Ditt eftername -> ")
    age=input("Ditt år -> ")
    person=Person(first,last,age)
    personlist.append(person)
    if 0<=len(personlist)<5:
        conti=input("Vill du mata in en ny person (J/N) ? -> ").lower()
        if conti == "j":
            pass
        else:
            break
    else:
        break
for x in personlist:
    print(x)
