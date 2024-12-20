# pliki csv dane oddzielone znakiem podziału
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce
import csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ["Radek", 'Coe', 2, '9.1']

dictionary = dict(zip(fields, row))
print(dictionary)  # {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'}

# newline="" ominięcie problemu pustej linii
filename = 'records.csv'
with open(filename, "w", newline="") as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

filename = 'records_dict.csv'
with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerow(dictionary)

products = [
    {"sku": 1, 'exp_date': "today", "price": 100},
    {"sku": 2, 'exp_date': "today", "price": 200},
    {"sku": 3, 'exp_date': "tomorrow", "price": 500},
    {"sku": 4, 'exp_date': "today", "price": 200.00},
    {"sku": 5, 'exp_date': "tomorrow", "price": 99.99},
]

filename = 'records_discount.csv'
fields_discount = [i for i in products[0]]
print(fields_discount)  # ['sku', 'exp_date', 'price']
with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields_discount)
    csvwriter.writeheader()
    csvwriter.writerows(products)
