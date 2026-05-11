from produkt import Produkt
from sklep import Sklep
from koszyk import Koszyk


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
                    if nr < 0 or nr >= len(sklep.produkty):
                        print("Brak takiego produktu w sklepie")
                        continue
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
