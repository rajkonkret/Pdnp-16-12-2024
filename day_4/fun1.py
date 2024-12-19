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


dodaj()  # 14
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(5, 7) # 12
