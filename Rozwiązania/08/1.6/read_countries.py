# ZADANIE 6:
# Odczytanie danych z pliku countries.txt, zapisanie ich na liście
# i wyświetlenie krajów w kolejności alfabetycznej.

# Funkcja read_from_file() odczytuje zawartość pliku.
# Parametr name oznacza nazwę pliku przekazaną do funkcji.
def read_from_file(name):

    # "r" oznacza tryb odczytu (read).
    # with automatycznie zamyka plik po zakończeniu pracy.
    with open(name, "r") as file:

        # read() odczytuje całą zawartość pliku jako jeden tekst.
        content = file.read()

    # return zwraca odczytany tekst do miejsca wywołania funkcji.
    return content


# Wywołujemy funkcję i zapisujemy zwrócony tekst w zmiennej.
file_content = read_from_file("countries.txt")

# splitlines() dzieli tekst na osobne linie i tworzy listę.
# Każdy kraj będzie osobnym elementem listy.
file_lines = file_content.splitlines()

# sorted() tworzy nową listę posortowaną alfabetycznie.
# Oryginalna lista file_lines pozostaje bez zmian.
sorted_lines = sorted(file_lines)

# Wyświetlamy posortowane kraje.
for line in sorted_lines:
    print(line)

# Notatka – problem ze znalezieniem pliku (FileNotFoundError)
# Python szuka pliku względem aktualnego folderu roboczego, a niekoniecznie folderu, w którym znajduje się plik .py.
# Rozwiązanie - zmiana folderu w terminalu:
# cd "Rozwiązania/08/1.6"
# python read_countries.py
# - cd (change directory) – zmienia aktualny folder.
# - python raed_countries.py – uruchamia program.


# - def – rozpoczyna definicję funkcji.
# - name – parametr funkcji, czyli wartość, którą przekazujemy do niej przy wywołaniu.
# - read() – odczytuje całą zawartość pliku jako jeden tekst.
# - return – zwraca wynik działania funkcji.
# - splitlines() – dzieli tekst na linie i umieszcza je na liście.
# - sorted() – sortuje elementy i zwraca nową listę. Domyślnie sortuje tekst alfabetycznie.
# - for – przechodzi kolejno przez elementy listy.
# Ważna różnica: read() odczytuje cały plik naraz, a for line in file pozwala odczytywać go linia po linii