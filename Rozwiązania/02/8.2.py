# Program ma obliczyć pole powierzchni i obwód koła na podstawie podanego promienia.

# Ustalamy promień koła.
# Możemy zmienić tę wartość, aby sprawdzić program dla innych danych.
r = 3

# Ustalamy przybliżoną wartość liczby pi.
# Liczba pi jest potrzebna do obliczenia pola i obwodu koła.
pi = 3.14

# Obliczamy pole powierzchni koła.
# ** oznacza potęgowanie.
# r ** 2 oznacza promień pomnożony przez samego siebie.
area = pi * r ** 2

# Obliczamy obwód koła.
circumference = 2 * pi * r

# Wyświetlamy obliczone pole powierzchni.
# F-string pozwala wstawiać wartości zmiennych do tekstu za pomocą {}.
print(f'Area: {area}')

# Wyświetlamy obliczony obwód.
print(f'Circumference: {circumference}')