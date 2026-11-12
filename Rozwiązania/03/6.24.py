# Program wyświetla wzór z gwiazdek:
# najpierw zwiększa liczbę gwiazdek od 1 do 5,
# a następnie zmniejsza ją od 4 do 1.

# Pierwsza pętla zwiększa liczbę gwiazdek od 1 do 5.
for i in range(1, 6):

    # Powtarzamy tekst '* ' tyle razy, ile wynosi i.
    # Na przykład dla i = 3 otrzymamy '* * *'.
    print('* ' * i)

# Druga pętla zmniejsza liczbę gwiazdek od 4 do 1.
# Wartość -1 oznacza, że za każdym razem odejmujemy 1.
for i in range(4, 0, -1):

    # Ponownie wypisujemy gwiazdki, tym razem w malejącej liczbie.
    print('* ' * i)

# W range(4, 0, -1) trzeci argument -1 oznacza, że liczby zmniejszają się o jeden. Z kolei mnożenie tekstu przez liczbę powtarza ten tekst.