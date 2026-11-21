
# ZADANIE 3.13:
# Napisz funkcję occurs(number, array), która sprawdza,
# czy podana liczba znajduje się na liście.
# Liczbę podaje użytkownik z klawiatury.

# Definiujemy funkcję z dwoma parametrami:
# number - liczba, której szukamy,
# array - lista, w której szukamy.
def occurs(number, array):

    # Operator in sprawdza, czy element znajduje się na liście.
    # Funkcja zwróci True, jeśli liczba zostanie znaleziona,
    # albo False, jeśli jej nie ma.
    return number in array


# Tworzymy listę podaną w poleceniu.
numbers = [15, 38, 7, 23, 14]

# input() pobiera tekst wpisany przez użytkownika.
# int() zamienia wpisany tekst na liczbę całkowitą.
search_number = int(input("Podaj liczbę do wyszukania: "))

# Wywołujemy funkcję i zapisujemy jej wynik.
result = occurs(search_number, numbers)

# Sprawdzamy wynik działania funkcji.
if result:
    print("Liczba znajduje się na liście.")
else:
    print("Liczby nie ma na liście.")


# PRZYKŁADOWY WYNIK:
# Podaj liczbę do wyszukania: 38
# Liczba znajduje się na liście.


# NOTATKI:
# def - słowo kluczowe służące do definiowania funkcji.
#
# Parametry funkcji to dane, które przekazujemy do funkcji.
# W tym przypadku są to number oraz array.
#
# return - zwraca wynik działania funkcji.
#
# in - sprawdza, czy element znajduje się w liście.
#
# input() - pobiera dane wpisane przez użytkownika.
# Dane z input() są domyślnie tekstem.
#
# int() - zamienia tekst na liczbę całkowitą.
#
# True oznacza prawdę, a False oznacza fałsz.
#
# Co zwraca funkcja occurs()?
# Odpowiedź: True albo False.
#
# Dlaczego używamy int(input())?
# Odpowiedź: Ponieważ input() zwraca tekst, a chcemy otrzymać liczbę.