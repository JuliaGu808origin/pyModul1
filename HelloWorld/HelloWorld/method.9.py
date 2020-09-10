def vokal(bokstav):
    if bokstav.lower() in ['a','e','i','o','u','y','å','ä','ö']:
        return True
    return False

test=input("Mata in en bokstav -> ")
if len(test)==1:
    print(vokal(test))
else:
    print("Fel bokstav")