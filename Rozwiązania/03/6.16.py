# W tym zadaniu obliczamy całkowity czas prania w zależności od wybranego programu i dodatkowych opcji.
# Kurtka pierze się 40 minut, bielizna 70 minut, a buty 20 minut.
# Dodatkowe płukanie trwa 15 minut, a dodatkowe wirowanie 9 minut.

total_washing_time = 0  # Zmienna przechowuje całkowity czas prania.

# input() pobiera wybrany program oraz odpowiedzi dotyczące dodatkowych opcji.
# lower() zamienia wpisany tekst na małe litery, aby rozpoznawać zarówno Y, jak i y.
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ').lower()
extra_rinse = input('Extra rinse? (y/n): ').lower()
extra_spin = input('Extra spin? (y/n): ').lower()

# Wybieramy czas podstawowego programu prania.
# if sprawdza pierwszy możliwy wybór, a elif kolejne możliwości.
if program == 'j':
    total_washing_time = 40
elif program == 'u':
    total_washing_time = 70
elif program == 's':
    total_washing_time = 20
else:
    # Wartość -1 oznacza, że użytkownik wybrał nieprawidłowy program.
    total_washing_time = -1

# Dodatkowe opcje doliczamy tylko wtedy, gdy wybrano poprawny program.
if total_washing_time >= 0:

    # Jeżeli użytkownik wpisał y, dodajemy 15 minut za dodatkowe płukanie.
    if extra_rinse == 'y':
        total_washing_time += 15

    # Jeżeli użytkownik wpisał y, dodajemy 9 minut za dodatkowe wirowanie.
    if extra_spin == 'y':
        total_washing_time += 9

    # F-string wstawia wartość zmiennej do tekstu za pomocą nawiasów klamrowych {}.
    print(f'Total washing time: {total_washing_time} minutes')
else:
    print('Incorrect washing program')

# Dlaczego używamy dwóch osobnych instrukcji if dla płukania i wirowania?
# Ponieważ użytkownik może wybrać obie opcje jednocześnie.
# Każda opcja powinna wtedy niezależnie zwiększyć całkowity czas prania.