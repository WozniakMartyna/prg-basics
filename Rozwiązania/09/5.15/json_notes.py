
# ZADANIE 09.5.15:
# Przykłady wykorzystania formatu JSON w języku Python.
#
# JSON (JavaScript Object Notation) to format zapisu i wymiany danych.
# Pozwala przechowywać dane w uporządkowanej postaci, np. w plikach.
# W Pythonie do obsługi JSON wykorzystujemy wbudowany moduł json.

import json  # Importujemy moduł json, który umożliwia obsługę formatu JSON.


# 1. TWORZENIE SŁOWNIKA PYTHONA

# Tworzymy słownik zawierający dane osoby.
# Słownik przechowuje dane w parach klucz: wartość.
person = {
    "name": "Anna",
    "age": 25,
    "city": "Krakow",
    "student": True
}

print("PYTHON DICTIONARY:")
print(person)


# 2. ZAMIANA SŁOWNIKA NA TEKST JSON

# json.dumps() zamienia obiekt Pythona, np. słownik, na tekst w formacie JSON.
# dumps oznacza zapis do tekstu, a nie bezpośrednio do pliku.
#
# indent=4 ustawia wcięcia, dzięki czemu tekst jest czytelniejszy.
# ensure_ascii=False pozwala zapisywać polskie znaki bez zamiany na kody Unicode.
person_json = json.dumps(person, indent=4, ensure_ascii=False)

print("\nJSON TEXT:")
print(person_json)


# 3. ZAMIANA TEKSTU JSON NA SŁOWNIK PYTHONA

# json.loads() wykonuje odwrotną operację do json.dumps().
# Zamienia tekst JSON na obiekt Pythona, w tym przypadku słownik.
person_from_json = json.loads(person_json)

print("\nDICTIONARY FROM JSON:")
print(person_from_json)

# Możemy teraz odczytywać dane tak samo jak ze zwykłego słownika.
print("Name:", person_from_json["name"])
print("Age:", person_from_json["age"])


# 4. ZAPISYWANIE DANYCH DO PLIKU JSON

file_name = "person.json"

# Otwieramy plik w trybie "w" (write), czyli zapisu.
# Jeśli plik nie istnieje, Python go utworzy.
# Jeśli istnieje, jego poprzednia zawartość zostanie zastąpiona.
with open(file_name, "w", encoding="utf-8") as file:

    # json.dump() zapisuje obiekt Pythona bezpośrednio do otwartego pliku.
    # indent=4 poprawia czytelność zapisanego pliku.
    json.dump(person, file, indent=4, ensure_ascii=False)

print("\nData has been saved to", file_name)


# 5. ODCZYTYWANIE DANYCH Z PLIKU JSON

# Otwieramy wcześniej utworzony plik w trybie "r" (read), czyli odczytu.
with open(file_name, "r", encoding="utf-8") as file:

    # json.load() odczytuje dane z pliku JSON i zamienia je na obiekt Pythona.
    loaded_person = json.load(file)

print("\nDATA READ FROM FILE:")
print(loaded_person)

# Ponownie możemy odwoływać się do wartości za pomocą kluczy słownika.
print("Person's city:", loaded_person["city"])


# 6. DODAWANIE NOWEJ DANYCH I PONOWNY ZAPIS

# Dodajemy nową parę klucz: wartość do słownika.
loaded_person["hobby"] = "reading"

# Ponownie zapisujemy zmieniony słownik do pliku.
# Tryb "w" zastępuje poprzednią zawartość pliku nowymi danymi.
with open(file_name, "w", encoding="utf-8") as file:
    json.dump(loaded_person, file, indent=4, ensure_ascii=False)

print("\nUPDATED DATA:")
print(loaded_person)

# Najważniejsze do zapamiętania
# Instrukcja	Działanie
# import json	Importuje moduł do obsługi JSON
# json.dumps()	Zamienia obiekt Pythona na tekst JSON
# json.loads()	Zamienia tekst JSON na obiekt Pythona
# json.dump()	Zapisuje dane do pliku JSON
# json.load()	Odczytuje dane z pliku JSON
# indent=4	Ustawia czytelne wcięcia
# ensure_ascii=False	Pozwala zapisywać polskie znaki bez kodowania ich jako sekwencji Unicode
# "r"	Otwiera plik do odczytu
# "w"	Otwiera plik do zapisu

# Ważna różnica:
# - dump i load – pracują bezpośrednio z plikiem.
# - dumps i loads – pracują z tekstem.