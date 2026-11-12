# W tym zadaniu sprawdzamy, czy prędkość samochodu mieści się w dozwolonym zakresie.
# Minimalna prędkość wynosi 40 km/h, a maksymalna 140 km/h.

speed_limit_min = 40
speed_limit_max = 140

# input() pobiera prędkość wpisaną przez użytkownika.
# int() zamienia tekst na liczbę całkowitą, aby można było porównać prędkość z limitami.
car_speed = int(input('Enter car speed: '))

# Operator or oznacza "lub".
# Wystarczy, że jeden warunek będzie prawdziwy, aby wyświetlić ostrzeżenie.
if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print('Warning: invalid car speed!!')
else:
    print('Car speed is valid')

# Czy prędkość 40 lub 140 km/h jest prawidłowa?
# Tak, ponieważ warunki sprawdzają wartości mniejsze niż 40 oraz większe niż 140.
# Same wartości graniczne są więc dozwolone.