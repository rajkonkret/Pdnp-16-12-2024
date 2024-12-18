# słownik - para klucz wartosc
# {'user' : "Radek", "wiek":76}
# odpowiednik jsona
# klucze nie mogą sie powtarzać

# pusty słownik
dictionary = dict()
print(type(dictionary))  # <class 'dict'>
print(dictionary)  # {}

dictionary_1 = {}
print(type(dictionary_1))  # <class 'dict'>
print(dictionary_1)  # {}

# dodanie elementu do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary["wiek"] = 39

print(dictionary)  # {'imie': 'Radek', 'wiek': 39}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 39])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 39)])

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 39}

# wypisanie wartości dla klucza
print(dictionary['imie'])  # Tomek

# print(dictionary["Imie"]) # KeyError: 'Imie', brak klucza
print(dictionary.get("Imie"))  # nie ma klucza, zwraca None
print(dictionary.get("Imie", "default"))  # nie ma klucza, zwraca default

dictionary.update({'data': '30-12-2024'})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 39, 'data': '30-12-2024'}

dict_small = {'x': 2}
print(dict_small)  # {'x': 2}
dict_small.update([('y', 3), ("z", 5)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 5}

# input() - pozwala wprowadzic dane do komputera
# tekst = input('Podaj imię') # zwraca str
# print(tekst)
# Podaj imięRadek
# Radek
# napisac aplikacje kalkulator
#

# a = int(input("Podaj pierwszą liczbę"))
# b = input("Podaj drugą liczbę")
# print(f"Wynik działania {a} + {b} = {a + float(b)}")  # Wynik działania 5 + 6 = 11.0

# napisac aplikacje słownik pol_ang

pol_ang = {"kot": 'cat', 'pies': "dog", 'dach': 'roof'}
print("znam takie słowka", pol_ang.keys())
odp = input("podaj słówko do przetłumaczenia")
# print(pol_ang[odp.strip().lower()])
# print(pol_ang[odp.strip().casefold()])

print(pol_ang.get(odp.strip().casefold()))
print(pol_ang.get(odp.strip().casefold(), "nie mo"))
