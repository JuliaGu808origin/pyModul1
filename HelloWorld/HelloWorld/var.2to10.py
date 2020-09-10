myName= "Julia Gu"
print(f"Hello {myName}")

age = 25
print(f"{myName} is {age} years old")

firstname = input("ditt förnamn: ")
lastname = input("ditt efternamn: ")
print(f"Du heter: {lastname}, {firstname}")

tal1 = int(input("tal 1 : "))
tal2 = int(input("tal 2 : "))
print(f"total is : {tal1+tal2}")

import datetime
birthYear = int(input("Ditt födelseåret: "))
thisYear = datetime.datetime.now().year
dayBirthYear = datetime.datetime(birthYear,1,1)
dayThisYear = datetime.datetime(thisYear,1,1)
days = ( dayThisYear-dayBirthYear ).days
print(f"Din ålder är: {birthYear}")
print(f"Det är {days} mellan dem")

num1 = int(input("tal 1: "))
num2 = int(input("tal 2: "))
sum = num1+num2
diff = abs(num1-num2)
aver = sum/2
print(f"summa: {sum}\ndifferens: {diff}\nmedelvärde: {aver}")

summa = float(input("mata in en summa -> "))
newSumma = summa*1.25
print(f"Den nya summan med moms är: {newSumma}")