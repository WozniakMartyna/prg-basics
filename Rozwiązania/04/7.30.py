# ZADANIE: Oblicz sumę liczb naturalnych od 1 do n rekurencyjnie.
# Przykład: dla n = 4 wynik to 1 + 2 + 3 + 4 = 10.

def sum_natural(n):
    # WARUNEK STOPU:
    # Suma od 1 do 0 wynosi 0.
    if n == 0:
        return 0

    # REKURENCJA:
    # Dodajemy n do sumy wszystkich liczb mniejszych od n.
    return n + sum_natural(n - 1)


def main():
    print(sum_natural(10))  # 10 + 9 + ... + 1 = 55.


if __name__ == "__main__":
    main()