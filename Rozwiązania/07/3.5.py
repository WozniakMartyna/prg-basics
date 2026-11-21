# ZADANIE 5: Obliczanie średniej arytmetycznej za pomocą pętli for.

# Tworzymy listę liczb.
numbers = [15, 8, 31, 47, 2, 19]

# Zmienna total będzie przechowywać sumę liczb.
total = 0

# Przechodzimy przez wszystkie elementy listy.
for number in numbers:

    # Dodajemy aktualną liczbę do sumy.
    total += number

# Obliczamy średnią.
# Dzielimy sumę przez liczbę elementów listy.
average = total / len(numbers)

# Wyświetlamy sumę i średnią.
print("Suma liczb:", total)
print("Średnia arytmetyczna:", average)