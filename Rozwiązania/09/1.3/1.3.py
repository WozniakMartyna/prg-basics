# ZADANIE 1.3:
# Utworzenie słownika opisującego telefon i wyświetlenie jego zawartości.

# Słownik przechowuje dane w parach: klucz: wartość.
# Każdy klucz opisuje jedną właściwość telefonu.
mobile = {
    "OS": "Android",
    "Brand": "Samsung",
    "Model": "Galaxy S24",
    "Storage": "256 GB",
    "Color": "Black",
    "Year": 2024
}

# .items() zwraca pary klucz-wartość ze słownika.
# key przechowuje klucz, a value przypisaną do niego wartość.
for key, value in mobile.items():
    print(f"{key} : {value}")


# {} – tworzy słownik.
# "OS" – klucz słownika.
# "Android" – wartość przypisana do klucza.
# .items() – pozwala pobierać jednocześnie klucz i wartość.
# for key, value in ... – przypisuje kolejne pary słownika do dwóch zmiennych.