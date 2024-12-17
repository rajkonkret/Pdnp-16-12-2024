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
