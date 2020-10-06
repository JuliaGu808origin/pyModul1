from abc import ABC, abstractmethod
class shape(ABC):
    def __init__(self, width, height):
        self._width=width
        self._height=height

    @abstractmethod
    def area(self):
        pass

class triangle(shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def area(self):
        super().area()
        print(self._width * self._height * 0.5)

class rectangle(shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def area(self):
        super().area()
        print(self._height * self._width)

def main():
    r = rectangle(10, 20)
    t = triangle(10, 20)
    r.area()
    t.area()

main()