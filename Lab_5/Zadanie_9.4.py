inw = ("Litwo, ojczyzno moja! ty jesteś jak zdrowie.\n"
       "Ile cię trzeba cenić, ten tylko się dowie,\n"
       "Kto cię stracił. Dziś piękność twą w całej ozdobie\n"
       "Widzę i opisuję, bo tęsknię po tobie.")

linie = inw.split('\n')

print("Małe litery:", inw.lower() + "\n")
print("Wielkie litery:", inw.upper() + "\n")
print("Każdy wers z wielkiej litery:", "\n".join([linia.capitalize() for linia in linie]) + "\n")
print("Co drugi wers:", "\n".join([linie[i].upper() if i % 2 == 0 else linie[i].lower() for i in range(len(linie))]) + "\n")
print("Co druga litera:", "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(inw)]) + "\n")
print("Co druga litera (pominięcie):", inw[::2] + "\n")
print("Odwrócona kolejność:", inw[::-1])