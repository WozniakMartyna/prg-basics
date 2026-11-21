# ZADANIE: Oblicz całkowitą wartość produktów znajdujących się w sklepie.
#
# Mamy dwie listy:
# product_prices – ceny poszczególnych produktów.
# product_quantities – liczba sztuk poszczególnych produktów.
#
# Cena i ilość produktu znajdują się na tej samej pozycji obu list.

# Lista zawierająca ceny 10 produktów.
# Liczby dziesiętne zapisujemy z kropką, a nie przecinkiem.
product_prices = [
    2999.99, 149.99, 499.99, 89.99, 1199.99,
    349.99, 189.99, 99.99, 249.99, 999.99
]

# Lista zawierająca liczbę dostępnych sztuk każdego produktu.
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]


# Tworzymy zmienną total_value, która będzie przechowywać
# łączną wartość wszystkich produktów.
# Na początku suma wynosi 0.
total_value = 0

# Zmienna i będzie przechowywać indeks aktualnego produktu.
# Zaczynamy od 0, ponieważ pierwszy element listy ma indeks 0.
i = 0

# Pętla while przechodzi przez wszystkie produkty.
# len(product_prices) zwraca liczbę produktów, czyli 10.
while i < len(product_prices):

    # Pobieramy cenę produktu o aktualnym indeksie.
    price = product_prices[i]

    # Pobieramy liczbę sztuk tego samego produktu.
    quantity = product_quantities[i]

    # Obliczamy wartość produktu:
    # cena jednej sztuki pomnożona przez liczbę dostępnych sztuk.
    product_value = price * quantity

    # Dodajemy wartość aktualnego produktu do całkowitej wartości sklepu.
    total_value += product_value

    # Zwiększamy indeks, aby przejść do następnego produktu.
    i += 1


# Wyświetlamy całkowitą wartość produktów.
# round(total_value, 2) zaokrągla wynik do dwóch miejsc po przecinku.
print("Total value of products:", round(total_value, 2))