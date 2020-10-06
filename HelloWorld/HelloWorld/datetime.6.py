import datetime
datumString = input("Ange datum: YYYY-mm-dd -> ")
datum = datetime.datetime.strptime( datumString, "%Y-%m-%d")

print(datum)
