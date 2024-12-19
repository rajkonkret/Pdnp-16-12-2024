# funkcje zwracające wynik
# konczą się instrukcją return

def dodaj(a, b):
    return a + b  # return, zwróć wynik


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(6, 23))  # 29
print(odejmij(1))
print(odejmij())
print(odejmij(1, 2))
print(odejmij(1, 2, 3))
print(odejmij(b=9))

print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
print(oblicz_vat(vat=15, cena=5000))
# 1230.0
# 1080.0
# 5750.0

zm = oblicz_vat(1000)
print(zm)  # 1230.0
print(type(zm))  # <class 'float'>
if zm == 1230:
    print("Brawo")

print(dodaj(6, 89) + odejmij(234, 78))  # 251
