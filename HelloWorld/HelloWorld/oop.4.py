class FordonsAnnons:
    def __init__(self, pris, rubrik, beskrivning, arsmodell, antalmil):
        self._pris = pris
        self._rubrik = rubrik
        self._beskrivning = beskrivning
        self._arsmodell = arsmodell
        self._antalmil = antalmil

    def getAnnonsText(self):
        return f"""
                En grym {self._rubrik} 
                Årsmodell {self._arsmodell}, {self._antalmil} mil
                {self._pris} kr
                {self._beskrivning}
                """

class BilAnnons(FordonsAnnons):
    def __init__(self, pris, rubrik, beskrivning, arsmodell, antalmil, color, sommardack, vinterdack):
        super().__init__(pris, rubrik, beskrivning, arsmodell, antalmil)
        self._color = color
        self._sommardack = sommardack
        self._vinterdack = vinterdack

    def getAnnonsText(self):
        return f"""
                En grym {self._rubrik} 
                Årsmodell {self._arsmodell}, {self._color}, {self._antalmil} mil
                {self._pris} kr
                Sommar däck: {self._sommardack}
                Vinter däck: {self._vinterdack}
                {self._beskrivning}
                """

class HusvagnsAnnons(FordonsAnnons):
    def __init__(self, pris, rubrik, beskrivning, arsmodell, antalmil, 
                 color, sommardack, vinterdack, dusch, antalbaddar):
        super().__init__(pris, rubrik, beskrivning, arsmodell, antalmil)
        self._color = color
        self._sommardack = sommardack
        self._vinterdack = vinterdack
        self._dusch = dusch
        self._antalbaddar = antalbaddar

    def getAnnonsText(self):
        return f"""
                En grym {self._rubrik} 
                Årsmodell {self._arsmodell}, {self._color}, {self._antalmil} mil
                {self._pris} kr
                Sommar däck: {self._sommardack}
                Vinter däck: {self._vinterdack}
                Dusch: {self._dusch}
                antal bäddar: {self._antalbaddar}
                {self._beskrivning}
                """

from enum import Enum
class Drivtyp(Enum):
    kardan = 1
    kedja = 2

class MotorCykelAnnons(FordonsAnnons):
    def __init__(self, pris, rubrik, beskrivning, arsmodell, antalmil, motorvolym, drivtyp):
        super().__init__(pris, rubrik, beskrivning, arsmodell, antalmil)
        self._motorvolym = motorvolym
        self._drivtyp = drivtyp

    def getAnnonsText(self):
        return f"""
                En grym {self._rubrik} 
                Årsmodell {self._arsmodell}, {self._antalmil} mil
                {self._pris} kr
                Motor volym: {self._motorvolym} CM3
                driv typ: {self._drivtyp.name}
                {self._beskrivning}
                """

def main():
    b1 = BilAnnons(33333, "Volvo 240", "En perfekt bil för den händige till ett fantastiskt pris.", 
                   "1981", 49000, "Red", True, False )
    h1 = HusvagnsAnnons(44444, "BMW 350", "En perfekt husvagn för den händige till ett fantastiskt pris.", 
                        "1995", 13000, "Black", False, True, True, 3)
    m1 = MotorCykelAnnons(22222, "Reno 404", "En perfekt motor cykel för den händige till ett fantastiskt pris.", 
                          "2000", 3000, 800, Drivtyp.kardan)

    for each in [b1, h1, m1]:
        print(each.getAnnonsText())

main()