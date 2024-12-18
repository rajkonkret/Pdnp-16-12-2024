# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if
# w zależności od warunku wykona jeden lub drugi blok programu
# warunek musi zwracac bool

odp = True
print(bool(odp))  # True
# odp = False
if odp:
    # blok kodu wgdy warunek True
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza część programu")

odp = "Radek"
print(bool(odp))

if odp:
    print("Dane zostały odebrane")

if odp == "Radek":  # == porównanie
    print("Nadal Radek")  # Nadal Radek

odp = 0
if odp:
    print("Działa")
else:  # w przeciwnym przypadku
    print("zero - False")  # zero - False

a = "Radek"
if len(a) > 3:
    print(f'Długość wynosi więcej niż 3, {len(a)}')
    # Długość wynosi więcej niż 3, 5

a = "Radek"
n = len(a)
if n > 3:
    print(f"Długosć wynosi więcej niz 3, {n}")
    # Długość wynosi więcej niz 3, 5

# operator morsa, walrus operator
if (n := len(a)) > 3:
    print(f"Długość wynosi więcej niz 3, {n}")
# Długość wynosi więcej niz 3, 5


# kolejnosc ma znaczenie
# podatek = 0
# zarobki = int(input("Podaj zarobki"))
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 30_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi {podatek * zarobki}")

sum_zam = 150
if sum_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

rabat = 25 if sum_zam > 100 else 0
print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

# zasymulejemy system zbierania logów
# system jaki wysłął logi - musimy zmienną
# email, console, inny
# gdy sytem cosole wyswietlamy napis "Stało się coś strasznego"
# email -> "System email"
# jesli system jest email to do listy błedów wpisac opis błedu
# error, medium, inny
lista_b = []
error = "medium"
alert_system = "email"

if alert_system == 'console':
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("System email")
    if error == "error":
        lista_b.append("Krytyczny")
    elif error == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("inny")
else:
    print("Inny system")

print(lista_b)  # ['Krytyczny']
# System email
# ['Ostrzeżenie']
print(f"{alert_system}: error: {lista_b}")  # email: error: ['Ostrzeżenie']

# napisac test z...
# zadac pytanie
# pobrac odpowiedz
# sprawdzic czy własciwa i wypisac wynik
punkty = 0
odp = input("Podaj rok Chrztu Polski")  # str
if odp == "966":
    print("Brawo")
    punkty += 1  # punkty = punkty + 1
else:
    print("Masz w ksiązce na 28 stronie")
print(punkty)
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
