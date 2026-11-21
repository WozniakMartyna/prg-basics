# ZADANIE: Znajdź kategorię, na którą wydano najwięcej pieniędzy.
#
# Mamy dwie listy:
# categories – nazwy kategorii wydatków.
# expenses – kwoty wydane w poszczególnych kategoriach.
#
# Elementy na tych samych pozycjach są ze sobą powiązane.

# Lista zawierająca nazwy kategorii wydatków.
categories = ["Food", "Transport", "Rent", "Entertainment"]

# Lista zawierająca kwoty wydane w poszczególnych kategoriach.
expenses = [500, 150, 1000, 200]


# max() znajduje największą wartość w liście expenses.
max_expense = max(expenses)

# index() zwraca indeks pierwszego wystąpienia podanej wartości.
# Szukamy pozycji, na której znajduje się największy wydatek.
max_index = expenses.index(max_expense)


# Korzystamy z tego samego indeksu w obu listach.
# expenses[max_index] pobiera największą kwotę.
# categories[max_index] pobiera nazwę kategorii odpowiadającą tej kwocie.
print("Most expensive category:", categories[max_index])
print("Expense:", expenses[max_index])