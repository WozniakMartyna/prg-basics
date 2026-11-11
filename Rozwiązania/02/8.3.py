# Program pobiera temperaturę w stopniach Celsjusza, a następnie przelicza ją na Kelwiny i stopnie Fahrenheita.

# Wzory
# Kelwiny: K = C + 273.15
# Fahrenheity: F = C * (9/5) + 32

# KROK 1: Pobieramy temperaturę w stopniach Celsjusza.
# input() pobiera wartość jako tekst.
# float() zamienia tekst na liczbę, która może mieć część dziesiętną.
celsius = float(input('Enter temperature in Celsius: '))

# KROK 2: Przeliczamy temperaturę na Kelwiny.
# Do temperatury w Celsjuszach dodajemy 273.15.
kelvin = celsius + 273.15

# KROK 3: Przeliczamy temperaturę na stopnie Fahrenheita.
# Mnożymy temperaturę przez 9, dzielimy przez 5 i dodajemy 32.
fahrenheit = celsius * 9 / 5 + 32

# KROK 4: Wyświetlamy temperaturę w stopniach Celsjusza.
# F-string pozwala wstawiać wartości zmiennych do tekstu za pomocą {}.
# :.2f oznacza wyświetlenie dwóch miejsc po przecinku.
print(f'Temperature in Celsius: {celsius:.2f}')

# KROK 5: Wyświetlamy temperaturę w Kelwinach.
print(f'Temperature in Kelvin: {kelvin:.2f}')

# KROK 6: Wyświetlamy temperaturę w stopniach Fahrenheita.
print(f'Temperature in Fahrenheit: {fahrenheit:.2f}')