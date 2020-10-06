from datetime import datetime

class Bokning:
    def __init__(self, starttid, sluttid, kund, sporthall):
        self._starttid = starttid
        self._sluttid = sluttid
        self._kund = kund
        self._sporthall = sporthall

    def getHall(self):
        return self._sporthall

    def getDates(self):
        start = datetime.strptime(self._starttid,"%Y-%m-%d %H:%M")
        slut = datetime.strptime(self._sluttid,"%Y-%m-%d %H:%M")
        return [start, slut]

    def __str__(self):
        return f"{self._starttid} -- {self._sluttid} -> {self._sporthall}"

    def writeTaken(self):
        return f"{self._starttid} -- {self._sluttid} -> {self._sporthall.getTyp()} taken "
