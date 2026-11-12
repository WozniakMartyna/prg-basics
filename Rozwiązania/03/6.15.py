# W tym zadaniu sprawdzamy poprawność numeru produktu EAN-13.
# Poprawny numer musi składać się dokładnie z 13 cyfr.
# Jeżeli numer zaczyna się od 590, wyświetlamy informację o produkcie z Polski.

# input() pobiera numer produktu jako tekst.
# Przechowujemy go jako tekst, ponieważ chcemy sprawdzać jego długość i poszczególne znaki.
ean = input('Enter EAN-13 article number: ')

# len() zwraca liczbę znaków w tekście.
# isdigit() sprawdza, czy wszystkie znaki są cyframi.
# and oznacza, że oba warunki muszą być spełnione jednocześnie.
if len(ean) == 13 and ean.isdigit():
    print('Article number is correct')

    # startswith('590') sprawdza, czy numer rozpoczyna się od cyfr 590.
    if ean.startswith('590'):
        print('Article manufactured in Poland')
else:
    print('Incorrect article number')