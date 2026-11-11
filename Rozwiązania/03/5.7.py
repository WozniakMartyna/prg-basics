# W oryginalnym programie wystarczy dodać warunek if, który sprawdzi, czy zostało pięć sekund lub mniej. Wtedy zamiast liczby wyświetlimy jej angielską nazwę.
# Program pobiera liczbę sekund od użytkownika i odlicza do zera.
# Ostatnie pięć sekund wyświetla słownie: five, four, three, two, one.

import time  # Importujemy moduł time pozwalający wykonywać operacje związane z czasem.

countdown = int(input("Enter the number of seconds to count down: "))
# input() pobiera tekst od użytkownika.
# int() zamienia wpisany tekst na liczbę całkowitą.

# Słownik przechowuje angielskie nazwy liczb od 5 do 1.
number_words = {
    5: "five",
    4: "four",
    3: "three",
    2: "two",
    1: "one"
}

# Pętla działa tak długo, jak countdown jest większe od zera.
while countdown > 0:

    # Jeżeli zostało 5 sekund lub mniej, wyświetlamy liczbę słownie.
    if countdown <= 5:
        print(number_words[countdown]) # pobiera ze słownika nazwę odpowiadającą aktualnej liczbie.

    # W przeciwnym przypadku wyświetlamy liczbę normalnie.
    else:
        print(countdown)

    countdown -= 1  # Zmniejsza licznik o jeden (1 sekundę). Jest to skrócony zapis countdown = countdown - 1.

    time.sleep(1)  # Zatrzymujemy program na 1 sekundę.

print("Time's up!")  # Wyświetlamy komunikat po zakończeniu odliczania.