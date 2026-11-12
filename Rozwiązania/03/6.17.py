# Program zamienia czas zapisany w formacie 24-godzinnym
# (np. 16:30) na format 12-godzinny (np. 4:30pm).

# input() pobiera od użytkownika tekst, np. "16:30".
time_24 = input('Enter time in 24-hour format (hh:mm): ')

# int() zamienia tekst na liczbę całkowitą.
# [0:2] pobiera dwa pierwsze znaki, czyli godzinę.
hour = int(time_24[0:2])

# [3:5] pobiera znaki od pozycji 3 do 4, czyli minuty.
# Minuty pozostają tekstem, ponieważ nie wykonujemy na nich obliczeń.
minutes = time_24[3:5]

# if sprawdza, czy godzina wynosi 0, czyli północ.
if hour == 0:
    hour_12 = 12
    period = 'am'

# elif sprawdza kolejny warunek, jeśli poprzedni nie był prawdziwy.
# Godziny mniejsze od 12 oznaczają czas przed południem.
elif hour < 12:
    hour_12 = hour
    period = 'am'

# Godzina 12 oznacza południe.
elif hour == 12:
    hour_12 = 12
    period = 'pm'

# else wykonuje się, jeśli żaden wcześniejszy warunek nie był prawdziwy.
# Dla godzin większych od 12 odejmujemy 12.
else:
    hour_12 = hour - 12
    period = 'pm'

# f-string (litera f przed tekstem) pozwala wstawiać wartości zmiennych
# w miejsca oznaczone nawiasami klamrowymi {}.
print(f'Time in 12-hour format: {hour_12}:{minutes}{period}')