def ceil(n):
    return int(n) + (n % 1 > 0)

def floor(n):
    return int(n) if n >= 0 else int(n) - (n % 1 != 0)

liczby = [1.2, 3.8, -2.1, 5.0, -3.99]
for liczba in liczby:
    print(f"{liczba}: ceil = {ceil(liczba)}, floor = {floor(liczba)}")
