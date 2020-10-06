import datetime

year = int(input("Ange år"))
month = int(input("Ange månad"))
datum = datetime.datetime(year,month,1)
datumNextMonth = datum  + datetime.timedelta(days=31)
datumFirstNextMonth = datetime.datetime(datumNextMonth.year,datumNextMonth.month,1)
lastThisMonth = datumFirstNextMonth + datetime.timedelta(days=-1)

print(lastThisMonth.day)

datum1 = datetime.datetime.now()
datum2 = datetime.datetime(datum1.year,12,24)
diff = datum2 - datum1

print(diff.days)

day = int(input("Ange dag"))
month = int(input("Ange månadsnummer"))
year = int(input("Ange år"))

datum1 = datetime.datetime.now()
datum2 = datetime.datetime(year,month,day)

if datum1.date() == datum2.date():
    print("Samma")