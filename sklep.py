from produkt import Produkt


class Sklep:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.produkty = []

    def dodaj_produkt(self, nazwa, cena, ilosc):
        try:
            numer = len(self.produkty) + 1
            nowy = Produkt(nazwa, cena, ilosc, numer)
            self.produkty.append(nowy)
        except ValueError as e:
            print(f"Błąd: {e}")

    def pokaz_produkty(self):
        for produkt in self.produkty:
            print(produkt.produkt_info())
