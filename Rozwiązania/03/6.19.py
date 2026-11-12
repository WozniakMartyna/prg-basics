# Program zadaje użytkownikowi trzy pytania.
# Odpowiedzi zapisuje jako wartości logiczne True albo False,
# a następnie wyświetla je w formie Yes lub No.

# input() pobiera odpowiedź użytkownika.
# lower() zamienia wpisany tekst na małe litery.
# == 'y' sprawdza, czy odpowiedź jest równa literze y.
# Wynikiem porównania jest True (prawda) albo False (fałsz).
interested = input('Are you interested in programming? (y/n): ').lower() == 'y'

games = input('Do you play computer games? (y/n): ').lower() == 'y'

instagram = input('Do you have an Instagram account? (y/n): ').lower() == 'y'

# Sprawdzamy pierwszą odpowiedź.
if interested:
    print('Interested in programming: Yes')
else:
    print('Interested in programming: No')

# Sprawdzamy drugą odpowiedź.
if games:
    print('Do you play computer games? Yes')
else:
    print('Do you play computer games? No')

# Sprawdzamy trzecią odpowiedź.
if instagram:
    print('Do you have an Instagram account? Yes')
else:
    print('Do you have an Instagram account? No')