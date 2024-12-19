# stworzyć funkcje obliczjącą średnią
def liczby(name=None, *cyfry):  # dowolna liczba argumentów pozycyjnych
    print(cyfry)
    count = len(cyfry)
    suma = 0
    suma_p = sum(cyfry)
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
    except Exception as e:
        print("Błąd", e)
    else:  # wykona się gdy nie ma błedu
        print(f"Średnia dla ucznia {name} wynosi {avg}")
    finally:
        print("Obliczenia zakończone")


liczby()
liczby(1)
liczby(1, 2, 3, 4)
liczby("Radek", 2, 3, 4)
# ()
# (1,)
# (1, 2, 3, 4)
# ()
# Błąd division by zero
# (1,)
# Średnia wynosi 1.0
# (1, 2, 3, 4)
# Średnia wynosi 2.5
# ()
# Błąd division by zero
# Obliczenia zakończone
# ()
# Błąd division by zero
# Obliczenia zakończone
# (2, 3, 4)
# Średnia dla ucznia 1 wynosi 3.0
# Obliczenia zakończone
# (2, 3, 4)
# Średnia dla ucznia Radek wynosi 3.0
# Obliczenia zakończone
