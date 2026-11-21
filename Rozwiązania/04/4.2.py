# ZADANIE 4.2
# Należy zapoznać się z tym, czym są funkcje w Pythonie.
# Funkcja to fragment kodu, który można uruchamiać wielokrotnie.
# W tym przykładzie tworzymy funkcję dodającą dwie liczby,
# a następnie wywołujemy ją i wyświetlamy wynik.

# def służy do definiowania, czyli tworzenia funkcji.
# add to nazwa funkcji.
# a i b to parametry, czyli wartości przekazywane do funkcji.
def add(a, b):

    # return zwraca wynik działania funkcji.
    # W tym przypadku zwracamy sumę dwóch parametrów.
    return a + b

# Wywołujemy funkcję add(), przekazując jej liczby 3 i 5.
# Wynik funkcji zapisujemy w zmiennej result.
result = add(3, 5)

# print() wyświetla wynik na ekranie.
print('Result:', result)

# Możemy wywołać tę samą funkcję ponownie z innymi liczbami.
print('Another result:', add(10, 7))

# Ważne pojęcia:
# def - rozpoczyna definicję funkcji.
# add - nazwa funkcji, którą sami wybieramy.
# a, b - parametry funkcji.
# return - zwraca wynik i kończy działanie funkcji.
# add(3, 5) - wywołanie funkcji z argumentami 3 i 5.
#
# Parametr to nazwa używana w definicji funkcji (np. a, b).
# Argument to konkretna wartość przekazana podczas wywołania (np. 3, 5).
#
# - Co się stanie, jeśli usuniemy return? Funkcja nie zwróci wyniku
#   (domyślnie zwróci None).
# - Czy można zmienić nazwę add? Tak, można użyć innej nazwy,
#   pamiętając, aby zmienić ją również przy wywołaniu.