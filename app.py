class Produkt:
    def __init__(self, nazwa, cena, ilosc):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc

    def produkt_info(self):
        return f"Nazwa: {self.nazwa} | Cena: {self.cena} | Ilość: {self.ilosc}"


produkt1 = Produkt("Iphone", 3999, 10)
print(produkt1.produkt_info())
