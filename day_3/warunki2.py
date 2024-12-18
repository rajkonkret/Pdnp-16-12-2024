# python 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programowania")

match lang.casefold().strip():
    case "python":
        lista.append("Znam Pythona")
    case "java":
        lista.append("znam Javę")
    case _:  # wartośc domyslna, odpowiednik else
        print("Nie znam takiego języka")

print(lista)
# Podaj znany Ci język programowaniajava
# ['znam Javę']
