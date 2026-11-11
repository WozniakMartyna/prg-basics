# Program sprawdza, czy numer rejestracyjny samochodu rozpoczyna się od KR lub KK, czyli oznaczeń podanych w zadaniu dla Krakowa.

# Pobieramy numer rejestracyjny od użytkownika.
# input() pobiera wpisany numer jako tekst.
car_number = input('Enter car registration number: ')

# Pobieramy dwa pierwsze znaki numeru rejestracyjnego.
# [0:2] oznacza znaki o indeksach 0 i 1.
first_two_letters = car_number[0:2]

# Sprawdzamy, czy dwie pierwsze litery to KR lub KK.
# == sprawdza, czy wartości są równe.
# or oznacza "lub" – wystarczy, że jeden warunek jest prawdziwy.
is_krakow = first_two_letters == "KR" or first_two_letters == "KK"

# Wyświetlamy wynik sprawdzenia.
# F-string pozwala wstawić wartość zmiennej do tekstu za pomocą {}.
print(f'Car is from Krakow: {is_krakow}')