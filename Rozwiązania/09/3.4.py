# ZADANIE 3.4:
# Zamiana liczby naturalnej na system binarny za pomocą stosu.

# Zasada działania:
# 1. Dzielimy liczbę przez 2.
# 2. Zapisujemy resztę z dzielenia na stosie.
# 3. Dzielimy wynik całkowity przez 2.
# 4. Powtarzamy operację, aż wynik dzielenia będzie równy 0.
# 5. Pobieramy reszty ze stosu – w odwrotnej kolejności – i tworzymy liczbę binarną.

# Pobieramy liczbę od użytkownika.
number = int(input("Natural number: "))

# Sprawdzamy, czy podana liczba jest naturalna (0 lub większa).
if number < 0:
    print("Please enter a natural number (0 or greater).")

else:
    # Tworzymy pusty stos na reszty z dzielenia.
    stack = []

    # Kopiujemy liczbę, aby zachować jej pierwotną wartość.
    temp = number

    # Szczególny przypadek: zero w systemie binarnym to 0.
    if temp == 0:
        stack.append(0)

    # Powtarzamy dzielenie, dopóki liczba jest większa od zera.
    while temp > 0:

        # % 2 zwraca resztę z dzielenia przez 2.
        remainder = temp % 2

        # Odkładamy resztę na stos.
        stack.append(remainder)

        # // 2 wykonuje dzielenie całkowite.
        # Na przykład 18 // 2 daje 9.
        temp = temp // 2

    # Tworzymy pusty tekst na wynik binarny.
    binary_number = ""

    # Pobieramy reszty ze stosu w odwrotnej kolejności.
    while len(stack) > 0:

        # pop() pobiera ostatni element stosu i go usuwa.
        digit = stack.pop()

        # Zamieniamy cyfrę na tekst i dopisujemy do wyniku.
        binary_number += str(digit)

    # Wyświetlamy liczbę w systemie binarnym.
    print(f"Binary number: {binary_number}")


# str(digit) – zamienia liczbę na tekst, aby można było dopisać ją do napisu.
# binary_number += str(digit) – dopisuje kolejną cyfrę do wyniku.
# pop() – pobiera elementy ze stosu w odwrotnej kolejności niż zostały dodane