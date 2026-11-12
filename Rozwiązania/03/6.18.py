# Program sprawdza, w której ćwiartce układu współrzędnych
# znajduje się punkt o współrzędnych x i y.
# Uwzględnia również osie oraz początek układu współrzędnych.

# input() pobiera dane jako tekst, a int() zamienia je na liczby całkowite.
x = int(input('Enter x: '))
y = int(input('Enter y: '))

# Najpierw sprawdzamy, czy punkt jest początkiem układu współrzędnych.
# and oznacza "i" – oba warunki muszą być prawdziwe.
if x == 0 and y == 0:
    print('Point is at the origin')

# Jeśli x wynosi 0, punkt znajduje się na osi Y.
elif x == 0:
    print('Point is on the Y axis')

# Jeśli y wynosi 0, punkt znajduje się na osi X.
elif y == 0:
    print('Point is on the X axis')

# x > 0 oznacza dodatnią wartość x, a y > 0 dodatnią wartość y.
# Punkt znajduje się wtedy w pierwszej ćwiartce.
elif x > 0 and y > 0:
    print('Point is in the first quadrant')

# Ujemne x i dodatnie y oznaczają drugą ćwiartkę.
elif x < 0 and y > 0:
    print('Point is in the second quadrant')

# Ujemne x i ujemne y oznaczają trzecią ćwiartkę.
elif x < 0 and y < 0:
    print('Point is in the third quadrant')

# Jeśli żaden wcześniejszy warunek nie pasuje,
# punkt znajduje się w czwartej ćwiartce.
else:
    print('Point is in the fourth quadrant')