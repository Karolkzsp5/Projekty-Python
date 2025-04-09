nazwa_pliku = input("Podaj nazwę pliku: ")
try:
    with open(nazwa_pliku, 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print("Plik nie istnieje!")
except Exception as e:
    print(f"Wystąpił błąd: {type(e).__name__}")