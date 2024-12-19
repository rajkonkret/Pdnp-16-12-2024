# funkcje - wydzielony fragment programu, można go wywołac w dowolnym momencie
# funkcja musi być najpierw zadeklarowana
# w miejscu deklaracji funkcja nic nie robi
# żeby wykonac funkcję należy ją wywołać

a = 6
b = 8


# PEP8 - dwie linijki odstepu
# deklaracja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):  # dwa obowiązkowe argumenty
    print(a + b)  # zmienne lokalne


# symulujemy przeciązanie funkcji różną liczbą argumentów
def odejmij(a, b, c=0):  # argument c ma wartosc domyslna
    print(a - b - c)


dodaj()  # 14
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'

# argumenty po pozycji
dodaj2(5, 7)  # 12
odejmij(1, 2)
odejmij(1, 2, 3)

# argumenty po nazwie
odejmij(b=9, a=8)
odejmij(b=9, a=8, c=90)

# argumenty mieszane
odejmij(1, c=10, b=67)
# odejmij(a=1, c=10, 67) # SyntaxError: positional argument follows keyword argument

print(dodaj())
print(dodaj() + dodaj2(5, 9))
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
