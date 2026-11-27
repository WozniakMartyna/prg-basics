# ZADANIE 9:
# Wyświetlenie pracowników zatrudnionych na stanowisku Software Engineer.

# Nazwa pliku z danymi pracowników.
file_name = "it_company.csv"

# Określamy stanowisko, którego szukamy.
job_title = "Software Engineer"

# Numer pierwszego znalezionego pracownika.
number = 1

# Otwieramy plik w trybie odczytu.
with open(file_name, "r") as file:

    # Odczytujemy plik linia po linii.
    for line in file:

        # Operator in sprawdza, czy dany tekst znajduje się w innym tekście.
        # Sprawdzamy, czy nazwa stanowiska występuje w aktualnej linii.
        if job_title in line:

            # strip() usuwa zbędne białe znaki z początku i końca tekstu,
            # np. znak nowej linii.
            print(f"{number}. {line.strip()}")

            # Zwiększamy numer po wyświetleniu pracownika.
            number += 1

# Notatka – problem ze znalezieniem pliku (FileNotFoundError)
# Python szuka pliku względem aktualnego folderu roboczego, a niekoniecznie folderu, w którym znajduje się plik .py.
# Rozwiązanie - zmiana folderu w terminalu:
# cd "Rozwiązania/08/1.9"
# python employees.py
# - cd (change directory) – zmienia aktualny folder.
# - python read_car_park.py – uruchamia program.

# in – sprawdza, czy określony element lub tekst znajduje się w innym elemencie lub tekście.
# if – wykonuje instrukcje tylko wtedy, gdy warunek jest prawdziwy.
# strip() – usuwa białe znaki z początku i końca tekstu.
# number += 1 – zwiększa numer o jeden.
# f"..." – pozwala wstawiać wartości zmiennych do tekstu za pomocą {}.