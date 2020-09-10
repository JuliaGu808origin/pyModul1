isAntal=True
while isAntal:
    try:
        antal = int(input("Mata in antal minuter (minst 60, typ Integer) -> "))
        if antal<60:
            print("Fel antal, minst antal är 60 minuter.")
        else:
            isAntal = False
    except:
        print("Fel antal, int behöver mata in.")    
timmar = antal/60
minuter = antal%60
print(f"Detta är {timmar} timmar och {minuter} minuter")



