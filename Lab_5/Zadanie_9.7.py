inw = ("Litwo, ojczyzno moja! ty jesteś jak zdrowie.\n"
       "Ile cię trzeba cenić, ten tylko się dowie,\n"
       "Kto cię stracił. Dziś piękność twą w całej ozdobie\n"
       "Widzę i opisuję, bo tęsknię po tobie.")

wyrazy = inw.split()
for i, wyraz in enumerate(wyrazy):
    with open(f'wyraz_{i}.txt', 'w', encoding='utf-8') as f:
        f.write(wyraz)