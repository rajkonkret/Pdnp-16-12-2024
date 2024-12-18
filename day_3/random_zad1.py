import random

# biblioteka do działań na liczbach losowych

print(random.randint(1, 100))  # int od 1 do 100
print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(5))  # od 0 do 4
print(random.random())  # float 0.13387947758622987 od 0 do 0.9999999
print(random.random() * 8)  # float 1.9865305551958636 od 0 do 7.9999999

lista = [67, 45, 32, 68, 89, 90, 42]
print(random.choice(lista))  # wylosuje element z listy,67

lista_kule = list(range(1, 50))  # od 1 do 49
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)

print(random.choices(lista_kule, k=6))  # [5, 30, 42, 42, 46, 44] z powtórzeniami
print(random.sample(lista_kule, k=6))  # [31, 25, 47, 17, 49, 11]
print(random.sample(lista_kule, 6))  # [42, 1, 33, 17, 7, 16]
