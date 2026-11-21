# ZADANIE: Przygotuj raport temperatur z miesiąca marca.
# Oblicz liczbę pomiarów, średnią, minimum, maksimum
# oraz liczbę dni z temperaturą poniżej zera.

# Tworzymy listę temperatur zmierzonych w kolejnych dniach marca.
# Każdy element listy oznacza temperaturę jednego dnia.
temperatures = [
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]


# 1. Obliczamy liczbę pomiarów.
# len() zwraca liczbę elementów listy.
# W marcu mamy 30 pomiarów.
measurements = len(temperatures)


# 2. Obliczamy średnią temperaturę.
# Zmienna temp_total będzie przechowywać sumę wszystkich temperatur.
# Na początku suma wynosi 0.
temp_total = 0

# Pętla for przechodzi przez wszystkie temperatury.
# Zmienna temp przechowuje aktualnie sprawdzaną temperaturę.
for temp in temperatures:

    # Dodajemy aktualną temperaturę do sumy.
    # Operator += oznacza dodanie wartości do dotychczasowej wartości zmiennej.
    temp_total += temp

# Średnia to suma wszystkich temperatur podzielona przez liczbę pomiarów.
avg_temp = temp_total / measurements


# 3. Obliczamy temperaturę minimalną i maksymalną.
# min() zwraca najmniejszą wartość z listy.
min_temp = min(temperatures)

# max() zwraca największą wartość z listy.
max_temp = max(temperatures)


# 4. Obliczamy liczbę dni z temperaturą ujemną.
# Tworzymy licznik, który na początku wynosi 0.
negative_temp = 0

# Zmienna i przechowuje indeks aktualnie sprawdzanej temperatury.
# Zaczynamy od indeksu 0.
i = 0

# Pętla while działa, dopóki i jest mniejsze od liczby pomiarów.
while i < measurements:

    # temperatures[i] pobiera temperaturę z aktualnej pozycji listy.
    # Sprawdzamy, czy temperatura jest mniejsza od 0.
    if temperatures[i] < 0:

        # Jeżeli temperatura jest ujemna, zwiększamy licznik o 1.
        negative_temp += 1

    # Przechodzimy do następnego elementu listy.
    i += 1


# 5. Wyświetlamy raport temperatur.
print("TEMPERATURE REPORT")
print("==================")
print("Month: March")
print("Number of measurements:", measurements)
print("Average temperature in the month:", round(avg_temp, 2))
print("Minimum temperature:", min_temp)
print("Maximum temperature:", max_temp)
print("Number of days with negative temperature:", negative_temp)