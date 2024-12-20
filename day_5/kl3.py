class Pojazd:
    """
    Klasa Pojazd
    """

    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print("Kolor", self.kolor)


class Samochod(Pojazd):
    """
    Klasa Samochód, dziedziczy po klasie pojazd
    """

    def __init__(self, kolor, marka):
        super().__init__(kolor)  # musimy wywołac konstruktor klasy wyzszej
        self.marka = marka

    def info(self):
        super().info()  # mozemy wywłać metode z klasy wyzszej
        print("Marka:", self.marka)


poj = Pojazd("czerwony")
poj.info()  # Kolor czerwony

sam = Samochod("biały służbowy", "Skoda")
sam.info()
# Kolor biały służbowy
# Marka: Skoda
