
# ZADANIE 4.10:
# Wyświetlanie produktów, których cena jest mniejsza niż 60,
# a liczba sztuk w magazynie jest mniejsza niż 40.
# Dane odczytujemy z pliku clothing.csv.

import csv
# Importujemy moduł csv do odczytywania danych z plików CSV.

file_name = "clothing.csv"

with open(file_name, "r", encoding="utf-8", newline="") as file:
    # Otwieramy plik w trybie odczytu ("r").
    # newline="" jest zalecane podczas korzystania z modułu csv.

    reader = csv.DictReader(file)
    # DictReader odczytuje każdy wiersz jako słownik.
    # Nazwy kolumn z pierwszego wiersza stają się kluczami.

    print("PRODUCTS")
    print("========")

    for product in reader:
        # Przechodzimy po kolejnych produktach z pliku CSV.
        # Każdy produkt jest zapisany jako słownik.

        name = product["Product_Name"]
        # Pobieramy nazwę produktu z kolumny Product_Name.

        price = float(product["Price"])
        # Pobieramy cenę i zamieniamy tekst na liczbę zmiennoprzecinkową.
        # Dzięki float() możemy porównywać ceny jako liczby.

        stock = int(product["Stock_Quantity"])
        # Pobieramy liczbę sztuk w magazynie.
        # int() zamienia tekst na liczbę całkowitą.

        if price < 60 and stock < 40:
            # < oznacza "mniejsze niż".
            # and oznacza, że oba warunki muszą być spełnione:
            # cena poniżej 60 ORAZ stan magazynowy poniżej 40.

            print(f"{name}, Price: {price}, Stock: {stock}")
            # Wyświetlamy nazwę produktu, cenę i liczbę sztuk.

# do terminala
# cd "Rozwiązania/08/4.10"
# python filter_clothing.py