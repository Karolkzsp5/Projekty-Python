inw = ("Litwo, ojczyzno moja! ty jesteś jak zdrowie.\n"
       "Ile cię trzeba cenić, ten tylko się dowie,\n"
       "Kto cię stracił. Dziś piękność twą w całej ozdobie\n"
       "Widzę i opisuję, bo tęsknię po tobie.")

zmieniona_w = inw.replace('w', '{w[n]}')
for i in range(1, inw.count('w')+1):
    zmieniona_w = zmieniona_w.replace('{w[n]}', f'{{w{i}}}', 1)
print(zmieniona_w.format(**{'w'+str(i): f'0x{i:04X}' for i in range(1, inw.count('w')+1)}))
