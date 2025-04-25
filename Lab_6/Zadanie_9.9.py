class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pokaz(self):
        print(f"Punkt znajduje się w ({self.x}, {self.y})")

class Odcinek:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def dlugosc(self):
        return ((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2) ** 0.5

class Trojkat:
    def __init__(self, p1, p2, p3):
        self.a = Odcinek(p1, p2)
        self.b = Odcinek(p2, p3)
        self.c = Odcinek(p3, p1)

    def obwod(self):
        return self.a.dlugosc() + self.b.dlugosc() + self.c.dlugosc()
