# Program wyświetla tabliczkę mnożenia dla liczby podanej przez użytkownika.

# input() pobiera liczbę od użytkownika jako tekst.
# int() zamienia wpisany tekst na liczbę całkowitą.
number = int(input('Enter number: '))

# Pętla przechodzi przez liczby od 1 do 10.
for i in range(1, 11):

    # Mnożymy podaną liczbę przez aktualną wartość i.
    result = number * i

    # f-string pozwala wstawiać wartości zmiennych do tekstu za pomocą {}.
    print(f'{number} x {i} = {result}')