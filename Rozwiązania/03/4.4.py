# Program ma wyświetlić nazwę uczelni tak, aby pomiędzy każdym znakiem znajdowała się dodatkowa spacja.

# Zmienna university przechowuje nazwę uczelni.
university = 'Krakow University of Economics'

# Tworzymy pusty tekst, do którego będziemy dodawać znaki i spacje.
university_expanded = ''

# Pętla for przechodzi kolejno przez każdy znak nazwy uczelni.
# Zmienna char przechowuje aktualny znak.
for char in university:
    # Dodajemy aktualny znak oraz spację do nowego tekstu.
    # Operator + łączy teksty ze sobą.
    # Wcięcie wskazuje, że dodawanie znaków odbywa się wewnątrz pętli.
    university_expanded = university_expanded + char + ' '

# Usuwamy ostatnią, niepotrzebną spację z końca tekstu.
# [:-1] oznacza wszystkie znaki oprócz ostatniego (slicing).
university_expanded = university_expanded[:-1]

# Wyświetlamy oryginalną nazwę uczelni.
print(university)

# Wyświetlamy nazwę uczelni z dodatkowymi spacjami.
print(university_expanded)