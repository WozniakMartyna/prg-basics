# ZADANIE 5: Odczytywanie krajów i numerowanie ich

with open("countries.txt", "r") as file:

    # Ustawiamy numer pierwszego kraju.
    number = 1

    # Odczytujemy plik linia po linii.
    for line in file:

        # f-string pozwala wstawić wartość zmiennej do tekstu.
        print(f"{number}. {line}", end="")

        # Zwiększamy numer o 1 po każdym kraju.
        number += 1

# Notatka – problem ze znalezieniem pliku (FileNotFoundError)
# Python szuka pliku względem aktualnego folderu roboczego, a niekoniecznie folderu, w którym znajduje się plik .py.
# Rozwiązanie - zmiana folderu w terminalu:
# cd "Rozwiązania/08/1.5"
# python print_countries.py
# - cd (change directory) – zmienia aktualny folder.
# - python print_countries.py – uruchamia program.