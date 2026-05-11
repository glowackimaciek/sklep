class Produkt:
    def __init__(self, nazwa, cena, ilosc, numer=""):
        if cena < 0:
            raise ValueError("Cena nie może być ujemna!")
        if ilosc < 0:
            raise ValueError("Ilość nie może być ujemna!")
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc
        self.numer = numer

    def produkt_info(self):
        return f"ID: {self.numer} | Nazwa: {self.nazwa} | Cena: {self.cena} | Ilość: {self.ilosc}"
