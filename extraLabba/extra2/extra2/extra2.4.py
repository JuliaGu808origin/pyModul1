###################################################################################
# Skapa lite klasser för ett spel:
# En basklass som heter GameObject (x och y -koordinater)
# Denna ska inte gå att instansiera.
# Den ska ha en metod Draw som alla subclasser måste implementera.
# Skapa Rocket som ärver från GameObject.
# Skapa också en enemyklass som ärver från GameObject.
# Skapa upp några objekt, lägg i en lista och loopa igenom och "rita ut"
# på skärmen (dvs kör Draw)
# ？？具體怎麽做
###################################################################################

from abc import ABC
import matplotlib.pyplot as plt

class GameObject(ABC):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def draw(self):
        pass

class Rocket(GameObject):
    def __init__(self, x, y):
        super().__init__(x,y)

    def draw(self):
        return [self._x, self._y, 'go-']
        #plt.plot(self._x, self._y, 'go')
        #plt.ylabel("Y")
        #plt.xlabel("X")
        #plt.title("Plotting Example")
        #plt.show()

class Enemy(GameObject):
    def __init__(self, x, y):
        super().__init__(x,y)

    def draw(self):
        return [self._x, self._y, 'rs-']
        #plt.plot(self._x, self._y, 'rs')
        #plt.ylabel("Y")
        #plt.xlabel("X")
        #plt.title("Plotting Example")
        #plt.show()

r = Rocket([1, 2, 3], [5, 7, 6])
[rx, ry, rd] = r.draw()
e = Enemy([5, 7, 3], [1, 2, 6])
[ex, ey, ed] = e.draw()
plt.plot(rx, ry, rd, ex, ey, ed)
plt.ylabel("Y")
plt.xlabel("X")
plt.title("Plotting Example")
plt.show()
