# Celem zadania jest napisanie programu, który pobiera cenę produktu i wysokość rabatu w procentach, a następnie oblicza kwotę rabatu i cenę po obniżce.

# Program oblicza cenę produktu po uwzględnieniu rabatu.

# Pobieramy początkową cenę produktu.
# input() pobiera wpisaną wartość jako tekst.
price_string = input('Enter price: ')

# Zamieniamy tekst na liczbę zmiennoprzecinkową.
# float() pozwala wykonywać obliczenia na kwotach z częścią dziesiętną.
price = float(price_string)

# Pobieramy wysokość rabatu w procentach.
discount_string = input('Enter discount %: ')

# Zamieniamy wpisany rabat na liczbę.
discount = float(discount_string)

# Obliczamy kwotę obniżki.
# Mnożymy cenę przez wysokość rabatu i dzielimy przez 100.
reduction = price * discount / 100

# Obliczamy cenę po rabacie.
# Odejmujemy kwotę obniżki od ceny początkowej.
discounted_price = price - reduction

# Wyświetlamy cenę początkową z dwoma miejscami po przecinku.
# f"..." – tworzy f-string, czyli tekst, w którym można umieszczać wartości zmiennych w nawiasach {}.
# {price} – wstawia wartość zmiennej do f-stringa.
# :.2f oznacza wyświetlenie liczby z dokładnością do dwóch miejsc po przecinku.
print(f'Original price: {price:.2f}')

# Wyświetlamy wysokość rabatu w procentach.
print(f'Discount: {discount:.2f}%')

# Wyświetlamy cenę po obniżce.
print(f'Price with discount: {discounted_price:.2f}')

# Wyświetlamy kwotę, o którą zmniejszyła się cena.
print(f'Reduction: {reduction:.2f}')