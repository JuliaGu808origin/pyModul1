def PrintMessage():
    return "Hello World!"
print(PrintMessage())

def ToPercentage(tal):
    tal=tal*100
    return f"{tal}%"
try:
    tal=float(input("Mata in ett decimaltal mellan 1 och 0 ->"))
    if 0<=tal<=1:
        print(ToPercentage(tal))
except:
    print("Fel decimaital.")

def metod4(sum):
    return sum*0.25
try:
    sum=int(input("Mata in summan heltal -> "))
    print(f"Moms är {metod4(sum)}")
except:
    print("Fel tal")

def metod3(str1, str2):
    return str1+str2
if __name__ == "__main__":
    str1=input("Mata första sträng -> ")
    str2=input("Mata andra sträng -> ")
    print(metod3(str1,str2))
