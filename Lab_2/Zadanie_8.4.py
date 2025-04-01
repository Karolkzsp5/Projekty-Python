a = list(range(10))
b = [complex(i, 0) for i in range(10)]
c = [i * 0.1 for i in range(10)]

sklejonaLista = a + b + c

print("Lista sklejona:", sklejonaLista)