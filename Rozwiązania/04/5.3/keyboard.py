# ZADANIE 5.3:
# Utwórz funkcje do pobierania z klawiatury tekstu,
# liczby całkowitej, liczby rzeczywistej i wartości logicznej.


# FUNKCJA 1: pobieranie tekstu (string).

# def definiuje funkcję.
# message to parametr zawierający komunikat dla użytkownika.
def input_string(message):
    value = input(message)  # input() pobiera tekst z klawiatury.
    return value            # return zwraca pobrany tekst.


# FUNKCJA 2: pobieranie liczby całkowitej (integer).

def input_integer(message):
    value = input(message)  # input() pobiera tekst.
    return int(value)       # int() zamienia tekst na liczbę całkowitą.


# FUNKCJA 3: pobieranie liczby rzeczywistej (real).

def input_real(message):
    value = input(message)  # Pobieramy tekst z klawiatury.
    return float(value)     # float() zamienia tekst na liczbę rzeczywistą.


# FUNKCJA 4: pobieranie wartości logicznej (boolean).

def input_boolean(message):
    value = input(message)  # Pobieramy odpowiedź y albo n.
    return value.lower() == 'y'

# lower() zamienia litery na małe.
# == sprawdza, czy odpowiedź jest równa 'y'.
# Jeśli tak, funkcja zwraca True. W przeciwnym razie False.
#
# WAŻNE:
# input() zawsze zwraca tekst (string).
# int() zamienia tekst na liczbę całkowitą.
# float() zamienia tekst na liczbę rzeczywistą.
# return przekazuje wynik funkcji do miejsca jej wywołania.
# True i False to dwie wartości typu logicznego (boolean).