#Utöka uppgift 5 med att även ange mätdatum för varje mätvärde. Skriv sedan ut
#varje mätvärde på samma sätt men tillsammans med mätdatum

#ett sätt att lösa är att ha TVÅ listor. En med datum och en med temperaturen. Så
#man lagrar tillhörande data på SAMMA INDEX I båda arrayerna!

#Lös på sätt 2: skapa en klass med två properties

import math
import datetime

num=int(input("hur många mätningar som skall registreras? -> "))
tempdict={}
while True:
    try:
        temp=float(input("Ange värde för mätning -> "))
        today=datetime.datetime.now()
        todayStr= today.strftime("%Y-%m-%d, %H:%M:%S")
        addTemp={todayStr: temp}
        tempdict.update(addTemp)
    except:
        print("Fel värde ! Detta skall vara decimaltal !")
    if len(tempdict)==num:
        templist=tempdict.values()
        ave = round(math.fsum(templist)/len(templist), 2)
        print(f"Alla mätningar: {tempdict}")
        maxVärde=max(templist)
        for datum,value in tempdict.items():
            if value==maxVärde:
                print(f"Max värdet: {maxVärde}, datum är: {datum}")
        print(f"Medelvärdet: {ave}")
        break
