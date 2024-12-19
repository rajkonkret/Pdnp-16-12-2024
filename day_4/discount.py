from datetime import datetime, date, timedelta

today = date.today()
print(today)  # 2024-12-19
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print("Aktualny czas", time)  # Aktualny czas 2024-12-19 10:04:19.461929

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2024-12-20

print(time.time())  # 10:09:21.100622
print(today.day)  # 19

formatted_data = datetime.now().strftime("%d/%m/%Y")
print(formatted_data)  # 19/12/2024
print(type(formatted_data))  # <class 'str'>

# 10:11
formatted_time = datetime.now().strftime("%H:%M")
print(formatted_time)  # 10:15

#
formatted_time = datetime.now().strftime("%I:%M %p")
print(formatted_time)  # 10:17 AM

products = [
    {"sku": 1, 'exp_date': today, "price": 100},
    {"sku": 2, 'exp_date': today, "price": 200},
    {"sku": 3, 'exp_date': tomorrow, "price": 500},
    {"sku": 4, 'exp_date': today, "price": 200.00},
    {"sku": 5, 'exp_date': tomorrow, "price": 99.99},
]
for p in products:
    # print(p) # {'sku': 1, 'exp_date': datetime.date(2024, 12, 19), 'price': 100}
    # print(p['exp_date'])
    if p['exp_date'] != today:  # != rózne
        continue  # przrywa bierzącą iterację, wrac ana początek pętli, bierze kolejny element
    p['price'] *= 0.8  # price = price * 0.8
    print(f"""Price for sku {p['sku']}
is now {p['price']}""")
# Price for sku 1
# is now 80.0
# Price for sku 2
# is now 160.0
# Price for sku 4
# is now 160.0
