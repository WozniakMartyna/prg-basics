# ZADANIE:
# Sprawdzenie liczby miejsc dostępnych i zarezerwowanych w kinie
# oraz sprawdzenie statusu wybranego miejsca.

# Tworzymy listę dwuwymiarową reprezentującą salę kinową.
# Sala ma 5 wierszy i 5 miejsc w każdym wierszu.
# A = Available (dostępne)
# B = Booked (zarezerwowane)
cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
]


# Funkcja oblicza całkowitą liczbę miejsc.
def seats_total(seats):

    # len(seats) zwraca liczbę wierszy.
    # W tym przypadku jest ich 5.
    rows = len(seats)

    # len(seats[0]) zwraca liczbę miejsc w pierwszym wierszu.
    # W tym przypadku jest ich 5.
    places_in_row = len(seats[0])

    # Mnożymy liczbę wierszy przez liczbę miejsc w wierszu.
    return rows * places_in_row


# Funkcja oblicza liczbę dostępnych miejsc.
def seats_available(seats):

    # Zmienna będzie przechowywać liczbę miejsc dostępnych.
    available = 0

    # Przechodzimy po wszystkich wierszach.
    for row in seats:

        # Przechodzimy po każdym miejscu w aktualnym wierszu.
        for place in row:

            # Jeżeli miejsce ma wartość A, jest dostępne.
            if place == 'A':

                # Zwiększamy licznik o 1.
                available += 1

    # Zwracamy policzoną liczbę dostępnych miejsc.
    return available


# Funkcja oblicza liczbę zarezerwowanych miejsc.
def seats_booked(seats):

    # Zmienna będzie przechowywać liczbę zarezerwowanych miejsc.
    booked = 0

    # Przechodzimy po wszystkich wierszach.
    for row in seats:

        # Przechodzimy po wszystkich miejscach w aktualnym wierszu.
        for place in row:

            # Jeżeli miejsce ma wartość B, jest zarezerwowane.
            if place == 'B':

                # Zwiększamy licznik o 1.
                booked += 1

    # Zwracamy liczbę zarezerwowanych miejsc.
    return booked


# Funkcja sprawdza status wybranego miejsca.
# row - numer wiersza podany przez użytkownika (od 1).
# place - numer miejsca podany przez użytkownika (od 1).
def seat_status(seats, row, place):

    # Zamieniamy numery podane od 1 na indeksy Pythona od 0.
    # Na przykład wiersz 1 i miejsce 1 to seats[0][0].
    row_index = row - 1
    place_index = place - 1

    # Pobieramy oznaczenie wybranego miejsca.
    status = seats[row_index][place_index]

    # Sprawdzamy, czy miejsce jest dostępne.
    if status == 'A':
        return "Available"

    # Jeżeli nie jest dostępne, oznacza to, że jest zarezerwowane.
    else:
        return "Booked"


# Wyświetlamy informacje o sali kinowej.
print('CINEMA INFORMATION TABLE')

# Wywołujemy funkcję seats_total() i wyświetlamy wynik.
print('Total seats:', seats_total(cinema_seats))

# Wywołujemy funkcję seats_available() i wyświetlamy wynik.
print('Seats available:', seats_available(cinema_seats))

# Wywołujemy funkcję seats_booked() i wyświetlamy wynik.
print('Seats booked:', seats_booked(cinema_seats))

# Sprawdzamy status miejsca w pierwszym wierszu i pierwszej kolumnie.
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))

# Sprawdzamy status miejsca w piątym wierszu i piątej kolumnie.
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))

# Sprawdzamy status miejsca w trzecim wierszu i piątej kolumnie.
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))