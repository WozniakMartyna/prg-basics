# ZADANIE 8: Funkcja zwracająca tekst składający się z n gwiazdek.

# Definiujemy funkcję o nazwie star.
# Parametr n określa, ile gwiazdek ma zawierać zwracany tekst.
def star(n):

    # Operator * powiela tekst n razy.
    # Przykładowo "*" * 3 daje "***".
    return "*" * n


# Tworzymy listę określającą liczbę gwiazdek w kolejnych wierszach.
numbers = [2, 6, 4, 9, 7]

# Przechodzimy przez liczby z listy.
for number in numbers:

    # Wywołujemy funkcję star() i wyświetlamy zwrócony tekst.
    print(star(number))

# DODATKOWE NOTATKI:
#
# def - słowo kluczowe służące do tworzenia funkcji.
#
# n - parametr funkcji, czyli informacja przekazywana do funkcji.
#
# return - zwraca wynik działania funkcji.
# Po wykonaniu return funkcja kończy swoje działanie.
#
# Przykład:
# star(3) zwróci tekst "***".
#
# Operator * może powielać tekst:
# "A" * 3 daje "AAA".