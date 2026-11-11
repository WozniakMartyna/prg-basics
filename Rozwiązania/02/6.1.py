# Program ma policzyć liczbę znaków w imieniu, nazwisku oraz w całym imieniu i nazwisku razem ze spacją.

# Program oblicza liczbę znaków w imieniu, nazwisku oraz w pełnym imieniu i nazwisku.

# Tworzymy zmienną name i zapisujemy w niej imię.
# Tekst zapisujemy w cudzysłowie lub apostrofach.
name = 'Martyna'

# Tworzymy zmienną surname i zapisujemy w niej nazwisko.
surname = 'Wozniak'

# Funkcja len() liczy liczbę znaków w tekście.
# Wynik zapisujemy w zmiennej characters_in_name.
characters_in_name = len(name)

# Liczymy znaki w nazwisku.
characters_in_surname = len(surname)

# Łączymy imię, spację i nazwisko.
# Operator + łączy teksty.
# Spacja w cudzysłowie oddziela imię od nazwiska.
full_name = name + ' ' + surname

# Liczymy znaki w całym tekście, razem ze spacją.
characters_in_full_name = len(full_name)

# Wyświetlamy liczbę znaków w imieniu.
# f przed tekstem oznacza f-string, czyli formatowany tekst. Dzięki niemu możemy wstawiać wartości zmiennych do tekstu za pomocą {}.
# Wartość zmiennej wstawiamy do tekstu za pomocą {}.
print(f'Your name has {characters_in_name} characters')

# Wyświetlamy liczbę znaków w nazwisku.
print(f'Your surname has {characters_in_surname} characters')

# Wyświetlamy liczbę znaków w pełnym imieniu i nazwisku.
print(f'Your full name has {characters_in_full_name} characters')