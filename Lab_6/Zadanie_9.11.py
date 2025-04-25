class Osoba:
    def __init__(self, identyfikator, wiek):
        self._id = identyfikator
        self.__wiek = wiek

o = Osoba(123, 25)
print(dir(o))
