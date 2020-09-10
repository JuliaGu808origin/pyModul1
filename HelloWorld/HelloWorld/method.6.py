def MaxVarde2(tal1, tal2):
    if tal1>tal2:
        return tal1
    return tal2

def MaxVarde3(tal1,tal2,tal3):
    tallist=[tal1,tal2,tal3]
    return max(tallist)

def KontrolleraMaxVarde(tal1, tal2, tal3):
    tallist=[tal1,tal2,tal3]
    if 0 in tallist:
        tallist.remove(0)
        print(MaxVarde2(tallist[0], tallist[1]))
    else:
        print(MaxVarde3(tallist[0], tallist[1], tallist[2]))

templist=[]
while True:
    try:
        tal=int(input("Mata in ett heltal -> "))
        templist.append(int(tal))
        if len(templist) == 3:
            KontrolleraMaxVarde(templist[0], templist[1], templist[2])
            break
    except:
        print("Fel tal !")