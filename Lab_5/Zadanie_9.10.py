szablon = """Witaj {imie} {nazwisko},
Twoje zamówienie:
- {produkt1}, szt {ilosc1}, cena {cena1:.2f}zł, razem {suma1:.2f}zł
- {produkt2}, szt {ilosc2}, cena {cena2:.2f}zł, razem {suma2:.2f}zł
SUMA: {total:.2f}zł

Pozdrawiamy,
Zespół {sklep}"""

print(szablon.format(
    imie="Jan", nazwisko="Kowalski",
    produkt1="książka", ilosc1=1, cena1=199.99, suma1=199.99,
    produkt2="zeszyt", ilosc2=2, cena2=7.89, suma2=15.78,
    total=215.77, sklep="TwojFantastycznySklep"
))