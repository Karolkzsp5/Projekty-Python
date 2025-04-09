inw = ("Litwo, ojczyzno moja! ty jesteś jak zdrowie.\n"
       "Ile cię trzeba cenić, ten tylko się dowie,\n"
       "Kto cię stracił. Dziś piękność twą w całej ozdobie\n"
       "Widzę i opisuję, bo tęsknię po tobie.")

with open('inwokacja.txt', 'w', encoding='utf-8') as f:
    f.write(inw)

with open('inwokacja.txt', 'r', encoding='utf-8') as f:
    inw_plik = f.read()