# ZADANIE: Wyświetl listę zakupów.
#
# Każdy produkt powinien zostać wyświetlony w osobnej linii.
# Do przejścia przez wszystkie elementy listy wykorzystujemy pętlę for.


# Tworzymy listę o nazwie shopping_list.
# Lista zawiera teksty (napisy), dlatego każdy produkt
# zapisujemy w cudzysłowie.
shopping_list = [
    "milk",
    "bread",
    "eggs",
    "butter",
    "cheese",
    "tomatoes",
    "potatoes",
    "carrots",
    "onions",
    "garlic"
]


# Rozpoczynamy pętlę for.
# item to zmienna, która w każdym obiegu przechowuje
# kolejny element listy shopping_list.
#
# Pierwszy obieg: item = "milk".
# Drugi obieg: item = "bread".
# Trzeci obieg: item = "eggs".
# I tak dalej, aż do ostatniego produktu.
for item in shopping_list:

    # Wyświetlamy aktualny produkt.
    # print() domyślnie przechodzi do nowej linii po wyświetleniu tekstu.
    print(item)