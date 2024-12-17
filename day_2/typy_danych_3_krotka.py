# krotka(tupla) - kolekcja niemutowalna, tylko do odczytu
# pozwala efektywniej zarządzac pamięcią
# krotka jedoelementowa - zastępstwo stałych, zmienna

tupla = ("Radek")
print(type(tupla))  # <class 'str'>

tupla_2 = "Radek",
print(type(tupla_2))
print(tupla_2)  # ('Radek',)

# PEP8 zaleca tworzyc tuple jednoelementowe z ()
tupla_3 = ("Radek",)
print(tupla_3)  # ('Radek',)

tupla_liczby = 43, 55, 22.34, 11, 200
print(type(tupla_liczby))
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

# tupla jest niemutowalna
# tupla_liczby[3] = 123  # TypeError: 'tuple' object does not support item assignment

del tupla_liczby
# print(tupla_liczby) # NameError: name 'tupla_liczby' is not defined

tupla_imiona = "Radek", 'Tomek', "Zenek", "Ania", 'Eliza', "Marek"
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Ania', 'Eliza', 'Marek')
print(type(tupla_imiona))  # <class 'tuple'>

print(tupla_imiona.index("Radek"))  # na indeksie 0
print(tupla_imiona.count("Eliza"))  # występuje jeden raz

# rozpakowanie tupli
tup = 1, 2
print(type(tup))  # <class 'tuple'>
a, b = 1, 2
a, b = tup
print(a, b)  # 1 2

tup_2 = 1, 2, 3
a, *b = tup_2
print(a, b)  # 1 [2, 3]

name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)  # Radek Tomek ['Zenek', 'Ania', 'Eliza', 'Marek']

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)  # Radek ['Tomek', 'Zenek', 'Ania', 'Eliza'] Marek

*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)  # ['Radek', 'Tomek', 'Zenek', 'Ania'] Eliza Marek

# sortowanie krotki, zwraca nową listę
print(sorted(tupla_imiona))  # ['Ania', 'Eliza', 'Marek', 'Radek', 'Tomek', 'Zenek']
print(tupla_imiona)  # tupla się nie zmienia
