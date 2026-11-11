# Test jest zaliczony, jeśli poprawnie wykonano co najmniej 50% zadań.
# Łącznie jest 20 zadań, więc trzeba poprawnie wykonać co najmniej 10.

# Program sprawdza, czy test został zaliczony.

total_tasks = 20  # Całkowita liczba zadań w teście.

# input() pobiera liczbę poprawnie wykonanych zadań.
# int() zamienia wpisany tekst na liczbę całkowitą.
tasks_ok = int(input('Enter number of correctly completed tasks: '))

test_passed = False  # Na początku zakładamy, że test nie jest zaliczony.

# Sprawdzamy, czy liczba poprawnych odpowiedzi stanowi co najmniej połowę.
# >= oznacza "większe lub równe".
if tasks_ok >= total_tasks * 0.5:
    test_passed = True  # Jeśli warunek jest prawdziwy, zmieniamy wynik na True.

# Sprawdzamy wartość zmiennej test_passed.
if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')

# Sprawdzamy dla przykładowych liczb poprawnych odpowiedzi:
# 20 – Gratulacje! Test zaliczony.
# 11 – Gratulacje! Test zaliczony.
# 10 – Gratulacje! Test zaliczony.
# 9 – Niestety, test niezaliczony.
# 0 – Niestety, test niezaliczony.