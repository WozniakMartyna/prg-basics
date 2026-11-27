# ZADANIE 5.16:
# Odczytanie informacji o komputerze z pliku computer.json
# i wyświetlenie wszystkich danych na ekranie.

import json  # Importujemy moduł json, który służy do obsługi plików JSON.

# Otwieramy plik computer.json w trybie "r" (read), czyli do odczytu.
# encoding="utf-8" zapewnia poprawne odczytywanie znaków tekstowych.
# with automatycznie zamknie plik po zakończeniu odczytywania.
with open("computer.json", "r", encoding="utf-8") as file:

    # json.load() odczytuje dane z pliku JSON i zamienia je na obiekt Pythona.
    # Ponieważ plik zawiera jeden słownik, zmienna data będzie słownikiem.
    data = json.load(file)

# Wyświetlamy nagłówek programu.
print("COMPUTER INFORMATION")
print("====================")

# items() zwraca pary klucz-wartość ze słownika.
# key przechowuje nazwę właściwości, np. "manufacturer".
# value przechowuje jej wartość, np. "Dell".
# Pętla przechodzi przez wszystkie elementy słownika.
for key, value in data.items():

    # Wyświetlamy nazwę właściwości i przypisaną do niej wartość.
    print(key, ":", value)

# do terminala
# cd "Rozwiązania/09/5.16"
# python computer_info.py

# json.load(file) – odczytuje dane z pliku JSON i zamienia je na obiekt Pythona.
# data – zmienna przechowująca odczytany słownik.
# .items() – pozwala pobierać jednocześnie klucz i wartość ze słownika.
# for key, value in data.items() – przechodzi przez wszystkie pary w słowniku.
# key – nazwa właściwości, np. "model".
# value – wartość właściwości, np. "XPS 15".