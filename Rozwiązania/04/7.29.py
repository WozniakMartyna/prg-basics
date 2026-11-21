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

# if __name__ == "__main__": oznacza: wykonaj poniższy kod tylko wtedy, gdy ten plik został uruchomiony bezpośrednio, a nie zaimportowany jako moduł.

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