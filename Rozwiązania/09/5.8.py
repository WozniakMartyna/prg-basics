# ZADANIE 5.8:
# Obliczenie całkowitego kosztu zakupów na podstawie cen i ilości.

# Słownik zawierający ceny produktów.
prices = {
    'milk': 1.49,
    'butter': 2.09,
    'juice': 1.19,
    'bread': 1.99
}

# Słownik zawierający produkty i ich ilości w koszyku.
cart = {
    'juice': 3,
    'bread': 1,
    'milk': 2
}

# Zmienna przechowująca całkowity koszt zakupów.
total_cost = 0

# Przechodzimy po produktach znajdujących się w koszyku.
for product, quantity in cart.items():

    # Pobieramy cenę produktu ze słownika prices.
    price = prices[product]

    # Mnożymy cenę przez ilość i dodajemy do sumy.
    total_cost += price * quantity

# :.2f wyświetla wynik z dokładnością do dwóch miejsc po przecinku.
print(f"Total cost: {total_cost:.2f}")


# cart.items() – pobiera nazwę produktu i jego ilość.
# prices[product] – pobiera cenę produktu z drugiego słownika.
# price * quantity – oblicza koszt danego produktu.
# :.2f – formatuje liczbę do dwóch miejsc po przecinku.