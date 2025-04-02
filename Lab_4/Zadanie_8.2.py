lista1 = [1,2,3,4]
lista2 = [5,6,7,8]

def dodaj(lista1, lista2):
    return [(lista1[x]) + (lista2[x]) for x in range(len(lista1))]

def odejmij(lista1, lista2):
    return [(lista1[x]) - (lista2[x]) for x in range(len(lista1))]

def pomnoz(lista1, lista2):
    return [(lista1[x]) * (lista2[x]) for x in range(len(lista1))]

print(dodaj(lista1, lista2))
print(odejmij(lista1, lista2))
print(pomnoz(lista1, lista2))