inw = ("Litwo, ojczyzno moja! ty jesteś jak zdrowie.\n"
       "Ile cię trzeba cenić, ten tylko się dowie,\n"
       "Kto cię stracił. Dziś piękność twą w całej ozdobie\n"
       "Widzę i opisuję, bo tęsknię po tobie.")

alfabet = 'abcdefghijklmnoprstuwxyz'
zmieniana_litera = inw.replace('a', '{}')
print(zmieniana_litera.format(*alfabet))