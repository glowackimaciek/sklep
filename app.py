class Produkt:
    def __init__(self, nazwa, cena, ilosc):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc

    def produkt_info(self):
        return f"Nazwa: {self.nazwa} | Cena: {self.cena} | Ilość: {self.ilosc}"


class Sklep:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.produkty = []

    def dodaj_produkt(self, nazwa, cena, ilosc):
        nowy = Produkt(nazwa, cena, ilosc)
        self.produkty.append(nowy)

    def pokaz_produkty(self):
        for produkt in self.produkty:
            print(produkt.produkt_info())


sklep = Sklep("Media Expert")
sklep.dodaj_produkt("Iphone", 2999, 10)
sklep.dodaj_produkt("Sony XMH 4500", 999, 10)
sklep.pokaz_produkty()
