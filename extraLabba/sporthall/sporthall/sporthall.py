class SportHall:
    def __init__(self, typ):
        self._typ = typ

    def __str__(self):
        return f"{self._typ.name}"

    def getTyp(self):
        return f"{self._typ.name}"
