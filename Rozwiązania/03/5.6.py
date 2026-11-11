# W tym zadaniu zamieniamy pętlę for na pętlę while.
# Program oblicza sumę liczb parzystych od 1 do N.

N = 10  # Ustalamy górną granicę zakresu.
sum_even = 0  # Zmienna przechowuje sumę liczb parzystych.
i = 1  # Zmienna i ustawia pierwszą sprawdzaną liczbę.

# Pętla działa, dopóki i jest mniejsze lub równe N.
while i <= N:
    # Sprawdzamy, czy liczba jest parzysta.
    # Reszta z dzielenia liczby parzystej przez 2 wynosi 0.
    if i % 2 == 0:
        sum_even += i  # Dodajemy aktualną parzystą liczbę do sumy.

    i += 1  # zwiększa i o jeden, żeby pętla mogła przejść do kolejnej liczby i w końcu się zakończyć. Przechodzimy do następnej liczby.

print(f"The sum of even numbers from 1 to {N} is: {sum_even}") # F-string wstawia wartości zmiennych N i sum_even do tekstu.