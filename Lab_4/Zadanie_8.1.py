def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    if b == 0:
        print("Nie można dzielić przez 0")
        return None
    return a / b

def main():
    a = 10
    b = 5

    print(dodaj(a, b))
    print(odejmij(a, b))
    print(pomnoz(a, b))

    wynik = podziel(a, b)
    if wynik is not None:
        print(wynik)

if __name__ == "__main__":
    main()
