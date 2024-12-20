from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # oznaczenie metody abstrakcyjnej
    def wydaj_odglos(self):
        pass


class Kura(Ptak):

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Ko ko ko ko ko ")

    def dziobanie(self):
        print("Ide podziobać")


class Orzel(Ptak):
    """
    Klasa dziiedziczy z Ptak
    """

    def wydaj_odglos(self):
        print("Kir kier kir")

    def polowanie(self):
        print("Polowanie")


# po oznaczeniu klasy jako abstrakcyjna
#  TypeError: Can't instantiate abstract class
#  Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzeł", 45)
# or1.latam()  # Tu Orzeł Lecę z szybkością 45
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0

kur2 = Kura("Kura")
kur2.latam()  # Tu Kura Ja nie latam

or2 = Orzel("Orzeł Bielik", 50)
or2.latam()  # Tu Orzeł Bielik Lecę z szybkością 50
kur2.wydaj_odglos()
or2.wydaj_odglos()
# Ko ko ko ko ko
# Kir kier kir
kur2.dziobanie()
or2.polowanie()
# Ide podziobać
# Polowanie
lista = [kur2, or2]
for i in lista:
    i.wydaj_odglos()
# polimorfizm. obiekty róznych klas dzięki dziedziczeniu i klasie abstrakcyjnej mogą byc uznane za tożsame
