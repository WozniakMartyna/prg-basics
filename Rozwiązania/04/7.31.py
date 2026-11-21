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

# Oznacza: jeśli ten plik został uruchomiony bezpośrednio, wykonaj funkcję main().
# 
# 
# REKURENCJA – NAJWAŻNIEJSZE INFORMACJE
#
# Rekurencja to sposób rozwiązywania problemu, w którym funkcja
# wywołuje samą siebie, ale z mniejszym lub prostszym argumentem.
#
# Każda rekurencja musi mieć:
# 1. Warunek zakończenia – określa, kiedy funkcja ma przestać
#    wywoływać samą siebie.
# 2. Wywołanie rekurencyjne – funkcja ponownie wywołuje samą siebie,
#    aby rozwiązać mniejszą część problemu.
#
# Funkcja najpierw wykonuje kolejne wywołania, aż osiągnie
# warunek zakończenia. Następnie zwracane są wyniki i wykonywane
# są pozostałe działania.