
# ZADANIE 4.4:
# Wyświetlanie zawartości pliku CSV po pięć linii.
# Po każdej grupie program czeka na naciśnięcie klawisza Enter.

file_name = "it_company.csv"

# Otwieramy plik w trybie odczytu ("r").
# encoding="utf-8" pozwala poprawnie odczytywać różne znaki.
# with automatycznie zamknie plik po zakończeniu pracy.
with open(file_name, "r", encoding="utf-8") as file:

    lines = file.readlines()
    # readlines() odczytuje wszystkie linie pliku.
    # Zwraca listę, w której każda linia jest osobnym elementem.
    # Przykładowo:
    # lines[0] - pierwsza linia,
    # lines[1] - druga linia,
    # lines[2] - trzecia linia itd.

    # range() tworzy kolejne wartości indeksów.
    # 0 - zaczynamy od pierwszego elementu listy,
    # len(lines) - liczba wszystkich linii,
    # 5 - zwiększamy indeks o 5 przy każdym powtórzeniu.
    #
    # Dzięki temu i przyjmuje wartości: 0, 5, 10, 15, 20...
    for i in range(0, len(lines), 5):

        # Pobieramy maksymalnie 5 kolejnych linii.
        # lines[i:i + 5] oznacza:
        # rozpocznij od indeksu i i pobierz elementy do i+5,
        # ale bez uwzględniania końcowego indeksu.
        #
        # Przykład:
        # i = 0  -> elementy 0, 1, 2, 3, 4
        # i = 5  -> elementy 5, 6, 7, 8, 9
        # i = 10 -> elementy 10, 11, 12, 13, 14
        for line in lines[i:i + 5]:

            print(line, end="")
            # Wyświetlamy aktualną linię.
            # end="" oznacza, że print() nie dodaje własnego
            # znaku nowej linii na końcu.
            # Odczytana linia zazwyczaj ma już znak \n.

        # Sprawdzamy, czy zostały jeszcze jakieś linie do wyświetlenia.
        if i + 5 < len(lines):

            input("Press Enter key...")
            # input() wyświetla komunikat i czeka na wpisanie danych.
            # W tym przypadku wystarczy nacisnąć Enter.
            # Program zatrzyma się tutaj do momentu naciśnięcia Enter.


# do terminala
# cd "Rozwiązania/08/4.4"
# python display_csv.py

# readlines() tworzy listę wszystkich linii.
# range(..., 5) pozwala pobierać kolejne grupy po pięć elementów. Jeżeli plik ma nagłówek, on również jest liczony jako jedna z linii.