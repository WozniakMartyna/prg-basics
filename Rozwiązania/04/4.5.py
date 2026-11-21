# ZADANIE 4.5
# Należy napisać funkcję pts_to_grade(points),
# która zamienia liczbę punktów na ocenę opisową.
# Zasady:
# mniej niż 10 punktów - Fail
# od 10 punktów - Satisfactory
# od 14 punktów - Good
# od 18 punktów - Excellent
# Na końcu należy przetestować funkcję dla 15 punktów.

# def tworzy funkcję pts_to_grade.
# points to parametr, czyli liczba zdobytych punktów.
def pts_to_grade(points):

    # Sprawdzamy warunki od najwyższego progu.
    # >= oznacza "większe lub równe".
    if points >= 18:
        grade = 'Excellent'

    # elif oznacza "w przeciwnym razie, jeśli".
    # Ten warunek sprawdzamy, jeśli poprzedni nie był prawdziwy.
    elif points >= 14:
        grade = 'Good'

    elif points >= 10:
        grade = 'Satisfactory'

    # else wykonuje się, jeśli żaden wcześniejszy warunek nie pasuje.
    else:
        grade = 'Fail'

    # Zwracamy przypisaną ocenę.
    return grade

# Przypisujemy zmiennej test_result wartość 15.
test_result = 15

# Wywołujemy funkcję i wyświetlamy ocenę.
print(pts_to_grade(test_result))

# - Dlaczego zaczynamy od 18? Żeby najpierw sprawdzić najwyższy próg.
# - Co oznacza elif? Sprawdza kolejny warunek, jeśli wcześniejszy nie pasował.
# - Czym różni się else od elif? else nie sprawdza warunku,
#   tylko wykonuje się, gdy żaden wcześniejszy warunek nie pasował.
# - Czy można użyć kilku instrukcji if zamiast elif? Można,
#   ale wtedy sprawdzane byłyby wszystkie warunki osobno.