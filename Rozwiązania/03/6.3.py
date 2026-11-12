# W tym zadaniu sprawdzamy, ile żarówek świeci w zależności od ustawienia dwóch przełączników.
# Pierwszy przełącznik włącza jedną żarówkę, a drugi dwie żarówki.

light_switch1 = False  # False oznacza wyłączony przełącznik, True oznacza włączony.
light_switch2 = False
bulbs_on = 0  # Na początku żadna żarówka nie jest włączona.

# Jeżeli pierwszy przełącznik jest włączony, dodajemy jedną żarówkę.
if light_switch1:
    bulbs_on += 1 # To to samo co: bulbs_on = bulbs_on + 1

# Jeżeli drugi przełącznik jest włączony, dodajemy dwie żarówki.
if light_switch2:
    bulbs_on += 2

# F-string pozwala wstawić wartość zmiennej bulbs_on do tekstu za pomocą nawiasów klamrowych.
print(f'Number of bulbs on: {bulbs_on}')