# ZADANIE 4.7
# Należy uzupełnić program, który zamienia każdą literę imienia
# wpisanego przez użytkownika na odpowiadające jej słowo z alfabetu ICAO.
# Przykładowo litera A oznacza Alfa, B oznacza Bravo, C oznacza Charlie.
# Funkcja icao() jest już podana w zadaniu – uzupełniamy część,
# która przechodzi po literach imienia i wyświetla odpowiednie słowa.

# Funkcja icao() zamienia literę na odpowiadające jej słowo ICAO.
def icao(letter):

    # capitalize() zamienia pierwszą literę na wielką,
    # a pozostałe litery na małe.
    # Dzięki temu funkcja rozpoznaje zarówno 'a', jak i 'A'.
    letter = letter.capitalize()

    # Sprawdzamy, jaka litera została przekazana do funkcji.
    if letter == 'A':
        icao_name = 'Alfa'
    elif letter == 'B':
        icao_name = 'Bravo'
    elif letter == 'C':
        icao_name = 'Charlie'
    elif letter == 'D':
        icao_name = 'Delta'
    elif letter == 'E':
        icao_name = 'Echo'
    elif letter == 'F':
        icao_name = 'Foxtrot'
    elif letter == 'G':
        icao_name = 'Golf'
    elif letter == 'H':
        icao_name = 'Hotel'
    elif letter == 'I':
        icao_name = 'India'
    elif letter == 'J':
        icao_name = 'Juliett'
    elif letter == 'K':
        icao_name = 'Kilo'
    elif letter == 'L':
        icao_name = 'Lima'
    elif letter == 'M':
        icao_name = 'Mike'
    elif letter == 'N':
        icao_name = 'November'
    elif letter == 'O':
        icao_name = 'Oscar'
    elif letter == 'P':
        icao_name = 'Papa'
    elif letter == 'Q':
        icao_name = 'Quebec'
    elif letter == 'R':
        icao_name = 'Romeo'
    elif letter == 'S':
        icao_name = 'Sierra'
    elif letter == 'T':
        icao_name = 'Tango'
    elif letter == 'U':
        icao_name = 'Uniform'
    elif letter == 'V':
        icao_name = 'Victor'
    elif letter == 'W':
        icao_name = 'Whiskey'
    elif letter == 'X':
        icao_name = 'X-ray'
    elif letter == 'Y':
        icao_name = 'Yankee'
    elif letter == 'Z':
        icao_name = 'Zulu'
    else:
        # Jeśli znak nie jest literą od A do Z, zwracamy ???.
        icao_name = '???'

    # return zwraca nazwę słowa przypisanego do litery.
    return icao_name


# Pobieramy imię wpisane przez użytkownika.
name = input('Enter your name: ')

# Wyświetlamy nagłówek przed wypisaniem słów ICAO.
print('ICAO words for spelling out your name:')

# for przechodzi kolejno po każdym znaku wpisanego imienia.
# char oznacza aktualnie sprawdzany znak.
for char in name:

    # Wywołujemy funkcję icao() dla aktualnej litery.
    # Otrzymane słowo zapisujemy w zmiennej word.
    word = icao(char)

    # Wyświetlamy słowo.
    # end=" " sprawia, że kolejne słowa pojawiają się w tej samej linii,
    # oddzielone spacją, zamiast każde w nowej linii.
    print(word, end=" ")

# - Co robi capitalize()? Zmienia pierwszą literę na wielką,
#   a pozostałe na małe.
# - Co robi for char in name? Przechodzi po każdym znaku tekstu name.
# - Co robi icao(char)? Wywołuje funkcję dla aktualnego znaku.
# - Co robi end=" "? Zmienia zakończenie print(), aby nie przechodzić
#   do nowej linii, tylko wstawić spację.
# - Czy można zmienić nazwę char? Tak, to nazwa zmiennej,
#   ale trzeba używać tej samej nazwy wewnątrz pętli.
# - Czy można użyć print(word) bez end=" "? Tak, ale wtedy
#   każde słowo zostanie wyświetlone w osobnej linii.