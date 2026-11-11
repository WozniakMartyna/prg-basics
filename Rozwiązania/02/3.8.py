# W tym zadaniu program ma obliczać średnią ocen ucznia. W oryginalnym kodzie znajduje się kilka błędów:
# mat powinno być math – nazwa zmiennej jest nieprawidłowa.
# Art powinno być art – Python rozróżnia małe i wielkie litery.
# muzic powinno być music – błędna nazwa zmiennej.
# Ocena z historii jest tekstem '3', a powinna być liczbą 3.
# Zamiast odejmowania - powinno być dodawanie +, ponieważ obliczamy średnią ocen.
# Sumę ocen trzeba podzielić przez 4.
# W ostatnim print() cudzysłowy są nieprawidłowo zapisane, a averege powinno być average.

# A program that calculates and prints the average grade of a student.
# Program oblicza i wyświetla średnią ocen ucznia.

# Zapisujemy ocenę z matematyki.
math = 5

# Zapisujemy ocenę ze sztuki.
art = 4

# Zapisujemy ocenę z muzyki.
music = 5

# Zapisujemy ocenę z historii jako liczbę całkowitą.
history = 3

# Dodajemy wszystkie oceny i dzielimy sumę przez ich liczbę.
average = (math + art + music + history) / 4

# Wyświetlamy obliczoną średnią ocen.
print("Average grade is", average)