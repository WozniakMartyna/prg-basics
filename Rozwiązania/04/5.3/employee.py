# ZADANIE 5.3:
# Program pozwala wprowadzić i wyświetlić dane pracownika.
# Można zdecydować, czy wynagrodzenie zostanie wyświetlone.


# IMPORT MODUŁU

# import dołącza moduł keyboard.py.
# Nie wpisujemy rozszerzenia .py.
import keyboard

# POBIERANIE DANYCH PRACOWNIKA

# keyboard.nazwa_funkcji() wywołuje funkcję z modułu keyboard.
first_name = keyboard.input_string('Enter name: ')
last_name = keyboard.input_string('Enter last name: ')
age = keyboard.input_integer('Enter age: ')
salary = keyboard.input_real('Enter salary: ')

# Pytamy, czy wynagrodzenie ma być ukryte.
# y oznacza True (ukryj), n oznacza False (pokaż).
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n) ')


# WYŚWIETLANIE DANYCH PRACOWNIKA

print('DATA RECORD')
print('===========')

print('Name:', first_name, last_name)
print('Age:', age)

# if sprawdza warunek.
# not odwraca wartość logiczną.
# Wynagrodzenie pokaże się tylko wtedy, gdy nie jest ukryte.
if not is_salary_hidden:
    print('Salary:', salary)


# NOTATKI:
# import keyboard - importuje nasz moduł.
# Kropka w keyboard.input_string oznacza dostęp do funkcji modułu.
# if - wykonuje kod, gdy warunek jest prawdziwy (True).
# not - zamienia True na False, a False na True.
# Wcięcie przed print oznacza, że należy on do instrukcji if.