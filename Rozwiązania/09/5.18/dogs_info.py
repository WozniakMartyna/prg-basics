
# ZADANIE 5.18:
# Odczytanie danych o psach z pliku dogs.json
# i wyświetlenie informacji tylko o psach młodszych niż 5 lat.

import json  # Importujemy moduł do obsługi plików JSON.

# Otwieramy plik dogs.json w trybie "r" (read), czyli do odczytu.
# encoding="utf-8" pozwala poprawnie odczytywać znaki tekstowe.
# with automatycznie zamyka plik po zakończeniu odczytywania.
with open("dogs.json", "r", encoding="utf-8") as file:

    # json.load() odczytuje dane z pliku JSON.
    # W tym przypadku otrzymujemy listę słowników – każdy opisuje jednego psa.
    data = json.load(file)


# Wyświetlamy nagłówek programu.
print("DOGS YOUNGER THAN 5 YEARS")
print("=========================")

# Przechodzimy kolejno przez wszystkie słowniki na liście.
# Każdy element dog zawiera informacje o jednym psie.
for dog in data:

    # Pobieramy wiek aktualnego psa ze słownika.
    age = dog["age"]

    # Sprawdzamy, czy pies ma mniej niż 5 lat.
    # Operator < oznacza "mniejsze niż".
    # Pies mający dokładnie 5 lat nie spełnia tego warunku.
    if age < 5:

        # Jeśli warunek jest prawdziwy, wyświetlamy wszystkie informacje o psie.
        # items() zwraca pary klucz-wartość ze słownika.
        for key, value in dog.items():

            # Wyświetlamy nazwę pola i jego wartość.
            print(key, ":", value)

        # Dodajemy pustą linię, aby oddzielić informacje o kolejnych psach.
        print()


# do terminala
# cd "Rozwiązania/09/5.18"
# python dogs_info.py

# dog["age"] – pobiera wartość wieku z aktualnego słownika.
# age < 5 – sprawdza, czy wiek jest mniejszy od 5.
# if – wykonuje kod tylko wtedy, gdy warunek jest prawdziwy.
# dog.items() – pozwala przejść przez wszystkie pary klucz-wartość.
# for dog in data – przechodzi przez wszystkie psy na liście.