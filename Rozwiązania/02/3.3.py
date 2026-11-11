# Na początku x = 7, a y = 34. Mamy zamienić te wartości miejscami. Do tego użyjemy dodatkowej zmiennej z.
# A program for swapping two variable values.
# Program zamienia wartości dwóch zmiennych miejscami.

# Przypisujemy początkowe wartości do zmiennych.
x = 7
y = 34

# Tworzymy dodatkową zmienną pomocniczą.
z = 0

# Wyświetlamy wartości przed zamianą.
print("Before swapping: x=", x, "y=", y)

# Zapisujemy wartość x w zmiennej pomocniczej z.
z = x

# Przepisujemy wartość y do zmiennej x.
x = y

# Przepisujemy zapisaną wcześniej wartość z do zmiennej y.
y = z

# Wyświetlamy wartości po zamianie.
print("After swapping: x=", x, "y=", y)