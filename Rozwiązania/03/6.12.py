# W tym zadaniu obliczamy kwotę do zapłaty za zakupione produkty.
# Jeżeli klient kupi więcej niż dwa produkty, każdy kolejny produkt otrzymuje rabat 25%.

# input() pobiera dane wpisane przez użytkownika.
# int() zamienia liczbę produktów na liczbę całkowitą.
number_of_products = int(input('Number of products purchased: '))

# float() zamienia cenę produktu na liczbę zmiennoprzecinkową,
# dzięki czemu możemy podać również cenę z groszami.
product_price = float(input('Product price: '))

# Jeżeli kupiono najwyżej dwa produkty, nie naliczamy rabatu.
if number_of_products <= 2:
    amount_to_pay = number_of_products * product_price
else:
    # Dwa pierwsze produkty mają pełną cenę.
    # Pozostałe produkty kosztują 75% ceny, ponieważ odjęto rabat 25%.
    amount_to_pay = 2 * product_price + (number_of_products - 2) * product_price * 0.75

# F-string wstawia obliczoną kwotę do tekstu.
# :.2f oznacza wyświetlenie kwoty z dokładnością do dwóch miejsc po przecinku.
print(f'Amount to pay: {amount_to_pay:.2f}')