# ZADANIE 5.2
# Plik converters.py
# Należy utworzyć funkcje do przeliczania jednostek długości:
# metry na centymetry, centymetry na metry,
# centymetry na cale oraz stopy i cale na centymetry.

# Zamienia metry na centymetry.
# 1 metr = 100 centymetrów.
def m_to_cm(n):
    return n * 100

# Zamienia centymetry na metry.
# 1 centymetr = 0.01 metra.
def cm_to_m(n):
    return n / 100

# Zamienia centymetry na cale.
# 1 cal = 2.54 centymetra, dlatego dzielimy przez 2.54.
def cm_to_inches(n):
    return n / 2.5

# Zamienia stopy i cale na centymetry.
# Najpierw zamieniamy stopy na cale (1 stopa = 12 cali).
# Dodajemy podaną liczbę cali, a następnie mnożymy przez 2.54.
def feet_and_inches_to_cm(feet, inches):
    total_inches = feet * 12 + inches
    return total_inches * 2.54

# Ten warunek sprawia, że poniższe testy wykonają się tylko wtedy,
# gdy uruchomimy bezpośrednio plik converters.py.
# Nie wykonają się przy imporcie modułu do innego programu.
if __name__ == "__main__":

    # Testujemy zamianę metrów na centymetry.
    print(f'2m = {m_to_cm(2)}cm')

    # Testujemy zamianę centymetrów na metry.
    print(f'532cm = {cm_to_m(532)}m')

    # Testujemy zamianę centymetrów na cale.
    print(f'10cm = {cm_to_inches(10)} inches')

    # Testujemy zamianę stóp i cali na centymetry.
    print(f'5 feet and 6 inches = {feet_and_inches_to_cm(5, 6)}cm')


# - Co robi return? Zwraca wynik funkcji.
# - Dlaczego używamy / 2.54? Ponieważ jeden cal ma 2.54 cm.
# - Dlaczego mnożymy stopy przez 12? Ponieważ stopa ma 12 cali.
# - Co oznacza if __name__ == "__main__"?
#   Sprawdza, czy plik został uruchomiony bezpośrednio.
# - Czy można zmienić nazwy parametrów? Tak, ale trzeba
#   konsekwentnie zmienić je w całej funkcji.