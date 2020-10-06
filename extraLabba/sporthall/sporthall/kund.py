class Kund:
    def __init__(self, namn, telefonnummer, email, postnummer, gatuadress):
        self._namn = namn
        self._telefonnummer = telefonnummer
        self._email = email
        self._postnummer = postnummer
        self._gatuadress = gatuadress
        self._boknings =[]

    def getTelefonnummer(self):
        return self._telefonnummer

    def addBokning(self, bokning):
        self._boknings.append(bokning)

    def getBokning(self):
        return self._boknings
