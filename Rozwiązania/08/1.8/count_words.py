# ZADANIE 8:
# Odczytanie tekstu z pliku pets.txt, wyświetlenie go
# i obliczenie liczby wszystkich słów.

# Otwieramy plik w trybie odczytu.
with open("pets.txt", "r") as file:

    # read() odczytuje całą zawartość pliku.
    content = file.read()

# Wyświetlamy tekst zapisany w pliku.
print("Text from file:")
print(content)

# Zmienna przechowuje łączną liczbę słów.
# Na początku liczba słów wynosi 0.
word_count = 0

# splitlines() dzieli tekst na osobne linie.
# Dzięki temu możemy przetwarzać każdą linię oddzielnie.
for line in content.splitlines():

    # split() dzieli linię na słowa.
    # Domyślnie rozdziela tekst w miejscach występowania białych znaków,
    # np. spacji, tabulatorów i znaków nowej linii.
    words = line.split()

    # len() zwraca liczbę elementów listy, czyli liczbę słów w tej linii.
    word_count += len(words)

# Wyświetlamy łączną liczbę słów ze wszystkich linii.
print("Number of words:", word_count)


# Notatka – problem ze znalezieniem pliku (FileNotFoundError)
# Python szuka pliku względem aktualnego folderu roboczego, a niekoniecznie folderu, w którym znajduje się plik .py.
# Rozwiązanie - zmiana folderu w terminalu:
# cd "Rozwiązania/08/1.8"
# python count_words.py
# - cd (change directory) – zmienia aktualny folder.
# - python read_car_park.py – uruchamia program.


# split() – dzieli tekst na listę słów.
# len() – zwraca liczbę elementów listy lub znaków w tekście.
# word_count += len(words) – dodaje liczbę słów z aktualnej linii do całkowitego wyniku.
# splitlines() – pozwala przejść przez tekst linia po linii.
# content – przechowuje całą zawartość pliku jako tekst.