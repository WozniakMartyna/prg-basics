# ZADANIE 1: Liczenie liczb parzystych na liście za pomocą pętli while.

# Tworzymy listę zawierającą liczby całkowite.
numbers = [34, 7, 19, 4, 21, 8]

# Zmienna count będzie przechowywać liczbę znalezionych liczb parzystych.
# Na początku nie znaleźliśmy jeszcze żadnej, dlatego ustawiamy 0.
count = 0

# Zmienna i będzie wskazywać indeks aktualnie sprawdzanego elementu.
# Indeksy listy zaczynają się od 0.
i = 0

# len(numbers) zwraca liczbę elementów znajdujących się na liście.
# Pętla działa tak długo, jak indeks i jest mniejszy od długości listy.
while i < len(numbers):

    # Sprawdzamy, czy aktualna liczba jest parzysta.
    # Operator % oblicza resztę z dzielenia.
    # Jeżeli reszta z dzielenia przez 2 wynosi 0, liczba jest parzysta.
    if numbers[i] % 2 == 0:

        # Zwiększamy licznik o 1.
        count += 1

    # Przechodzimy do następnego elementu listy.
    # To ważne, żeby pętla nie sprawdzała ciągle tego samego elementu.
    i += 1

# Wyświetlamy końcowy wynik.
print("Liczba parzystych elementów:", count)