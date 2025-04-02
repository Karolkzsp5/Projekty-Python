n = 3

def dodaj(a, b):
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    return c

def odejmij(a, b):
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] - b[i][j]
    return c

def pomnoz(a, b):
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c

def main():
    a = [[2] * n for _ in range(n)]
    b = [[3] * n for _ in range(n)]

    print("Dodawanie:")
    for row in dodaj(a, b):
        print(row)

    print("Odejmowanie:")
    for row in odejmij(a, b):
        print(row)

    print("Mnożenie:")
    for row in pomnoz(a, b):
        print(row)

if __name__ == "__main__":
    main()
