class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print("Nazywam się", self.imie)

    # wypisz_wzrost, wypisz_wiek
    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu")

    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


# cz1 = Human() # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Radek", 56, 190, "m")
print(cz1)  # <__main__.Human object at 0x0000016AE53499D0>
print(cz1.imie)  # Radek
cz1.powitanie()  # Nazywam się Radek
cz1.wypisz_wiek()
cz1.wypisz_wzrost()
# Nazywam się Radek
# Mam 56 lat
# Mam 190 cm wzrostu

cz2 = Human("Ania", 56, 167)
cz2.powitanie()  # Nazywam się Radek
cz2.wypisz_wiek()
cz2.wypisz_wzrost()
# Nazywam się Ania
# Mam 56 lat
# Mam 167 cm wzrostu
cz1.ruszaj()
cz2.ruszaj()
# Ruszyłem w drogę
# Ruszyłam w drogę
