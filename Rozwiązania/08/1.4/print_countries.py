# ZADANIE 4: Odczytywanie pliku tekstowego linia po linii

# open() otwiera plik countries.txt.
# "r" oznacza tryb odczytu (read).
# as file przypisuje otwartemu plikowi nazwę file.
with open("countries.txt", "r") as file:

    # for przechodzi przez plik, odczytując kolejne linie.
    for line in file:

        # Wyświetlamy aktualną linię.
        # end="" zapobiega dodaniu dodatkowego pustego wiersza,
        # ponieważ linia z pliku ma już znak końca linii.
        print(line, end="")


# Notatka – problem ze znalezieniem pliku (FileNotFoundError)
# Python szuka pliku względem aktualnego folderu roboczego, a niekoniecznie folderu, w którym znajduje się plik .py.
# Rozwiązanie - zmiana folderu w terminalu:
# cd "Rozwiązania/08/1.4"
# python print_countries.py
# - cd (change directory) – zmienia aktualny folder.
# - python print_countries.py – uruchamia program.