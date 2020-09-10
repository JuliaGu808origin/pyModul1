str1 = input("Mata första sträng -> ")
str2 = input("Mata andra sträng -> ")
str3 = input("Mata tredje sträng -> ")
print(f"{str1+str2+str3}")

str="Hello, world"
print(f"Först w position är {str.index('w')}")

b="I am a C# hacker."
print(f"Sista a position är {b.rindex('a')}")
print(f"C position är {b.index('C')}, total längden är {len(b)}")
blist=b.split()
for x in blist:
    print(x)
newb=""
for x in b:
    if x.lower() in ['a','c','k','r']:
        newb=newb+x.upper()
    else:
        newb=newb+x.lower()
print(newb)

name="kurt andersson"
print(name.title())

text="Detta är en sträng som du skall ändra"
newtext=text.replace(" ","*")
count=newtext.count("*")
print(f"New text: {newtext}, {count} x '*'")

numstr="ett,två,tre,fyra,fem,sex,sju"
numarr=numstr.split(",")
print(numarr)

import re
email = input("Mata in ditt email -> ")
match=re.search(r'^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$', email)
if match:
    print("Rätt")
else:
    print("Fel")

mening=input("Mata in en mening -> ")
meningarr = mening.split()
words = list(filter(lambda x: x.strip()!="", meningarr))
print(f"Din mening: {mening}")
print(f"{len(words)} ord i den")

palindrom=input("Mata in ett ord eller en mening -> ").replace(" ","")
newpalindrom=palindrom[::-1]
if palindrom==newpalindrom:
    print("Rätt palindrom")
else:
    print("Inte palindrom")