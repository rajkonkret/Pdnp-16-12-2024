import csv

fields = []
rows = []

# filename = 'records.csv'
filename = 'records_discount.csv'

with open(filename, "r") as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    print(dialect.delimiter)
    f.seek(0)  # ustawiamy odczyt na początek pliku
    csvreader = csv.reader(f, delimiter=dialect.delimiter)
    # csvreader = csv.reader(f, delimiter=";")
    print(csvreader)

    fields = next(csvreader)  # wczyta pierwszy element i ustawi na następny
    for i in csvreader:
        # print(i)
        rows.append(i)
        # ['name', 'branch', 'year', 'cgpa']
        # ['Radek', 'Coe', '2', '9.1']

print("Fields:", fields)
print("Rows:", rows)
# Fields: ['name', 'branch', 'year', 'cgpa']
# Rows: [['Radek', 'Coe', '2', '9.1']]
# Fields: ['sku', 'exp_date', 'price']
# Rows: [['1', 'today', '100'], ['2', 'today', '200'],
#        ['3', 'tomorrow', '500'], ['4', 'today', '200.0'], ['5', 'tomorrow', '99.99']]
