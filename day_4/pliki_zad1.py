# działania z plikami
# context manager do usprawnienia pracy np.:  z plikami
# with - context manager w pythonie

# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', "w", encoding='utf-8') as fh:  # filehandler - rura do pliku
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jeszcze jedno\n")

# "x" rzuca błedem gdy plik juz istnieje
# with open('test.log', "x", encoding='utf-8') as fh: # filehandler - rura do pliku
#     fh.write("Powitanie\n")
#     fh.write("Kolejne\n")
#     fh.write("Jeszcze jedno\n")
# FileExistsError: [Errno 17] File exists: 'test.log'
with open('test.log', "w", encoding='utf-8') as fh:  # filehandler - rura do pliku
    fh.write("Nadpisane\n")

# "a" - dopisanie
with open('test.log', "a", encoding='utf-8') as fh:  # filehandler - rura do pliku
    fh.write("Dopisanie\n")
    fh.write("Dopisane\n")
    fh.write("Dodane\n")
    fh.write("Dośdane\n")
    fh.write("Dośćąźdane\n")

with open('test.log', "r", encoding='utf-8') as file:
    lines = file.read()

print(lines)
