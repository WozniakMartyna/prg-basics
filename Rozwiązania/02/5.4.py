# Celem zadanie jest napisanie programu, który pobiera kwotę od użytkownika i oblicza podatek VAT w wysokości 23%.

# Pobieramy kwotę od użytkownika.
# input() pobiera wpisaną wartość jako tekst.
amount_string = input('Enter amount: ')

# Zamieniamy tekst na liczbę zmiennoprzecinkową.
# float() pozwala używać kwot z częścią dziesiętną.
amount = float(amount_string)

# Obliczamy podatek VAT.
# 0.23 oznacza 23%, ponieważ 23 / 100 = 0.23.
vat = amount * 0.23

# Wyświetlamy kwotę.
# f"..." – tworzy f-string, czyli tekst, w którym można umieszczać wartości zmiennych w nawiasach {}.
# {amount} – wstawia wartość zmiennej do f-stringa.
# :.2f oznacza wyświetlenie liczby z dokładnością do dwóch miejsc po przecinku.
print(f'Amount: {amount:.2f}')

# Wyświetlamy obliczony podatek VAT.
print(f'VAT 23%: {vat:.2f}')