# ZADANIE 3.20:
# Umieszczenie liczb parzystych przed nieparzystymi.

# Tworzymy przykładową listę liczb.
numbers = [7, 4, 9, 2, 8, 3, 6, 1]

# Tworzymy dwie puste listy.
even_numbers = []
odd_numbers = []

# Sprawdzamy kolejno wszystkie elementy.
for number in numbers:

    # Liczba jest parzysta, jeśli reszta z dzielenia przez 2 wynosi 0.
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        # Jeżeli warunek nie jest spełniony, liczba jest nieparzysta.
        odd_numbers.append(number)

# Łączymy obie listy.
# Operator + łączy zawartość dwóch list.
result = even_numbers + odd_numbers

# Wyświetlamy wynik.
print("Lista początkowa:", numbers)
print("Liczby parzyste i nieparzyste:", result)

# WYNIK:
# Lista początkowa: [7, 4, 9, 2, 8, 3, 6, 1]
# Liczby parzyste i nieparzyste: [4, 2, 8, 6, 7, 9, 3, 1]
#
# NOTATKI:
# % - operator reszty z dzielenia.
# number % 2 == 0 - sprawdza, czy liczba jest parzysta.
# else - wykonuje się, gdy warunek if nie jest spełniony.
# append() - dodaje element na końcu listy.
# + - łączy dwie listy w jedną.
#
# Ważne: kolejność liczb parzystych i nieparzystych
# wewnątrz swoich grup pozostaje taka sama jak na początku.