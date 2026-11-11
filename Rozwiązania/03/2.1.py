# elif oznacza „w przeciwnym razie, jeżeli”.
# # Dzięki niej możemy sprawdzić kilka warunków po kolei.

# Program sprawdza, czy liczba jest dodatnia, ujemna czy równa zero.

number = 5  # Zapisujemy liczbę w zmiennej.

if number > 0:  # Sprawdzamy, czy liczba jest większa od zera.
    print('Positive number')
elif number < 0:  # Jeśli pierwszy warunek był fałszywy, sprawdzamy, czy liczba jest mniejsza od zera.
    print('Negative number')
else:  # Jeśli żaden wcześniejszy warunek nie był prawdziwy, liczba musi być równa zero.
    print('Number is 0')

# Python sprawdza warunek przy if.
# Jeśli jest prawdziwy, wykonuje jego kod i pomija pozostałe warunki.
# Jeśli jest fałszywy, sprawdza kolejny warunek przy elif.
# Jeśli żaden warunek nie jest prawdziwy, wykonuje else.
# Możemy używać kilku instrukcji elif w jednym programie.
# Python wykonuje tylko pierwszy blok, którego warunek jest prawdziwy.