# Program pobiera kod SWIFT i wyświetla kod banku oraz kod kraju.
# Kod SWIFT ma zazwyczaj 8 lub 11 znaków:
# Pierwsze 4 znaki – kod banku.
# Kolejne 2 znaki – kod kraju.
# Kolejne 2 znaki – kod lokalizacji.
# Ostatnie 3 znaki – opcjonalny kod oddziału.

# Pobieramy kod SWIFT od użytkownika.
# input() pobiera wpisany kod jako tekst.
swift = input('Enter SWIFT code: ')

# Pobieramy pierwsze cztery znaki kodu SWIFT.
# [0:4] oznacza znaki od indeksu 0 do indeksu 3.
bank_code = swift[0:4]

# Pobieramy piąty i szósty znak kodu SWIFT.
# [4:6] oznacza znaki o indeksach 4 i 5.
country_code = swift[4:6]

# Wyświetlamy kod banku.
# F-string pozwala wstawić wartość zmiennej do tekstu za pomocą {}.
print(f'Bank Code: {bank_code}')

# Wyświetlamy kod kraju.
print(f'Country Code: {country_code}')

# Przykładowe uruchomienie programu dla kodu SWIFT:
# BPKOPLPW: Bank Code: BPKO, Country Code: PL
# CHASUS33: Bank Code: CHAS, Country Code: US
# DEUTDEFF: Bank Code: DEUT, Country Code: DE