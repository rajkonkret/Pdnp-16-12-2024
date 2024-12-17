# zbiór (set) - przechowuje unikalne wartości
# nie zacowuje kolejności przy dodawaniu elementów
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

# pusty zbiór
zb2 = set()
print(zb2)  # set()
print(type(zbior))  # <class 'set'>

# dodanie elementu do seta
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(18)
zbior.add(33)
zbior.add(24)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 24}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24}

# pop() - usunięcie pierwszego elementu
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22, 24}
zmienna = zbior.pop()
print("Usunęliśmy element:", zmienna)  # Usunęliśmy element: 66

zbior_copy = zbior.copy()
print(zbior_copy)
print(zbior)  # {777, 11, 44, 18, 22, 24}
print(zbior_copy)  # {18, 22, 24, 777, 11, 44}

print(id(zbior))  # 2926796923040
print(id(zbior_copy))  # 2926796918560

zbior_2 = {667, 11, 44, 18, 52, 62, 999, 999, 12.34}
print(type(zbior_2))  # <class 'set'>
print(zbior_2)  # {999, 11, 44, 12.34, 18, 52, 667, 62}

# suma zbiorów, dostajemy nowy zbiór
print(zbior | zbior_2)  # {999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}
print(zbior.union(zbior_2))  # {999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}

# częśc wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica
print(zbior - zbior_2)  # {24, 777, 22}
print(zbior.difference(zbior_2))  # {24, 777, 22}
print(zbior_2.difference(zbior))  # {999, 12.34, 52, 667, 62}

# łączy zbiory, zmienia zbiór bazowy!!!
zbior.update(zbior_2)
print(zbior)  # {999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}

krotka = tuple(zbior)
print(krotka)  # (999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62)

lista = list(zbior)
print(lista)  # [999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62]

# sprawdzamy czy element istnieje w zbiorze
print(999 in zbior)  # True
print(999 in lista)  # True
print(999 in krotka)  # True
