# ZADANIE 6: Obliczanie średniej arytmetycznej za pomocą pętli while.

# Tworzymy listę liczb.
numbers = [15, 8, 31, 47, 2, 19]

# Zmienna total przechowuje sumę liczb.
total = 0

# Zmienna i wskazuje indeks aktualnego elementu listy.
# Zaczynamy od indeksu 0, czyli pierwszego elementu.
i = 0

# Pętla działa, dopóki nie przejdziemy przez całą listę.
while i < len(numbers):

    # Dodajemy aktualny element do sumy.
    total += numbers[i]

    # Przechodzimy do następnego elementu.
    i += 1

# Obliczamy średnią, dzieląc sumę przez liczbę elementów.
average = total / len(numbers)

# Wyświetlamy wynik.
print("Suma liczb:", total)
print("Średnia arytmetyczna:", average)