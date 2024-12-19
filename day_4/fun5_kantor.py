# stworzyc funkcje kantor
# ma miec dwie wewnętrzne funkcje usd, eur
# w zależności od parametru zwracmy funkcje usd, eur

def kantor(waluta):
    def usd(kwota=0):
        print(f"Wymieniam dolary {kwota} na {kwota * 4.08} pln")

    def eur(kwota=0):
        print(f"Wymieniam euro {kwota} na {kwota * 4.25} pln")

    if waluta == "usd":
        return usd
    else:
        return eur


kantor_usd = kantor("usd")
kantor_usd()  # Wymieniam dolary

kantor_eur = kantor("eur")
kantor_eur()

kantor_eur(2000)  # Wymieniam euro 2000 na 8500.0 pln
kantor_usd(2000)  # Wymieniam dolary 2000 na 8160.0 pln
