# Program ma wyświetlić wzrost w centymetrach, a następnie przeliczyć go na stopy i cale.
# 1 cal = 2,54 cm.
# 1 stopa = 12 cali.
# Najpierw zamieniamy centymetry na cale.
# Następnie obliczamy pełną liczbę stóp i pozostałą liczbę cali.

# Zapisujemy wzrost w centymetrach.
cm = 170

# Zamieniamy centymetry na cale.
# 1 cal ma 2.54 cm, dlatego dzielimy centymetry przez 2.54.
total_inches = cm / 2.54

# Obliczamy liczbę pełnych stóp.
# Operator // oznacza dzielenie całkowite bez reszty.
# Dzielimy liczbę cali przez 12, ponieważ jedna stopa ma 12 cali.
# int() zamienia wynik na liczbę całkowitą.
feet = int(total_inches // 12)

# Obliczamy liczbę cali, które pozostały po odjęciu pełnych stóp.
# Operator % oblicza resztę z dzielenia.
# round() zaokrągla wynik do dwóch miejsc po przecinku.
inches = round(total_inches % 12, 2)

# Wyświetlamy wzrost w centymetrach, stopach i calach.
# F-string pozwala wstawiać wartości zmiennych do tekstu za pomocą {}.
print(f'I am {cm} cm tall, i.e. {feet} feet and {inches} inches')