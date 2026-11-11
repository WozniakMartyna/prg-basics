# Samochód ma trzy tryby jazdy:
# Auto; Symbol:	A; Zużycie na 100 km: 7 litrów
# Manual; Symbol: M; Zużycie na 100 km: 9 litrów
# Eco; Symbol: E; Zużycie na 100 km: 6 litrów
# Wzór na zużycie paliwa: zużycie = (dystans / 100) * zużycie_na_100_km

# Program oblicza zużycie paliwa na podstawie trybu jazdy i dystansu.

# input() pobiera wybrany tryb jazdy jako tekst.
driving_mode = input('Enter driving mode (A/M/E): ')

# input() pobiera dystans.
# int() zamienia wpisany tekst na liczbę całkowitą.
distance = int(input('Enter distance in km: '))

# Sprawdzamy, jaki tryb jazdy wybrał użytkownik.
if driving_mode == 'A':
    fuel_consumption = 7  # Auto: 7 litrów na 100 km.
elif driving_mode == 'M':
    fuel_consumption = 9  # Manual: 9 litrów na 100 km.
elif driving_mode == 'E':
    fuel_consumption = 6  # Eco: 6 litrów na 100 km.
else:
    # Jeśli użytkownik wpisał nieprawidłowy symbol, wyświetlamy komunikat.
    print('Incorrect driving mode')
    fuel_consumption = 0

# Obliczamy całkowite zużycie paliwa.
# Mnożymy dystans przez spalanie i dzielimy przez 100.
total_consumption = distance * fuel_consumption / 100

# f-string pozwala wstawiać wartości zmiennych do tekstu za pomocą {}.
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')

# w tej wersji program obsługuje nieprawidłowy symbol, ale wyświetli wtedy zużycie 0 litrów.
# Sprawdzanie dla wyników:
# Dystans = 200 km, Tryb = M, Zużycie = 18 litrów
# Dystans = 400 km, Tryb = A, Zużycie = 28 litrów
# Dystans = 350 km, Tryb = E, Zużycie = 21 litrów