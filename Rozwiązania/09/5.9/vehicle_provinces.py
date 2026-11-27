# ZADANIE 5.9:
# Program odczytuje numery rejestracyjne z pliku vehicle.txt
# i przypisuje do nich nazwy województw na podstawie pierwszej litery.

import csv  # Moduł csv służy do odczytywania i zapisywania plików CSV.


# TWORZENIE SŁOWNIKA WOJEWÓDZTW

provinces = {}  # Pusty słownik. Będzie przechowywał pary: litera - nazwa województwa.

# Otwieramy plik province.csv w trybie "r" (read), czyli odczytu.
# encoding="utf-8" pozwala poprawnie odczytywać polskie znaki, np. ą, ę, ś, ł.
# with automatycznie zamknie plik po zakończeniu wykonywania tego bloku.
with open("province.csv", "r", encoding="utf-8") as file:

    # DictReader odczytuje plik CSV jako słowniki.
    # Nazwy kolumn z pierwszego wiersza (Letter, Name) stają się kluczami.
    reader = csv.DictReader(file)

    # Pętla przechodzi kolejno przez wszystkie wiersze pliku CSV.
    # row oznacza aktualnie odczytywany wiersz.
    for row in reader:

        # Pobieramy wartości z odpowiednich kolumn.
        letter = row["Letter"]  # Litera rejestracyjna, np. K.
        name = row["Name"]      # Nazwa województwa, np. Małopolskie.

        # Dodajemy dane do słownika.
        # letter jest kluczem, a name wartością.
        provinces[letter] = name


# ODCZYTYWANIE NUMERÓW REJESTRACYJNYCH

# Otwieramy plik vehicle.txt w trybie "r", czyli do odczytu.
with open("vehicle.txt", "r", encoding="utf-8") as file:

    # Pętla odczytuje plik linia po linii.
    # Każda linia zawiera jeden numer rejestracyjny.
    for line in file:

        # strip() usuwa zbędne białe znaki z początku i końca tekstu,
        # w tym znak nowej linii (\n).
        registration = line.strip()

        # Sprawdzamy, czy linia nie jest pusta.
        # != oznacza "różne od".
        if registration != "":

            # Indeks [0] pobiera pierwszy znak tekstu.
            # Np. dla "KRA1234" otrzymamy literę "K".
            # Indeksy w Pythonie zaczynają się od zera.
            letter = registration[0]

            # Operator "in" sprawdza, czy litera istnieje wśród kluczy słownika.
            if letter in provinces:

                # provinces[letter] pobiera nazwę województwa przypisaną do litery.
                # f przed tekstem pozwala wstawiać wartości zmiennych w nawiasach {}.
                print(f"{registration} - {provinces[letter]}")

            else:
                # Ten fragment wykona się, jeśli litery nie ma w słowniku.
                print(f"{registration} - Nieznane województwo")

# do terminala
# cd "Rozwiązania/09/5.9"
# python vehicle_provinces.py