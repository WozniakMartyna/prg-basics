# Wyświetlanie kuponu lotto z liczbami od 1 do 49

for row in range(7):  # range(7) daje liczby od 0 do 6, czyli 7 wierszy
    for column in range(7):  # W każdym wierszu wyświetlamy 7 liczb
        # Obliczamy liczbę: numer wiersza + 1 + numer kolumny pomnożony przez 7
        number = row + 1 + column * 7

        print(number, end=' ')  # Wyświetlamy liczbę i spację, bez przechodzenia do nowej linii

    print()  # Po wyświetleniu 7 liczb przechodzimy do nowego wiersza