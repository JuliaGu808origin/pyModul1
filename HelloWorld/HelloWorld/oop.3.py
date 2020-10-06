class kattDjur:
    def __init__(self, artNamn, color):
        self._artNamn = artNamn
        self._color = color

    def makeSound(self):
        if self._artNamn=="mimi": return "mimi"
        if self._artNamn=="miao": return "miao"
        return self._artNamn

class husKatt(kattDjur):
    def __init__(self, artNamn, color):
        super().__init__(artNamn, color)

class tiger(kattDjur):
    def __init__(self, artNamn, color):
        super().__init__(artNamn, color)

def main():
    h1 = husKatt("huskatt1", "red")
    h2 = husKatt("mimi", "white")
    t1 = tiger("Tiger1", "black")
    t2 = tiger("miao", "blue")
    for each in [h1, h2, t1, t2]:
        print(each.makeSound())

main()