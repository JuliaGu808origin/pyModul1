class matratt:
    def __init__(self, namn, pris, typ, kalorier, lunch, alacarte):
        self._namn = namn
        self._pris = pris
        self._typ = typ
        self._kalorier = kalorier
        self._lunch = lunch
        self._alacarte = alacarte

    def getLunch(self):
        return self._lunch

    def getAlacarte(self):
        return self._alacarte

    def getNamn(self):
        return self._namn

    def getPris(self):
        return self._pris

    def getTyp(self):
        return self._typ

class menyListing:
    def __init__(self, namn, pris, typ):
        self._namn = namn
        self._pris = pris
        self._typ = typ

    def getNamn(self):
        return self._namn

    def getPris(self):
        return self._pris

    def getTyp(self):
        return self._typ

class meny:
    def __init__(self):
        pass

    def generateMenu(self, matLista):
        menylist=[]
        for each in matLista:
            eachMeny = menyListing(each.getNamn(), each.getPris(), each.getTyp())
            mmenyList.append(eachMeny)
        return menylist

class lunchMeny(meny):
    def __init__(self):
        super().__init__()

    def generateMenu(self, matLista):
        matLista = list(filter(lambda each : each._lunch == True, matLista))
        menylist=[]
        for each in matLista:
            eachMeny = menyListing(each.getNamn(), each.getPris(), each.getTyp())
            menylist.append(eachMeny)
        return menylist

class alacarteMeny(meny):
    def __init__(self):
        super().__init__()

    def generateMenu(self,matLista):
        matLista = list(filter(lambda each : each.getAlacarte() == True, matLista))
        menylist=[]
        for each in matLista:
            eachMeny = menyListing(each.getNamn(), each.getPris()*1.7, each.getTyp())
            menylist.append(eachMeny)
        return menylist

def main():
    m1 = matratt("name1",199, "vage", 100, True, False)
    m2 = matratt("name2", 100, "vegan", 90, True, True)
    m3 = matratt("name3", 299, "kött", 100, False, True)
    m4 = matratt("name4", 399, "nött", 100, True, False)
    
    l1 = lunchMeny()
    meny1 = l1.generateMenu([m1, m2, m3, m4])
    for each in meny1:
        print(f"Meny namn: {each.getNamn()}, Pris: {each.getPris()}, Typ: {each.getTyp()}")
    a1 = alacarteMeny()
    print("-------------------------------------------------")
    meny2 = a1.generateMenu([m1, m2, m3, m4])
    for each in meny2:
        print(f"Meny namn: {each.getNamn()}, Pris: {each.getPris()}, Typ: {each.getTyp()}")

main()