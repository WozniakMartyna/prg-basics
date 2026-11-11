# Program ma sprawdzać, czy na koncie jest wystarczająco dużo pieniędzy, aby zapłacić za zakupy.
# Saldo konta wynosi 500 zł.

account_balance = 500  # Saldo konta wynosi 500 zł.

# input() pobiera kwotę zakupów jako tekst.
# float() zamienia tekst na liczbę, która może mieć część dziesiętną.
total_payment = float(input('Enter total payment: '))

# Sprawdzamy, czy saldo konta jest większe lub równe kwocie zakupów.
# >= oznacza "większe lub równe".
if total_payment <= account_balance:
    print('Payment completed')  # Płatność jest możliwa.
else:
    print('No funds')  # Saldo jest za małe.

# Sprawdzamy dla przykładowych kwot:
# 140 zł – Płatność jest możliwa.
# 499 zł – Płatność jest możliwa.
# 500 zł – Płatność jest możliwa.
# 501 zł – Saldo jest za małe.
# 720 zł – Saldo jest za małe.