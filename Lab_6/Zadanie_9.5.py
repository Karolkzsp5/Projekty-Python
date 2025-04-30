def dodaj(a, b): return a + b
def odejmij(a, b): return a - b
def mnoz(a, b): return a * b
def dziel(a, b): return a / b

x = dodaj(dziel(dodaj(4, mnoz(2, odejmij(5, 10))),odejmij(mnoz(32, 11), 4)),2)
print("Wynik:", x)