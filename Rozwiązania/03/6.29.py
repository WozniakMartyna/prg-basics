# Wyświetlanie pierwszych N liczb pierwszych

# input() pobiera tekst wpisany przez użytkownika.
# int() zamienia ten tekst na liczbę całkowitą.
n = int(input('How many prime numbers? '))

number = 2  # Od liczby 2 rozpoczynamy sprawdzanie
found = 0  # Licznik znalezionych liczb pierwszych

while found < n:  # Pętla działa, dopóki nie znajdziemy N liczb pierwszych
    is_prime = True  # Na początku zakładamy, że liczba jest pierwsza
    divisor = 2  # Pierwszy sprawdzany dzielnik

    while divisor < number:  # Sprawdzamy dzielniki mniejsze od badanej liczby
        if number % divisor == 0:  # % oblicza resztę z dzielenia; 0 oznacza podzielność bez reszty
            is_prime = False  # Liczba nie jest pierwsza
            break  # Przerywamy sprawdzanie dzielników

        divisor += 1  # Zwiększamy dzielnik o 1

    if is_prime:  # Jeśli liczba jest pierwsza
        print(number, end=' ')  # Wyświetlamy ją
        found += 1  # Zwiększamy liczbę znalezionych liczb pierwszych

    number += 1  # Przechodzimy do sprawdzania kolejnej liczby