
# ZADANIE 4.6:
# Program oblicza liczbę linii, znaków i słów w wybranym pliku.
# Wykorzystujemy try-except, aby obsłużyć sytuację,
# w której użytkownik poda nazwę nieistniejącego pliku.

file_name = input("File name: ")
# input() wyświetla pytanie i czeka na odpowiedź użytkownika.
# Wpisana nazwa zostaje zapisana jako tekst (string).

try:
    # W bloku try umieszczamy kod, podczas wykonywania którego
    # może wystąpić błąd.
    # W tym zadaniu może nie istnieć plik o podanej nazwie.

    with open(file_name, "r", encoding="utf-8") as file:
        # open() otwiera wskazany plik.
        # file_name - nazwa pliku podana przez użytkownika.
        # "r" - tryb odczytu (read).
        # encoding="utf-8" - poprawne odczytywanie różnych znaków.
        # with automatycznie zamknie plik po zakończeniu pracy.

        text = file.read()
        # read() odczytuje całą zawartość pliku.
        # Zapisujemy ją w zmiennej text jako jeden długi tekst.

    lines = text.splitlines()
    # splitlines() dzieli tekst na osobne linie.
    # Zwraca listę, w której każda linia jest osobnym elementem.
    # Przykład: "Ala\nma\nkota" -> ["Ala", "ma", "kota"].

    words = text.split()
    # split() dzieli tekst na słowa.
    # Domyślnie rozdziela tekst w miejscach białych znaków,
    # czyli spacji, tabulatorów i znaków nowej linii.
    # Przykład: "Ala ma kota" -> ["Ala", "ma", "kota"].

    characters = len(text)
    # len() zwraca liczbę elementów.
    # Dla tekstu oznacza to liczbę znaków.
    # Liczymy również spacje, przecinki i znaki nowej linii.

    print("Number of lines:", len(lines))
    # len(lines) oblicza liczbę elementów listy linii.

    print("Number of characters:", characters)
    # Wyświetlamy wcześniej obliczoną liczbę znaków.

    print("Number of words:", len(words))
    # len(words) oblicza liczbę elementów listy słów.

except FileNotFoundError:
    # Ten blok wykona się tylko wtedy, gdy wskazany plik nie istnieje.
    # Program nie zakończy się komunikatem Traceback.

    print("Error: file does not exist.")

except PermissionError:
    # Ten blok obsługuje sytuację, w której nie mamy uprawnień
    # do odczytania wybranego pliku.

    print("Error: permission denied.")


# do terminala:
# cd "Rozwiązania/08/4.6"
# python count_file.py

# try - Blok, w którym próbujemy wykonać kod
# except - Blok obsługujący błąd
# read() - Odczytuje całą zawartość pliku
# splitlines() - Dzieli tekst na linie
# split() - Dzieli tekst na słowa
# len() - Liczy elementy lub znaki
# input() - Pobiera tekst od użytkownika
# with open() - Otwiera plik i automatycznie go zamyka