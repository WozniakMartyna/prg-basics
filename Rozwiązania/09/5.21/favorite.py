# ZADANIE 5.21: Utworzenie słownika z informacjami o ulubionej książce
# lub filmie, a następnie zapisanie tych informacji do pliku JSON.

import json  # Importujemy moduł json, który umożliwia zapisywanie
             # i odczytywanie danych w formacie JSON.

# Tworzymy słownik zawierający informacje o ulubionej książce.
# Słownik składa się z par: klucz (np. "title") i wartość (np. tytuł książki).
favorite = {
    "type": "book",  # Określamy, czy zapisujemy książkę, czy film.
    "title": "Harry Potter and the Philosopher's Stone",
    "author": "J.K. Rowling",
    "year": 1997,
    "genre": "Fantasy"
}

# Podajemy nazwę pliku, w którym chcemy zapisać dane.
file_name = "favorite.json"

# Otwieramy plik w trybie zapisu.
# "w" oznacza write, czyli zapis.
# Jeśli plik nie istnieje, Python automatycznie go utworzy.
# Jeśli już istnieje, jego poprzednia zawartość zostanie zastąpiona.
# encoding="utf-8" pozwala prawidłowo zapisywać polskie znaki.
with open(file_name, "w", encoding="utf-8") as file:

    # json.dump() zapisuje dane ze słownika favorite do otwartego pliku.
    # Pierwszy argument to dane, które chcemy zapisać.
    # Drugi argument to plik, do którego zapisujemy dane.
    # indent=4 ustawia cztery spacje wcięcia, dzięki czemu JSON jest czytelny.
    # ensure_ascii=False pozwala zapisywać polskie znaki bez zamiany na kody.
    json.dump(favorite, file, indent=4, ensure_ascii=False)

# Wyświetlamy komunikat informujący, że zapis został wykonany.
print("Favorite item has been saved to", file_name)

# do terminala
# cd "Rozwiązania/09/5.21"
# python favorite.py