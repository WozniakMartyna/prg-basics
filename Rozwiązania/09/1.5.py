# ZADANIE 1.5:
# Utworzenie listy pięciu krajów wraz z ich populacją.

# Lista może przechowywać różne obiekty, również słowniki.
# Każdy słownik opisuje jeden kraj.
countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83000000},
    {"name": "France", "population": 68000000},
    {"name": "Spain", "population": 48000000},
    {"name": "Italy", "population": 59000000}
]

# Nagłówek tabeli.
print("COUNTRY\t\tPOPULATION")
print("==============================")

# Przechodzimy po wszystkich słownikach znajdujących się na liście.
for country in countries:

    # Pobieramy wartości za pomocą odpowiednich kluczy.
    name = country["name"]
    population = country["population"]

    # \t oznacza tabulator, czyli odstęp między kolumnami.
    print(f"{name}\t\t{population}")

# countries – lista słowników.
# for country in countries – pobiera kolejno każdy słownik z listy.
# country["name"] – odczytuje nazwę kraju.
# country["population"] – odczytuje populację.
# \t – wstawia tabulator.