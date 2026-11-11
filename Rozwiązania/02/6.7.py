# Program wyświetla kod liczbowy każdej litery imienia.

# Zapisujemy imię w zmiennej name.
name = 'Martyna'

# Pętla for przechodzi kolejno przez wszystkie znaki tekstu name.
# Zmienna letter przechowuje aktualnie sprawdzaną literę.
for letter in name:

    # Funkcja ord() zamienia aktualną literę na jej kod liczbowy.
    # F-string pozwala wstawić literę i jej kod do tekstu za pomocą {}.
    print(f'The letter {letter} has a code {ord(letter)}')

# Pętla for wykonuje instrukcje dla kolejnych znaków tekstu.
# W tym programie:
# 1. Najpierw zmienna letter otrzymuje wartość M.
# 2. Program wyświetla literę i jej kod.
# 3. Następnie letter otrzymuje wartość a.
# 4. Program ponownie wyświetla literę i jej kod.
# 5. Dzieje się tak aż do przejścia przez wszystkie litery imienia.
# Wcięcie przed instrukcją print() oznacza, że należy ona do pętli for.