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


def menu(sklep, koszyk):
    while True:
        print(f"\n--- Sklep {sklep.nazwa} ---")
        print("1. Pokaż produkty w sklepie")
        print("2. Dodaj produkt do koszyka")
        print("3. Pokaż koszyk")
        print("4. Wyjdź")

        try:
            choice = int(input("Wybierz: "))
        except ValueError:
            print("Tylko cyfry")
            continue

        if choice == 1:
            if not sklep.produkty:
                print("Brak produktów w sklepie")
            else:
                sklep.pokaz_produkty()
        elif choice == 2:
            if not sklep.produkty:
                print("Brak produktów w sklepie")
            else:
                sklep.pokaz_produkty()
                try:
                    nr = int(input("Podaj numer: ")) - 1
                    ilosc = int(input("Podaj ilosc: "))
                except ValueError:
                    print("Tylko cyfry")
                    continue

                koszyk.dodaj_do_koszyka(sklep.produkty[nr], ilosc)
                print("Dodano do koszyka")
        elif choice == 3:
            if not koszyk.produkty:
                print("Koszyk jest pusty")
            else:
                koszyk.pokaz_koszyk()
        elif choice == 4:
            print("Zamykanie...")
            break
        else:
            print("Tylko cyfry 1-4")
            continue


sklep = Sklep("Media Expert")
sklep.dodaj_produkt("Iphone", 2999, 10)
sklep.dodaj_produkt("Sony XMH 4500", 999, 10)

koszyk = Koszyk()
menu(sklep, koszyk)
