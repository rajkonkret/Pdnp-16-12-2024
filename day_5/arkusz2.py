import pandas as pd

data = pd.read_excel('courses.xlsx')
print(data)
#    Unnamed: 0 Courses    Fee Duration  Discount
# 0           0   Spark  25000  50 days      2000
# 1           1  Pandas  15000  30 Days      1500
# 2           2  Python  12000      NaN       800
# 3           3     PHP  23000  15 Days       500

df = pd.DataFrame(data)
print(type(df)) # <class 'pandas.core.frame.DataFrame'>

# filtrowanie danych
print(df[df["Fee"] > 15000])
#    Unnamed: 0 Courses    Fee Duration  Discount
# 0           0   Spark  25000  50 days      2000
# 3           3     PHP  23000  15 Days       500
