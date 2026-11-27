
# ZADANIE 4.9:
# Wyszukiwanie pracowników zatrudnionych jako Graphic Designer.
# Odczytujemy dane z pliku CSV za pomocą modułu csv.

import csv
# Importujemy wbudowany moduł csv.
# Umożliwia on wygodne odczytywanie danych z plików CSV.

file_name = "it_company.csv"

with open(file_name, "r", encoding="utf-8", newline="") as file:
    # Otwieramy plik CSV w trybie odczytu.
    # newline="" jest zalecane podczas pracy z modułem csv.

    reader = csv.DictReader(file)
    # DictReader odczytuje plik CSV jako słowniki.
    # Nazwy kolumn z pierwszego wiersza stają się kluczami słownika.
    #
    # Przykładowo:
    # employee["First Name"] - imię pracownika,
    # employee["Last Name"]  - nazwisko pracownika,
    # employee["Job Title"]  - stanowisko,
    # employee["Email"]      - adres e-mail.

    print("GRAPHIC DESIGNERS")
    print("=================")

    for employee in reader:
        # Pętla przechodzi przez kolejne rekordy pracowników.
        # Każdy rekord zapisany jest w zmiennej employee jako słownik.

        if employee["Job Title"] == "Graphic Designer":
            # Sprawdzamy, czy stanowisko pracownika jest dokładnie
            # równe tekstowi "Graphic Designer".
            # == oznacza porównanie dwóch wartości.

            first_name = employee["First Name"]
            # Pobieramy imię z odpowiedniej kolumny.

            last_name = employee["Last Name"]
            # Pobieramy nazwisko.

            email = employee["Email"]
            # Pobieramy adres e-mail.

            print(f"{first_name} {last_name},{email}")
            # f-string pozwala wstawić wartości zmiennych do tekstu.
            # Wyświetlamy imię, nazwisko i adres e-mail.

# do terminala
# cd "Rozwiązania/08/4.9"
# python graphic_designers.py