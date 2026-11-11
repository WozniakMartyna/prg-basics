# Limit prędkości na autostradzie wynosi 140 km/h. Program ma pobrać prędkość samochodu i wyświetlić ostrzeżenie, jeżeli kierowca przekroczył limit.

speed_limit = 140  # Zmienna przechowuje dozwoloną prędkość: 140 km/h.

# input() wyświetla pytanie i pobiera tekst wpisany przez użytkownika.
# int() zamienia wpisany tekst na liczbę całkowitą.
car_speed = int(input('Enter car speed (km/h): '))

# Sprawdzamy, czy prędkość samochodu jest większa od limitu.
# Operator > oznacza "większe niż".
if car_speed > speed_limit:
    # f-string (litera f przed tekstem) pozwala wstawiać wartości zmiennych do tekstu za pomocą nawiasów klamrowych {}.
    print(f'Your speed is {car_speed} km/h')
    print('Warning: speed limit exceeded!!')

# if wykonuje wcięty kod tylko wtedy, gdy warunek jest prawdziwy.