#Skapa en array av 5 heltal och fyll den med värden. Byt ut alla udda tal i arrayen mot
#talet 0. Skriv sedan efteråt ut innehållet i hela arrayen till skärmen

import random
heltal=[]
for x in range(0,5):
    heltal.append(random.randint(1,100))
print(heltal)
for x in range(0,5):
    if heltal[x]%2 != 0:
        heltal[x]=0
print(heltal)