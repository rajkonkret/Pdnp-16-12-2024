# funkcja lambda
# lambda zwraca wynik (return)

def odejmij(a, b):
    return a - b


print(odejmij(234, 87))  # 147

odejmij2 = lambda a, b: a - b
print(odejmij2(345, 76))  # v

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

# mapowanie danych
lista = [1, 2, 3, 10, 20, 50, 70, 200, 300, 500]
lista_wyn = []
for i in lista:
    lista_wyn.append(i * 2)
print(lista_wyn)  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]

# list comprehensions
print([i * 2 for i in lista])  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]


def zmien(x):
    return x * 2


lista_wyn.clear()  # usunięcie danych z listy
for i in lista:
    lista_wyn.append(zmien(i))
print(lista_wyn)  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]

# map() bierze element z kolekcji i wykonuje na nim operacje zadaną funkcją
# funkcje wyższego rzędu
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]

# zastosowanie lambda jako funkcja naonimowa
# wykonanie w mmiejscu deklaracji
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 8, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 20, lista))}")
# Zastosowanie map(): [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]
# Zastosowanie map(): [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]
# Zastosowanie map(): [4, 8, 12, 40, 80, 200, 280, 800, 1200, 2000]
# Zastosowanie map(): [8, 16, 24, 80, 160, 400, 560, 1600, 2400, 4000]
# Zastosowanie map(): [20, 40, 60, 200, 400, 1000, 1400, 4000, 6000, 10000]

# filtrowanie danych
l3 = []
for i in lista:
    if i < 20:
        l3.append(i)
print(l3)  # [1, 2, 3, 10]

# filter() zwraca elementy spęłniające warunek
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 20, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3 and x < 50, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 50, lista))}")
# Zastosowanie filter(): [1, 2, 3, 10]
# Zastosowanie filter(): [10, 20]
# Zastosowanie filter(): [10, 20]
