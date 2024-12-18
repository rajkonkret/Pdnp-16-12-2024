# wyjątki - błędy podcas działania programu

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\Pdnp-16-12-2024\day_3\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

try:
    # print(5 / 0)
    # print("a" + 9)
    # print(int("A"))
    # raise KeyError("Brak klucza")
    wynik = 90 / 33
except ZeroDivisionError:
    print("Nie dzielimy przez zero")
except TypeError:
    print("Błąd typu")
except ValueError:
    print("Błąd waartości")
except Exception as e:
    print("Błąd", e)
else:  # gdy nie ma błedu
    print('wynik', wynik)
finally:
    print("wykonuje się zawsze")
# Nie dzielimy przez zero
# Błąd 'Brak klucza'
# wynik 2.727272727272727
