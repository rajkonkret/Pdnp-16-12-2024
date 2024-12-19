import chardet

# pip install chardet

with open('test.log', "r", encoding="utf-8") as f:
    raw_data = f.read()

print(raw_data)

# rb - odczyt bajtowy
with open('test.log', 'rb') as f:
    raw_data = f.read()

print(raw_data)
# b'Nadpisane\r\nDopisanie\r\nDopisane\r\nDodane\r\nDo\xc5\x9bdane\r\n'

result = chardet.detect(raw_data)
print(result)
# po zwiększeniu próbki (więcej polskich znaków w pliku)
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
encoding = result['encoding']
confidence = result['confidence']
print("Kodowanie:", encoding)
print("Trafność", confidence)
# Kodowanie: utf-8
# Trafność 0.99

print(raw_data.decode(encoding=encoding))
# Nadpisane
# Dopisanie
# Dopisane
# Dodane
# Dośdane
# Dośćąźdane
