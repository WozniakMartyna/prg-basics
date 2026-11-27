# ZADANIE 4.12:
# Podział książek z pliku books.csv na osobne pliki
# tekstowe w zależności od gatunku.

import csv

# Słownik łączy nazwę gatunku z nazwą pliku,
# do którego mają zostać zapisane książki tego gatunku.
output_files = {
    "Fantasy": "books_fantasy.txt",
    "Historical": "books_historical.txt",
    "Romance": "books_romance.txt",
    "Classic": "books_classic.txt"
}


# Funkcja zapisuje jedną książkę do odpowiedniego pliku.
def save_book(book):
    genre = book["Genre"]  # Odczytujemy gatunek książki.

    # Sprawdzamy, czy gatunek znajduje się w naszym słowniku.
    # Jeśli go nie ma, funkcja zakończy działanie bez zapisu.
    if genre not in output_files:
        return

    file_name = output_files[genre]

    # "a" oznacza dopisywanie do pliku.
    # Jeśli plik nie istnieje, Python utworzy go automatycznie.
    # encoding="utf-8" pozwala poprawnie zapisywać polskie znaki.
    with open(file_name, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        # Zapisujemy wszystkie informacje o książce:
        # tytuł, autora, gatunek i rok wydania.
        writer.writerow([
            book["Title"],
            book["Author"],
            book["Genre"],
            book["Year"]
        ])


# Główna część programu.
def main():

    # Najpierw czyścimy pliki wynikowe i dodajemy nagłówki.
    # Dzięki temu ponowne uruchomienie programu nie powieli danych.
    for genre, file_name in output_files.items():
        with open(file_name, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Author", "Genre", "Year"])

    try:
        # Otwieramy plik wejściowy do odczytu.
        with open("books.csv", "r", encoding="utf-8", newline="") as file:

            # DictReader odczytuje każdy wiersz jako słownik.
            # Nazwy kolumn, np. "Title" i "Genre", są kluczami.
            reader = csv.DictReader(file)

            # Przechodzimy po wszystkich książkach w pliku.
            for book in reader:
                save_book(book)

        print("Books have been divided into separate files.")

    except FileNotFoundError:
        # Ten komunikat pojawi się, jeśli books.csv nie zostanie znaleziony.
        print("Error: books.csv was not found.")


# Uruchamiamy funkcję main(), gdy ten plik jest uruchamiany bezpośrednio.
if __name__ == "__main__":
    main()

# do terminala
# cd "Rozwiązania/08/4.12"
# python split_books.py


# import csv – importuje moduł do obsługi plików CSV.
# csv.DictReader(file) – odczytuje dane jako słowniki, gdzie nazwy kolumn są kluczami.
# book["Genre"] – pobiera gatunek książki.
# if genre not in output_files – sprawdza, czy gatunek nie znajduje się w naszym słowniku.
# return – kończy działanie funkcji. Tutaj oznacza, że książka z nieobsługiwanym gatunkiem nie zostanie zapisana.
# csv.writer(file) – umożliwia zapisywanie danych w formacie kolumn oddzielonych przecinkami.
# writer.writerow([...]) – zapisuje jeden wiersz danych.
# "a" – dopisuje dane do pliku, a "w" – tworzy plik od nowa lub usuwa jego poprzednią zawartość.
# if __name__ == "__main__": – uruchamia main() tylko wtedy, gdy uruchamiamy ten plik bezpośrednio.