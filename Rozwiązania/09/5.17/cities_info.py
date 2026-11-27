# ZADANIE 5.17:
# Odczytanie danych o polskich miastach z pliku cities.json
# i wyświetlenie informacji o każdym mieście.

import json  # Moduł json służy do odczytywania i zapisywania danych w formacie JSON.

# Otwieramy plik cities.json w trybie "r" (read), czyli do odczytu.
# encoding="utf-8" jest ważne, ponieważ plik zawiera polskie znaki,
# np. ą, ć, ę, ł, ń, ó, ś, ź, ż.
# with automatycznie zamknie plik po zakończeniu odczytywania.
with open("cities.json", "r", encoding="utf-8") as file:

    # json.load() odczytuje dane z pliku JSON i zamienia je na obiekty Pythona.
    # W tym przypadku otrzymujemy listę słowników, ponieważ plik zawiera tablicę JSON.
    data = json.load(file)


# Wyświetlamy informacje o wszystkich miastach.
# Pętla for przechodzi kolejno przez elementy listy data.
# Każdy element city jest osobnym słownikiem opisującym jedno miasto.
for city in data:

    # items() zwraca pary klucz-wartość z aktualnego słownika miasta.
    # key przechowuje nazwę właściwości, np. "city".
    # value przechowuje jej wartość, np. "Warsaw".
    for key, value in city.items():

        # Wyświetlamy nazwę właściwości i jej wartość.
        print(key, ":", value)

    # Pusta instrukcja print() dodaje pustą linię,
    # żeby informacje o kolejnych miastach były od siebie oddzielone.
    print()

# do terminala
# cd "Rozwiązania/09/5.17"
# python cities_info.py

# W pliku JSON mamy nawiasy kwadratowe [], ponieważ dane są listą. Wewnątrz znajdują się nawiasy klamrowe {}, ponieważ każde miasto jest słownikiem.
# Jak Python odczytuje te dane?
# - data – cała lista miast.
# - city – jeden słownik opisujący aktualne miasto.
# - city.items() – pary klucz-wartość z tego słownika.
# - key – nazwa pola, np. "population".
# - value – wartość pola, np. 779115.