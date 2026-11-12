# W tym zadaniu sprawdzamy, czy imię wpisane przez użytkownika kończy się literą "a".
# Przyjmujemy uproszczoną zasadę z polecenia, że większość polskich imion żeńskich kończy się na "a".

# input() pobiera imię wpisane przez użytkownika i zapisuje je jako tekst.
name = input('Enter name: ')

# name != '' sprawdza, czy użytkownik wpisał jakikolwiek tekst.
# name[-1] pobiera ostatni znak tekstu. Indeks -1 oznacza ostatni znak.
# lower() zamienia pobrany znak na małą literę, dzięki czemu rozpoznajemy też wielkie "A".
if name != '' and name[-1].lower() == 'a':
    # F-string pozwala wstawić wartość zmiennej name do wyświetlanego tekstu.
    print(f'{name} -- Polish female name')

# Operator and wymaga spełnienia obu warunków.
# Najpierw sprawdzamy, czy imię nie jest puste, aby nie próbować pobrać znaku z pustego tekstu.