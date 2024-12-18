# pętle - możliwośc wykonaia kodu wielokrotnie
# for - pętla iteracyjna
import random
from itertools import zip_longest

for i in range(5):  # 0 do 4 - pięć razy
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(20):  # nie ma zmienna
    print("Test podłoga")
    # print(_)

for i in range(5):
    print(i * 2)
    print(i + 2)

# przerobic lotto na petle
# wylosowane liczby umiescic w liscie
lista_kule = list(range(1, 50))
lista_wyn = []
for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    lista_wyn.append(wyn)

print(lista_wyn)  # [41, 44, 14, 11, 3, 5]

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

lista3 = []
for j in range(10):
    if j % 2 == 0:
        lista3.append(j)
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista_wyn:
    if c > 10:
        print("Większy niż 10", c)
    else:
        print('Mniejsze, równe 10', c)
# Większy niż 10 11
# Mniejsze, równe 10 3
# Większy niż 10 38
# Większy niż 10 26
# Większy niż 10 42

for i in range(0, 10, 2):  # (start, stop, krok)
    print(i)

for i in range(-10, 0):
    print(i)

for i in range(10, 0, -2):  # pętla w dół, do tyłu
    print(i)

for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
        print(c)
    print("Przy każdym przejściu pętli", c)
# Przy każdym przejściu pętli 0
# 3
# Przy każdym przejściu pętli 3
# Przy każdym przejściu pętli 4
# Przy każdym przejściu pętli 6
# Przy każdym przejściu pętli 8

imiona = ["Radek", 'Tomek', "Zenek", "Ania"]
print(imiona)
print(type(imiona))
# ['Radek', 'Tomek', 'Zenek', 'Ania']
# <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Ania

# 0 Radek

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for i in range(len(imiona)):  # range(4) -> 0123
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate() - numeruje kolekcje i zwraca numer i element
for p in enumerate(imiona):
    print(p)
(0, 'Radek')
(1, 'Tomek')
(2, 'Zenek')
(3, 'Ania')

for i, p in enumerate(imiona):
    print(i, p)

# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania
for i, p in enumerate(imiona, start=1):
    print(i, p)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

imiona = ["Radek", 'Tomek', "Zenek", "Ania", "Ewa"]
wiek = [44, 55, 32, 27]
# Radek 44
# for p in imiona:
#     print(p, wiek[imiona.index(p)])
# Radek 44
# Tomek 55
# Zenek 32
# Ania 27

# Po dodaniu elementu do listy imiona
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\Pdnp-16-12-2024\day_3\petle_zad1.py", line 133, in <module>
#     print(p, wiek[imiona.index(p)])
#              ~~~~^^^^^^^^^^^^^^^^^
# IndexError: list index out of range

# zip() - łączy kolekcje
for i in zip(imiona, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Ania', 27)
for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 44
# Tomek 55
# Zenek 32
# Ania 27

# 0 Radek 44
for i in enumerate(zip(imiona, wiek)):
    print(i)
(0, ('Radek', 44))
(1, ('Tomek', 55))
(2, ('Zenek', 32))
(3, ('Ania', 27))
a, b = (0, ('Radek', 44))
print(a, b)  # 0 ('Radek', 44)
c, d = b
print(c, d)
print(a, c, d)  # 0 Radek 44
a, (c, d) = (3, ('Ania', 27))
for i, (p, w) in enumerate(zip(imiona, wiek)):
    print(i, p, w)
# 0 Radek 44
# 1 Tomek 55
# 2 Zenek 32
# 3 Ania 27

zip_list = zip_longest(imiona, wiek, fillvalue=None)
print(zip_list)  # <itertools.zip_longest object at 0x0000014636A29210>
print("------")
for i in zip_list:
    print(i)
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Ania', 27)
# ('Ewa', None)
print("-----")
for i in zip_list:
    print(i)
# mozemy wykorzystac raz
zip_list = zip_longest(imiona, wiek, fillvalue=None)
zipped = list(zip_list)
for i in zipped:
    print(i)
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Ania', 27)
# ('Ewa', None)
for o, w in zipped:
    print(o, w)
# Radek 44
# Tomek 55
# Zenek 32
# Ania 27
# Ewa None
