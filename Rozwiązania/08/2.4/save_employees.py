# ZADANIE 4:
# Zapisanie do pliku pracowników zatrudnionych jako Software Engineer.

# Nazwa pliku zawierającego wszystkich pracowników.
employees_file = "it_company.csv"

# Nazwa pliku, do którego zapiszemy wybranych pracowników.
position_file = "software_engineer.txt"

# Określamy stanowisko, którego szukamy.
job_title = "Software Engineer"

# Otwieramy plik docelowy w trybie zapisu ("w").
# Plik zostanie utworzony lub nadpisany, jeśli już istnieje.
with open(position_file, "w") as output_file:

    # Otwieramy plik źródłowy w trybie odczytu ("r").
    with open(employees_file, "r") as input_file:

        # Odczytujemy dane pracowników linia po linii.
        for line in input_file:

            # Sprawdzamy, czy w aktualnej linii znajduje się szukane stanowisko.
            if job_title in line:

                # Jeśli warunek jest prawdziwy, zapisujemy całą linię
                # do pliku software_engineer.txt.
                output_file.write(line)

# Informujemy o zakończeniu działania programu.
print(f"Employees have been saved to {position_file}.")

# do terminala:
# cd "Rozwiązania/08/2.4"
# python save_employees.py

# with open(..., "w") as output_file – otwiera plik docelowy do zapisu.
# with open(..., "r") as input_file – otwiera plik źródłowy do odczytu.
# Możemy używać dwóch instrukcji with jedna wewnątrz drugiej.
# if job_title in line – sprawdza, czy szukany tekst występuje w danej linii.
# output_file.write(line) – zapisuje znalezioną linię do drugiego pliku.
# input_file i output_file to nazwy zmiennych reprezentujących otwarte pliki.