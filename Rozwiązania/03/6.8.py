# W tym zadaniu sprawdzamy, czy dwie osoby są pełnoletnie.
# Użytkownik podaje imiona i wiek obu osób.

# input() pobiera imię jako tekst.
person1_name = input('Enter first person name: ')

# input() pobiera wiek jako tekst, dlatego używamy int(), aby zamienić go na liczbę całkowitą.
person1_age = int(input('Enter first person age: '))

person2_name = input('Enter second person name: ')
person2_age = int(input('Enter second person age: '))

# Operator and wymaga, aby oba warunki były prawdziwe.
# Oznacza to, że pierwsza i druga osoba muszą mieć co najmniej 18 lat.
if person1_age >= 18 and person2_age >= 18:
    # f-string pozwala wstawić wartości zmiennych do tekstu za pomocą nawiasów klamrowych {}.
    print(f'Both {person1_name} and {person2_name} are adults')
else:
    # else wykonuje się, jeśli przynajmniej jedna osoba nie jest pełnoletnia.
    print(f'Either {person1_name} or {person2_name} is not an adult')