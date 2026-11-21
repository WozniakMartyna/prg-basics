
# ZADANIE 3.12:
# Wyświetl elementy listy, które występują w niej tylko jeden raz.

# Tworzymy listę zawierającą powtarzające się liczby.
numbers = [2, 3, 2, 5, 8, 1, 9, 8]

# Tworzymy pustą listę, do której dodamy elementy występujące tylko raz.
unique_numbers = []

# Pętla for przechodzi kolejno przez wszystkie elementy listy.
for number in numbers:

    # count() zlicza, ile razy dana wartość występuje na liście.
    # Jeżeli wynik wynosi 1, oznacza to, że liczba występuje tylko raz.
    if numbers.count(number) == 1:

        # append() dodaje element na końcu listy wynikowej.
        unique_numbers.append(number)

# Wyświetlamy wynik.
print("Elementy występujące tylko raz:", unique_numbers)


# WYNIK:
# Elementy występujące tylko raz: [3, 5, 1, 9]


# NOTATKI:
# count() - zlicza wystąpienia podanej wartości na liście.
# Przykład: numbers.count(2) zwróci 2.
#
# == oznacza "jest równe".
# Sprawdzamy, czy liczba wystąpień wynosi dokładnie 1.
#
# append() - dodaje element na końcu listy.
#
# WAŻNE:
# Element unikalny w tym zadaniu oznacza element występujący dokładnie
# jeden raz, a nie po prostu element różniący się od pozostałych.
#
# Co się stanie, jeśli liczba wystąpi dwa razy?
# Odpowiedź: Nie zostanie dodana do listy wynikowej.