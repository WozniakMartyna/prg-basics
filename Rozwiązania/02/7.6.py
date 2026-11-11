# Program sprawdza, czy prędkość pojazdu na autostradzie mieści się w zakresie od 40 do 140 km/h włącznie.

# Pobieramy prędkość od użytkownika.
# input() pobiera wartość jako tekst.
# int() zamienia tekst na liczbę całkowitą.
speed = int(input('Enter vehicle speed: '))

# Sprawdzamy, czy prędkość jest większa lub równa 40
# ORAZ jednocześnie mniejsza lub równa 140.
# >= oznacza "większe lub równe".
# <= oznacza "mniejsze lub równe".
# and oznacza "i" – oba warunki muszą być prawdziwe.
speed_is_valid = speed >= 40 and speed <= 140

# Wyświetlamy informację, czy prędkość jest prawidłowa.
# F-string pozwala wstawić wartość zmiennej do tekstu za pomocą {}.
print(f'Speed is valid: {speed_is_valid}')