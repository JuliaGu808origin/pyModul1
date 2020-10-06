################################################################################
#Skapa en array och generera 100 slump-tal som du lägger i arrayen.
#Visa hur man kan ta fram medelvärde av alla tal som är jämnt delbara med 3 
#och som finns i arrayen.
################################################################################

import random

slumps = []
for i in range(100): slumps.append(random.randint(1,100))
delav3 = [i for i in slumps if i % 3 == 0]
print(round((sum(delav3) / len(delav3)), 2))