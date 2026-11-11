# Program pobiera symbol rozmiaru ubrania i wyświetla jego opis.

# input() pobiera tekst wpisany przez użytkownika.
size = input('Enter size symbol: ')

# Sprawdzamy, czy użytkownik wpisał rozmiar S.
# == sprawdza, czy dwie wartości są takie same.
if size == 'S':
    print('S: Small size')

# Jeśli poprzedni warunek był fałszywy, sprawdzamy rozmiar M.
elif size == 'M':
    print('M: Medium size')

# Sprawdzamy rozmiar L.
elif size == 'L':
    print('L: Large size')

# Sprawdzamy rozmiar XL.
elif size == 'XL':
    print('XL: Extra large size')

# Jeśli żaden z symboli nie pasuje, wyświetlamy informację o błędzie.
else:
    print('Incorrect symbol')

# if sprawdza pierwszy symbol.
# elif sprawdza kolejne symbole, jeśli wcześniejsze nie pasowały.
# else obsługuje wszystkie pozostałe przypadki.