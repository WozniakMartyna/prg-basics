# ZADANIE: Oblicz silnię liczby n za pomocą rekurencji.
# Silnia to iloczyn kolejnych liczb naturalnych od 1 do n.
# Przykład: 5! = 5 * 4 * 3 * 2 * 1 = 120.

def factorial(n):
    # WARUNEK STOPU:
    # Silnia 0 i 1 wynosi 1.
    # Ten warunek zatrzymuje kolejne wywołania funkcji.
    if n == 0 or n == 1:
        return 1

    # REKURENCJA:
    # Funkcja wywołuje samą siebie dla mniejszej liczby.
    if n > 1:
        return n * factorial(n - 1)


def main():
    print(factorial(5))  # Wynik: 120


if __name__ == "__main__":
    main()