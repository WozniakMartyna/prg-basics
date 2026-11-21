# ZADANIE: Oblicz statystyki wyników testu.
# True oznacza poprawną odpowiedź, a False błędną odpowiedź.

# Tworzymy listę wyników testu.
# Każdy element jest wartością logiczną: True albo False.
test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]


# 1. Obliczamy liczbę wszystkich pytań.
# len() zwraca liczbę elementów listy.
# Każdy element listy odpowiada jednemu pytaniu.
question_number = len(test_results)


# 2. Obliczamy liczbę poprawnych odpowiedzi.
# Na początku licznik poprawnych odpowiedzi wynosi 0.
correct_answers = 0

# Przechodzimy przez wszystkie wyniki testu.
# Zmienna answer przechowuje aktualną wartość True lub False.
for answer in test_results:

    # Sprawdzamy, czy odpowiedź jest poprawna.
    if answer == True:

        # Jeżeli answer ma wartość True, zwiększamy licznik o 1.
        correct_answers += 1


# 3. Obliczamy liczbę błędnych odpowiedzi.
# Wszystkie pytania minus poprawne odpowiedzi
# dają liczbę odpowiedzi niepoprawnych.
incorrect_answers = question_number - correct_answers


# 4. Obliczamy procent poprawnych odpowiedzi.
# Dzielimy liczbę poprawnych odpowiedzi przez liczbę wszystkich pytań.
# Mnożymy przez 100, aby otrzymać wynik procentowy.
correct_percentage = correct_answers / question_number * 100


# Wyświetlamy przygotowane statystyki.
print("TEST STATISTICS")
print("===============")
print("Number of questions:", question_number)
print("Number of correct answers:", correct_answers)
print("Number of incorrect answers:", incorrect_answers)
print("Percentage of correct answers:", correct_percentage, "%")