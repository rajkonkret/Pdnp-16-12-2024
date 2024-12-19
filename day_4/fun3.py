a = 10
b = 10


def dodaj():
    a = 8  # zmienne lokalne
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a  # użyj wewnątrz funkcji globalnego a
    a = 7  # a globalne
    b = 34
    print(a + b)


print(f'Zmienna a globalna (z góry) {a=}')  # Zmienna a globalna (z góry) a=10
dodaj()  # 16
print(f'Zmienna a globalna (z góry) {a=}')  # Zmienna a globalna (z góry) a=10
dodaj2()  # 20
print(f'Zmienna a globalna (z góry) {a=}')  # Zmienna a globalna (z góry) a=10
dodaj3()  # 41
print(f'Zmienna a globalna (z góry) {a=}')  # Zmienna a globalna (z góry) a=7
dodaj2()  # 17
