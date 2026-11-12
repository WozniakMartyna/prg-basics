# W tym zadaniu przypisujemy użytkownika do odpowiedniej grupy wiekowej.
# Dziecko ma mniej niż 13 lat, nastolatek od 13 do 19 lat,
# dorosły od 20 do 64 lat, a senior co najmniej 65 lat.

# input() pobiera wiek wpisany przez użytkownika.
# int() zamienia wpisany tekst na liczbę całkowitą, aby można było porównywać wiek z innymi liczbami.
age = int(input('Enter your age: '))

# Sprawdzamy warunki po kolei, zaczynając od najmłodszej grupy.
if age < 13:
    print('Child')
elif age <= 19:
    print('Teen')
elif age <= 64:
    print('Adult')
else:
    # Jeżeli żaden wcześniejszy warunek nie został spełniony, wiek wynosi co najmniej 65 lat.
    print('Senior')

# elif sprawdza kolejny warunek tylko wtedy, gdy wcześniejszy warunek if lub elif był fałszywy.
# Dlatego w elif age <= 19 nie musimy ponownie sprawdzać, czy wiek jest większy lub równy 13.