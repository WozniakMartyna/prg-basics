# Program wyświetla liczby od 1 do 30.
# Zamiast liczb podzielnych przez 3 wypisuje THREE,
# zamiast podzielnych przez 5 wypisuje FIVE,
# a zamiast podzielnych jednocześnie przez 3 i 5 – BINGO.

# for powtarza instrukcje dla kolejnych wartości zmiennej.
# range(1, 31) oznacza liczby od 1 do 30.
# Górna granica 31 nie jest uwzględniana.
for number in range(1, 31):

    # % oblicza resztę z dzielenia.
    # Jeśli reszta z dzielenia przez 3 i przez 5 wynosi 0, liczba jest podzielna przez obie te wartości.
    # and oznacza, że oba warunki muszą być prawdziwe.
    if number % 3 == 0 and number % 5 == 0:
        print('BINGO', end=' ')

    # elif sprawdza kolejny warunek, jeśli poprzedni był fałszywy.
    # Tutaj sprawdzamy podzielność przez 3.
    elif number % 3 == 0:
        print('THREE', end=' ')

    # Sprawdzamy podzielność przez 5.
    elif number % 5 == 0:
        print('FIVE', end=' ')

    # else wykonuje się, gdy żaden z wcześniejszych warunków nie pasuje.
    else:
        print(number, end=' ')

# end=' ' sprawia, że print() nie przechodzi do nowej linii,
# tylko oddziela kolejne wyniki spacją.

# Warunek sprawdzający podzielność przez 3 i 5 musi być pierwszy. Gdybyśmy najpierw sprawdzili samo 3, liczba 15 zostałaby oznaczona jako THREE, a nie BINGO.