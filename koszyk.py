class Koszyk:
    def __init__(self):
        self.produkty = []
        self.suma = 0

    def dodaj_do_koszyka(self, produkt, ilosc):
        self.produkty.append((produkt, ilosc))
        self.suma = self.suma + produkt.cena * ilosc

    def pokaz_koszyk(self):
        for produkt, ilosc in self.produkty:
            print(f"Nazwa: {produkt.nazwa} | Cena: {produkt.cena} | Ilość: {ilosc}")
        print(f"Suma: {self.suma} zł")

    def wyczysc_koszyk(self):
        self.produkty = []
        self.suma = 0
        print("Koszyk wyczyszczono")
