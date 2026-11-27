# ZADANIE 3:
# Skopiowanie zawartości pliku healthy_lifestyle.txt
# do pliku copy_healthy_lifestyle.txt.

# Nazwa pliku oryginalnego.
original_file = "healthy_lifestyle.txt"

# Nazwa pliku, w którym utworzymy kopię.
target_file = "copy_healthy_lifestyle.txt"

# Otwieramy oryginalny plik w trybie odczytu ("r").
with open(original_file, "r") as file:

    # read() odczytuje całą zawartość pliku jako jeden tekst.
    content = file.read()

# Otwieramy plik docelowy w trybie zapisu ("w").
# Jeśli plik nie istnieje, zostanie utworzony.
# Jeśli istnieje, jego wcześniejsza zawartość zostanie nadpisana.
with open(target_file, "w") as file:

    # Zapisujemy odczytaną wcześniej zawartość w nowym pliku.
    file.write(content)

# Wyświetlamy informację o zakończeniu kopiowania.
print(f"File has been copied to {target_file}.")

# w terminalu:
# cd "Rozwiązania/08/2.3"
# python copy_file.py


# original_file – nazwa pliku źródłowego, z którego pobieramy dane.
# target_file – nazwa pliku docelowego, do którego zapisujemy dane.
# read() – pobiera całą zawartość pliku.
# content – przechowuje odczytany tekst.
# write(content) – zapisuje ten tekst do drugiego pliku.
# "r" – odczyt, "w" – zapis.