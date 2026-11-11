# Program ma obliczyć sumę liczb parzystych w zakresie od 1 do 10.
# Liczby parzyste to: 2, 4, 6, 8, 10.
# W tym zadaniu wykorzystamy również:
# % – oblicza resztę z dzielenia.
# continue – pomija pozostałe instrukcje w bieżącym powtórzeniu pętli i przechodzi do następnego.

# Zmienna sum przechowuje wynik dodawania.
# Na początku suma wynosi 0.
sum = 0

# range(1, 11) tworzy liczby od 1 do 10.
for i in range(1, 11):
    # for przechodzi przez wszystkie liczby w zakresie.
    # i przechowuje aktualną liczbę.
    # Operator % oblicza resztę z dzielenia przez 2.
    # Jeśli reszta jest różna od 0, liczba jest nieparzysta.
    # != oznacza "różne od".
    if i % 2 != 0:
        # if sprawdza, czy warunek jest prawdziwy.
        # continue pomija dalsze instrukcje w tym powtórzeniu pętli.
        # Program przechodzi do następnej liczby.
        continue

    # Jeśli liczba jest parzysta, dodajemy ją do sumy.
    sum += i

# Wyświetlamy obliczoną sumę.
print(f'Sum of even numbers in the range <1,10> is {sum}')