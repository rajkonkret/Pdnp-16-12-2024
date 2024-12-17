# kolekcje

# lista - przechowuje dowolną ilosć danych, róznego typu na raz
# zachowuje kolejnosc przy dodawaniu danych

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(type(pusta_lista))  # <class 'list'>
print(pusta_lista)  # []

# append() - dodawanie elementów do listy
lista.append("Radek")
lista.append("Zenek")
lista.append("Tomek")
lista.append("Michał")
lista.append("Marek")
lista.append("Arek")
lista.append("Bogdan")
print(lista)
# ['Radek', 'Zenek', 'Tomek', 'Michał', 'Marek', 'Arek', 'Bogdan']
#     0         1       2         3        4        5        6
#     -7        -6      -5        -4       -3       -2       -1
print(len(lista))  # 7
print(lista[0])  # Radek
print(lista[3])  # Michał
print(lista[5])  # Arek

# print(lista[10])  # IndexError: list index out of range

print(lista[6])
print(lista[len(lista) - 1])  # Bogdan
print(lista[-1])  # Bogdan
print(lista[-2])  # Arek
print(lista[-5])  # Tomek

# wyświetlenie fragmentu listy (slicowanie)
print(lista[0:3])  # ['Radek', 'Zenek', 'Tomek'] 012
print(lista[:3])  # ['Radek', 'Zenek', 'Tomek'] indeksy 012
print(lista[2:])  # ['Tomek', 'Michał', 'Marek', 'Arek', 'Bogdan']
print(lista[2:6])  # ['Tomek', 'Michał', 'Marek', 'Arek']

print(lista[2:15])  # ['Tomek', 'Michał', 'Marek', 'Arek', 'Bogdan']
print(lista[:])  # ['Radek', 'Zenek', 'Tomek', 'Michał', 'Marek', 'Arek', 'Bogdan']
print(lista[2:2])  # []
print(lista[2:3])
print(lista[10:29])  # []

# ['Radek', 'Zenek', 'Tomek', 'Michał', 'Marek', 'Arek', 'Bogdan']
#     0         1       2         3        4        5        6
#     -7        -6      -5        -4       -3       -2       -1

print(lista[-2:0])  # [] -> [5:0]
print(lista[0:-2])  # -> [0:5] ['Radek', 'Zenek', 'Tomek', 'Michał', 'Marek']

lista_15 = list(range(15))  # 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[0:15:2])  # [start:stop:krok] [0, 2, 4, 6, 8, 10, 12, 14]
print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14]
print(lista[::2])  # ['Radek', 'Tomek', 'Marek', 'Bogdan']

print(lista[::-1])  # krok w tył
# ['Bogdan', 'Arek', 'Marek', 'Michał', 'Tomek', 'Zenek', 'Radek']

# nadpisanie elementu w liście na indeksie
# zmienia bazową listę
lista[3] = "Asia"
print(lista)  # ['Radek', 'Zenek', 'Tomek', 'Asia', 'Marek', 'Arek', 'Bogdan']

# insert() - dopisanie elementu we wskazanym indeksie
lista.insert(1, "Krzysztof")
print(lista)  # ['Radek', 'Krzysztof', 'Zenek', 'Tomek', 'Asia', 'Marek', 'Arek', 'Bogdan']

lista.insert(15, "Żaklina")
print(lista)
# ['Radek', 'Krzysztof', 'Zenek', 'Tomek', 'Asia', 'Marek', 'Arek', 'Bogdan', 'Żaklina']

# sprawdzenie indeksu dla elementu, pierwszy napotkany
print(lista.index("Asia"))  # 4
lista.append("Asia")  # dodaje na końcu
print(lista)
# ['Radek', 'Krzysztof', 'Zenek', 'Tomek', 'Asia', 'Marek', 'Arek', 'Bogdan', 'Żaklina', 'Asia']
print(lista.index("Asia"))  # indeks 4, pierwszy napotkany

# usunięcie po elemencie, pierwszy napotkany
lista.remove("Asia")
print(lista)
# ['Radek', 'Krzysztof', 'Zenek', 'Tomek', 'Marek', 'Arek', 'Bogdan', 'Żaklina', 'Asia']

# usunięcie po indeksie pop()
lista.pop(5)
print(lista)
# ['Radek', 'Krzysztof', 'Zenek', 'Tomek', 'Marek', 'Bogdan', 'Żaklina', 'Asia']
print(lista.pop(5))  # Bogdan
print(lista.pop(-3))  # Marek
print(lista.pop())  # Asia, usnie ostatni element z listy
