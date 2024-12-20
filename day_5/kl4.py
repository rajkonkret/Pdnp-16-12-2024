class Car:
    """
    Klasa opisująca samochód
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        # pole prywatne, hermetyzacja
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10  # predkosc = predkosc = 10

    def licznik(self):
        print(f"Jadę z szybkoscią {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    def __zmien_bieg(self):
        print("Zmien bieg")


sam = Car("Skoda tdi", "2024")
sam.gaz()
sam.gaz()
sam.gaz()
sam.gaz()
sam.gaz()
# Po ustawieniu pola jako prywatne
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(sam.__predkosc)  # 50 nie da się odczytac wartości
sam.licznik()  # Jadę z szybkoscią 50 km/h
sam.hamuj()
sam.hamuj()
sam.hamuj()
sam.hamuj()
sam.hamuj()
sam.licznik()
# Jadę z szybkoscią 50 km/h
# Jadę z szybkoscią 0 km/h
sam.gaz()
sam.licznik()  # Jadę z szybkoscią 10 km/h
sam.__predkosc = 0
sam.licznik()  # Jadę z szybkoscią 10 km/h
# Jadę z szybkoscią 50 km/h
# Jadę z szybkoscią 0 km/h
# Jadę z szybkoscią 10 km/h
# Jadę z szybkoscią 50 km/h
# Zmien bieg
# Zmien bieg
# Zmien bieg
# Zmien bieg
# Zmien bieg
# Jadę z szybkoscią 0 km/h
# Jadę z szybkoscią 10 km/h
# Jadę z szybkoscią 10 km/h
# hermetyzacja - pola prywatne
# enkapsulacja - hermetyzownie pól i wystawianie metod do ich odczytu i zapisu
