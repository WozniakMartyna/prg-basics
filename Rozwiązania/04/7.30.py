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

# Obliczamy sumę liczb od 1 do 10.
def main():
    print(sum_natural(10))  # 10 + 9 + ... + 1 = 55.


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