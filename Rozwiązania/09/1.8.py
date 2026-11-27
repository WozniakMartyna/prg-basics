# ZADANIE 09.1.8:
# Obniżenie cen produktów w sklepie odzieżowym o 10%.

# Program:
# 1. Wyświetla ceny przed obniżką.
# 2. Oblicza całkowitą wartość produktów przed obniżką.
# 3. Obniża każdą cenę o 10%.
# 4. Wyświetla nowe ceny.
# 5. Oblicza całkowitą wartość po obniżce.

# Słownik zawiera nazwy produktów i ich ceny.
price_list = {
    "T-shirt": 19.99,
    "Jeans": 49.99,
    "Jacket": 89.99,
    "Sneakers": 59.99,
    "Hat": 15.99
}

# Zmienna przechowująca sumę cen przed obniżką.
total_before = 0

print("PRICES BEFORE DISCOUNT")
print("======================")

# Wyświetlamy produkty i ich aktualne ceny.
for product, price in price_list.items():
    print(f"{product}: {price:.2f}")

    # Dodajemy cenę produktu do całkowitej wartości.
    total_before += price

print(f"Total before discount: {total_before:.2f}")

# Obniżamy każdą cenę o 10%.
# .items() pozwala pobrać nazwę produktu i jego cenę.
# list() tworzy listę par, dzięki czemu możemy bezpiecznie
# zmieniać wartości słownika podczas przechodzenia po parach.
for product, price in list(price_list.items()):

    # Cena po obniżce to 90% ceny początkowej.
    # round(..., 2) zaokrągla wynik do dwóch miejsc po przecinku.
    price_list[product] = round(price * 0.90, 2)

# Obliczamy sumę cen po obniżce.
total_after = 0

print("\nPRICES AFTER 10% DISCOUNT")
print("=========================")

# Wyświetlamy zmienione ceny.
for product, price in price_list.items():
    print(f"{product}: {price:.2f}")

    # Dodajemy nową cenę do sumy.
    total_after += price

print(f"Total after discount: {total_after:.2f}")

# price * 0.90 – pozostawia 90% ceny, czyli obniża ją o 10%.
# round(price, 2) – zaokrągla liczbę do dwóch miejsc po przecinku.
# list(price_list.items()) – tworzy listę par klucz–wartość. Dzięki temu możemy zmieniać słownik podczas przechodzenia po jego elementach.
# price_list[product] = ... – zmienia cenę przypisaną do danego produktu.
# :.2f – wyświetla liczbę z dokładnością do dwóch miejsc po przecinku.
# \n – rozpoczyna nową linię.