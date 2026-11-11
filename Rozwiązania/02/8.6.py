# Program oblicza koszt przewiezienia towaru na podstawie odległości, ceny paliwa i spalania samochodu.
# Ilość potrzebnego paliwa: odległość / 100 * spalanie.
# Koszt przewozu: ilość potrzebnego paliwa * cena paliwa.

# Pobieramy odległość transportu w kilometrach.
# input() pobiera dane jako tekst.
# int() zamienia tekst na liczbę całkowitą.
distance = int(input('Enter distance in km: '))

# Pobieramy cenę jednego litra paliwa.
# float() zamienia tekst na liczbę, która może mieć część dziesiętną.
fuel_price = float(input('Enter fuel price per liter: '))

# Pobieramy spalanie samochodu na 100 kilometrów.
fuel_consumption = float(input('Enter fuel consumption per 100 km: '))

# Obliczamy ilość paliwa potrzebną na podaną odległość.
# Mnożymy odległość przez spalanie i dzielimy przez 100.
total_fuel_consumption = distance * fuel_consumption / 100

# Obliczamy całkowity koszt paliwa.
# Mnożymy potrzebną ilość paliwa przez cenę jednego litra.
total_cost = total_fuel_consumption * fuel_price

# Wyświetlamy ilość potrzebnego paliwa.
# F-string pozwala wstawiać wartości zmiennych do tekstu za pomocą {}.
# :.2f oznacza wyświetlenie liczby z dwoma miejscami po przecinku.
print(f'Total fuel consumption: {total_fuel_consumption:.2f} liters')

# Wyświetlamy całkowity koszt transportu.
print(f'Total transport cost: {total_cost:.2f}')