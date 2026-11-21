# ZADANIE: Oblicz potęgę x^n za pomocą rekurencji.
# Przykład: 5^3 = 5 * 5 * 5 = 125.

def power(x, n):
    # WARUNEK STOPU:
    # Każda liczba podniesiona do potęgi 0 daje 1.
    if n == 0:
        return 1

    # REKURENCJA:
    # x^n = x * x^(n-1)
    return x * power(x, n - 1)


def main():
    print(power(5, 3))  # 5^3 = 5 * 5 * 5 = 125.


if __name__ == "__main__":
    main()