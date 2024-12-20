import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Baza zostałą podłączona")

    query = """
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary REAL NOT NULL);
    """

    # c.execute(query)
    # conn.commit()

    insert = """
    INSERT INTO developers (id,name,salary)
    VALUES (1,'Radek','11000');
    """

    # c.execute(insert)
    # conn.commit()

    for i in c.execute("SELECT * FROM developers;"):
        print(i) # (1, 'Radek', 11000.0)
except sqlite3.Error as e:
    print("Błąd", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
# Baza zostałą podłączona
# Połączenie zostało zamknięte
