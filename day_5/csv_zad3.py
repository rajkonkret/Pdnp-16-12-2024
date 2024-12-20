import pandas

data = pandas.read_csv('records_discount.csv', delimiter=";")
print(data)
#    sku  exp_date   price
# 0    1     today  100.00
# 1    2     today  200.00
# 2    3  tomorrow  500.00
# 3    4     today  200.00
# 4    5  tomorrow   99.99
print(data.columns)
# Index(['sku', 'exp_date', 'price'], dtype='object')
print(data.values)
# [[1 'today' 100.0]
#  [2 'today' 200.0]
#  [3 'tomorrow' 500.0]
#  [4 'today' 200.0]
#  [5 'tomorrow' 99.99]]
