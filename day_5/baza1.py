import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Baza zostałą podłączona")
except sqlite3.Error as e:
    print("Błąd", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
# Baza zostałą podłączona
# Połączenie zostało zamknięte