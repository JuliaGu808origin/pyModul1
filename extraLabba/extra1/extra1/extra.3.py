##########################################################################
# Password validator:
# Skriv en funktion som tar ett lösenord som inparameter.
# Den ska returnera true eller false beroende på om lösenordet uppfyller
# följande krav:
# minst 8 tecken
# minst en stor bokstav
# minst en liten bokstav
# minst en siffra
###########################################################################

import re

def checkPW(password):
    if len(password)<8: return False
    captials = re.findall(r'[A-Z]', password)
    if len(captials)<1: return False
    lowers = re.findall(r'[a-z]', password)
    if len(lowers)<1: return False
    numbers = re.findall(r'[0-9]', password)
    if len(numbers)<1: return False
    if " " in password: return False
    return True

pw = input("Write your password -> ")
if checkPW(pw): print("success !")
else: print("fail !")