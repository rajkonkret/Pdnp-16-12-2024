dictionary = {"imie": "Radek", 'nazwisko': "kowalski"}
print(type(dictionary))  # <class 'dict'>

# wyswietli klucze
for i in dictionary:
    print(i)

for i in dictionary.keys():
    print(i)
# imie
# nazwisko
# imie
# nazwisko

for v in dictionary.values():
    print(v)
# Radek
# kowalski

for i in dictionary.items():
    print(i)

for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => kowalski
#       sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>kowalski
for k, v in dictionary.items():
    print(k, v, sep="=>", end="<=>")
    # imie=>Radek<=>nazwisko=>kowalski<=>
print("Radek")  # imie=>Radek<=>nazwisko=>kowalski<=>Radek tu ustawi end="\n"
print("Tomek")  # Tomek

pol_ang = {"kot": 'cat', 'pies': "dog", 'dach': 'roof'}
ang_pol = {}
for k, v in pol_ang.items():
    ang_pol[v] = k
print(ang_pol)
# {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}
print({value: key for key, value in pol_ang.items()})
# {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}
