# ZADANIE:
# Obliczenie wydatków w poszczególnych kategoriach,
# wydatków w każdym tygodniu i sumy za cały miesiąc.

# Każdy wiersz oznacza jeden tydzień.
# Kolumny oznaczają kolejno: Food, Transport, Utilities.
monthly_expenses = [
    [200, 50, 100],  # Week 1
    [180, 60, 110],  # Week 2
    [220, 55, 105],  # Week 3
    [210, 65, 95]    # Week 4
]

# Tworzymy listę, w której będziemy przechowywać
# sumę wydatków dla każdej kategorii.
# Na początku każda suma wynosi 0.
category_totals = [0, 0, 0]

# Tworzymy listę na sumy wydatków poszczególnych tygodni.
week_totals = []

# Zmienna przechowuje całkowite wydatki miesięczne.
monthly_total = 0

# Przechodzimy po wszystkich tygodniach.
for week in monthly_expenses:

    # Zmienna przechowuje sumę wydatków aktualnego tygodnia.
    week_total = 0

    # Pętla przechodzi po trzech kategoriach w aktualnym tygodniu.
    # range(3) generuje indeksy 0, 1 i 2.
    for i in range(3):

        # Dodajemy wydatek do sumy odpowiedniej kategorii.
        # category_totals[i] oznacza sumę kategorii o indeksie i.
        category_totals[i] += week[i]

        # Dodajemy wydatek do sumy aktualnego tygodnia.
        week_total += week[i]

    # Po zsumowaniu trzech kategorii zapisujemy wynik tygodnia.
    week_totals.append(week_total)

    # Dodajemy sumę tygodnia do sumy całego miesiąca.
    monthly_total += week_total


# Wyświetlamy obliczone wyniki.
print('MONTHLY EXPENSES')
print('----------------')

# Wyświetlamy sumy dla poszczególnych kategorii.
print('Food:', category_totals[0])
print('Transport:', category_totals[1])
print('Utilities:', category_totals[2])

# Wyświetlamy sumy dla kolejnych tygodni.
print('Week 1:', week_totals[0])
print('Week 2:', week_totals[1])
print('Week 3:', week_totals[2])
print('Week 4:', week_totals[3])

print('---------------')

# Wyświetlamy sumę wszystkich wydatków miesięcznych.
print('TOTAL:', monthly_total)