# Należy uzupełnić warunki tak, aby program informował, czy podana liczba jest za mała, za duża, czy prawidłowa.
# Prosta gra polegająca na zgadywaniu liczby.

import random  # Importujemy moduł random, który pozwala losować liczby.

# random.randint(1, 100) losuje liczbę całkowitą od 1 do 100. Obie granice są wliczone. 
number_to_guess = random.randint(1, 100)

# Na początku ustawiamy zgadywaną liczbę na 0.
# Dzięki temu pętla rozpocznie działanie.
user_guess = 0

print("Guess the number between 1 and 100!")

# Pętla działa, dopóki wpisana liczba nie będzie równa wylosowanej.
while user_guess != number_to_guess:
    # while user_guess != number_to_guess powtarza grę, dopóki liczby nie są równe (czyli są różne)
    # Pobieramy liczbę od użytkownika i zamieniamy tekst na liczbę całkowitą (za pomocą int ()).
    user_guess = int(input("Enter your guess: "))

    # Sprawdzamy, czy podana liczba jest mniejsza od wylosowanej.
    if user_guess < number_to_guess:
        # if sprawdza pierwszy warunek.
        print("Too low! Try again.")

    # Jeśli pierwszy warunek jest fałszywy, sprawdzamy, czy liczba jest większa.
    elif user_guess > number_to_guess:
        # elif sprawdza kolejny warunek, jeżeli wcześniejszy nie został spełniony.
        print("Too high! Try again.")

    # Jeżeli liczba nie jest ani mniejsza, ani większa, musi być równa.
    else:
        # else wykonuje się, gdy żaden wcześniejszy warunek nie jest prawdziwy.
        print("Congratulations! You guessed the correct number.")

    # Wcięcia określają, które instrukcje należą do pętli i poszczególnych warunków.