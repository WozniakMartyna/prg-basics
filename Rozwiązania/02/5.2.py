# Sześcian ma wszystkie boki równej długości. Program pobiera długość boku z klawiatury i oblicza:
# Objętość: V = a^3
# Pole powierzchni: P = 6a^2

# A program to calculate the volume and surface area of a cube.
# Program oblicza objętość i pole powierzchni sześcianu.

# Pytamy użytkownika o długość boku sześcianu.
# input() pobiera wpisaną wartość jako tekst.
cube_side_string = input('Enter cube side: ')

# Zamieniamy tekst na liczbę całkowitą za pomocą int().
cube_side = int(cube_side_string)

# Obliczamy objętość sześcianu.
# **3 oznacza podniesienie długości boku do trzeciej potęgi.
cube_volume = cube_side ** 3

# Obliczamy pole powierzchni sześcianu.
# **2 oznacza podniesienie długości boku do kwadratu.
# Mnożymy wynik przez 6, ponieważ sześcian ma 6 ścian.
cube_surface_area = 6 * cube_side ** 2

# Wyświetlamy obliczoną objętość.
# f"..." – tworzy f-string, czyli tekst, w którym można umieszczać wartości zmiennych w nawiasach {}.
# {cube_side}, {cube_volume} – wstawiają wartości zmiennych do f-stringa.
print(f'The volume of a cube with side {cube_side} is {cube_volume}')

# Wyświetlamy obliczone pole powierzchni.
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')