# Przekątną prostokąta obliczamy z twierdzenia Pitagorasa:
# d = sqrt{a^2+b^2}
# W zadaniu boki mają długości a = 5 i b = 8. Do obliczenia pierwiastka użyjemy funkcji sqrt() z modułu math.

# A program that calculates the length of the diagonal of a rectangle.
# Program oblicza długość przekątnej prostokąta.

# Importujemy moduł math, który zawiera funkcje matematyczne.
import math

# Ustalamy długość pierwszego boku prostokąta.
a = 5

# Ustalamy długość drugiego boku prostokąta.
b = 8

# Obliczamy przekątną według twierdzenia Pitagorasa.
# **2 oznacza podniesienie liczby do kwadratu.
# math.sqrt() oblicza pierwiastek kwadratowy.
diagonal = math.sqrt(a**2 + b**2)

# Wyświetlamy długość przekątnej.
print("The diagonal of the rectangle is:", diagonal)