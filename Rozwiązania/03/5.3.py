# Program prosi użytkownika o imię.
# Jeżeli użytkownik nic nie wpisze, pytanie zostanie powtórzone.

name = ''  # Tworzymy pusty tekst. Na początku nie znamy imienia użytkownika.

while name == '':  # Pętla działa, dopóki name jest pustym tekstem.
    # == oznacza porównanie dwóch wartości. Nie jest tym samym co =, które przypisuje wartość.
    name = input('Enter your name: ')  # Pobieramy imię od użytkownika.
    # Jeśli użytkownik naciśnie Enter bez wpisania imienia, zmienna pozostanie pusta i pętla powtórzy pytanie.

# Ta instrukcja znajduje się poza pętlą, dlatego wykona się po jej zakończeniu.
print(f'Hello {name}')  # to f-string. Litera f przed cudzysłowem pozwala wstawiać wartości zmiennych do tekstu za pomocą nawiasów klamrowych {}.