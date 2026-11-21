# ZADANIE 3.19:
# Policzenie liczb większych od wartości podanej przez użytkownika.

# Tworzymy listę liczb rzeczywistych.
numbers = [2.5, 7.8, 1.2, 9.4, 5.6, 3.1]

# Pobieramy liczbę od użytkownika.
# float() zamienia wpisany tekst na liczbę rzeczywistą.
value = float(input("Podaj wartość: "))

# Zmienna count przechowuje liczbę znalezionych elementów.
count = 0

# Sprawdzamy kolejno wszystkie liczby z listy.
for number in numbers:

    # Sprawdzamy, czy aktualna liczba jest większa od podanej wartości.
    if number > value:
        count += 1  # Zwiększamy licznik o 1.

# Wyświetlamy wynik.
print("Liczba elementów większych od podanej wartości:", count)

# PRZYKŁAD:
# Dla wartości 5 wynik wynosi 3.
#
# NOTATKI:
# float() - zamienia tekst na liczbę rzeczywistą, np. "2.5" na 2.5.
# > - sprawdza, czy lewa wartość jest większa od prawej.
# count += 1 - zwiększa licznik o jeden.
# Pętla for pozwala sprawdzić każdy element listy.