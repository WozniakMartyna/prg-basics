# W tym zadaniu sprawdzamy, czy cena produktu została obniżona o co najmniej 10%.
# Porównujemy aktualną cenę produktu z jego poprzednią ceną.

current_price = 140.00  # Aktualna cena produktu.
previous_price = 200.00  # Poprzednia cena produktu.

# Obliczamy procentową obniżkę ceny.
# Odejmujemy aktualną cenę od poprzedniej, dzielimy przez poprzednią cenę i mnożymy przez 100.
price_reduction = (previous_price - current_price) / previous_price * 100

# Sprawdzamy, czy obniżka wynosi co najmniej 10%.
if price_reduction >= 10:
    print('Buy the product!!')
    # f-string pozwala wstawić wartość zmiennej do tekstu za pomocą nawiasów klamrowych {}.
    # :.0f oznacza wyświetlenie wyniku bez miejsc po przecinku.
    print(f'Product price reduced by {price_reduction:.0f}%')
else:
    print('Price reduction is less than 10%')