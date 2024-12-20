import requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/usd/"

response = requests.get(url)
print(response)

# <Response [200]>
# 3xx - warningi, bład przekierowania
# 4xx - 404 brak zasobu, 400 Bad Request
# 5xx - błedy po stronie serwera, 500 Intertnal Error

print(response.text)
# {"table": "A", "currency": "dolar amerykański", "code": "USD",
#  "rates": [{"no": "247/A/NBP/2024", "effectiveDate": "2024-12-20", "mid": 4.1002}]}
data = response.json()
print(data)
# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD',
#  'rates': [{'no': '247/A/NBP/2024', 'effectiveDate': '2024-12-20', 'mid': 4.1002}]}
print(data['rates'])
# [{'no': '247/A/NBP/2024', 'effectiveDate': '2024-12-20', 'mid': 4.1002}]
print(data['rates'][0])
# {'no': '247/A/NBP/2024', 'effectiveDate': '2024-12-20', 'mid': 4.1002}
print(data['rates'][0]['mid'])  # 4.1002
