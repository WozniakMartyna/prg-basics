# ZADANIE 4.8:
# Wyświetlanie nazw plików, których rozszerzenie ma dokładnie 4 znaki.
# Do wyszukiwania używamy wyrażeń regularnych.

import re
# Importujemy moduł re do obsługi Regex.

file_name = "files.txt"

with open(file_name, "r", encoding="utf-8") as file:
    # Otwieramy plik files.txt w trybie odczytu ("r").

    for line in file:
        # Pętla for odczytuje plik linia po linii.
        # Przy każdym powtórzeniu zmienna line zawiera kolejną linię.

        file_name = line.strip()
        # strip() usuwa zbędne spacje i znak końca linii.
        # Dzięki temu nazwa pliku nie zawiera dodatkowego \n.

        pattern = r"\.[A-Za-z0-9]{4}$"
        # Tworzymy wzorzec Regex:
        # \.          - szukamy prawdziwej kropki przed rozszerzeniem.
        # [A-Za-z0-9] - dopuszczamy litery małe, wielkie i cyfry.
        # {4}         - wymagamy dokładnie czterech takich znaków.
        # $           - dopasowanie musi kończyć się na końcu tekstu.

        result = re.search(pattern, file_name)
        # re.search() sprawdza, czy nazwa pasuje do wzorca.

        if result:
            # Jeśli znaleziono dopasowanie, warunek jest prawdziwy.

            print(file_name)
            # Wyświetlamy nazwę pliku.


# do terminala
# cd "Rozwiązania/08/4.8"
# python filter_files.py