# Program oblicza sumę i średnią liczb wpisanych przez użytkownika.
# Wpisanie 0 kończy wprowadzanie liczb.

total_sum = 0  # Zmienna przechowuje sumę. Na początku suma wynosi 0.
numbers_count = 0  # Zmienna przechowuje liczbę wpisanych wartości.

while True:  # Pętla działa bez końca, dopóki nie użyjemy break.
    # Pobieramy liczbę od użytkownika i zamieniamy ją na liczbę całkowitą.
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:  # Sprawdzamy, czy użytkownik wpisał 0.
        break  # break natychmiast kończy działanie pętli.

    total_sum += number  # Dodajemy podaną liczbę do dotychczasowej sumy.
    numbers_count += 1  # Zwiększamy licznik wpisanych liczb o 1.

print(f"The total sum of the numbers is: {total_sum}") #f-string wstawia wartość zmiennej do tekstu przez {}.

# Sprawdzamy, czy użytkownik wpisał przynajmniej jedną liczbę.
if numbers_count > 0:
    # Średnia to suma podzielona przez liczbę wpisanych wartości.
    average = total_sum / numbers_count
    print(f"The arithmetic mean is: {average}")
else:
    # Jeżeli użytkownik od razu wpisał 0, nie można obliczyć średniej.
    print("No numbers were entered, so the average cannot be calculated.")