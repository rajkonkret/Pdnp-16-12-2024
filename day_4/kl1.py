# klasa - szablon, przepis
# wskazuje cechy i funkcje
# obiekt (instancja) klasy - według przepis
# definicja klasa nie uruchamia klasy
# aby uruchomic klase musimy stworzyc jej obiekt
# paradygmaty programowania obiektowego
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja

# deklaracje klasy
# PEP8 zaleca do nazw uzywac PascalCase
class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """
    imie = ""
    wiek = None
    plec = "k"


cz1 = Human()
print(cz1)  # <__main__.Human object at 0x000001FEC4221D00>
print(Human.__doc__)  # Klasa Human opisująca człowieka w pythonie
print(print.__doc__)
# cd.\day_4
# pydoc -b server z dokumentacją kodu
# pydoc -w kl1 - plik html z dokumantacją kodu
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
#
# None
# k
cz1.wiek = 34
cz1.imie = "Anna"
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Anna
# 34
# k
cz2 = Human()
cz2.wiek = 43
cz2.imie = "Radek"
cz2.plec = "m"
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
# Radek
# 43
# m
