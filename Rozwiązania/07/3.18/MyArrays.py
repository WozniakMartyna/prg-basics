# ZADANIE 3.18:
# Moduł zawierający funkcje do wykonywania operacji na listach.

# Funkcja zwraca drugi największy RÓŻNY element listy.
def second_largest(array):

    # Tworzymy kopię listy, aby nie zmieniać oryginału.
    numbers = array.copy()

    # Sortujemy kopię metodą bąbelkową, bez używania sort() i sorted().
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    # Przechodzimy od końca listy w poszukiwaniu wartości
    # mniejszej od największej.
    largest = numbers[-1]

    for i in range(len(numbers) - 2, -1, -1):
        if numbers[i] < largest:
            return numbers[i]

    # Jeżeli nie ma drugiej różnej wartości, zwracamy None.
    return None


# Funkcja oblicza różnicę między największym i najmniejszym elementem.
def difference(array):

    # Przyjmujemy pierwszy element jako początkowe minimum i maksimum.
    smallest = array[0]
    largest = array[0]

    # Sprawdzamy wszystkie elementy listy.
    for number in array:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

    return largest - smallest


# Funkcja oblicza medianę listy.
def median(array):

    # Tworzymy kopię, aby nie zmieniać oryginalnej listy.
    numbers = array.copy()

    # Sortujemy listę rosnąco metodą bąbelkową.
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    # Obliczamy środkowy indeks.
    middle = len(numbers) // 2

    # Jeżeli liczba elementów jest nieparzysta,
    # mediana jest środkowym elementem.
    if len(numbers) % 2 == 1:
        return numbers[middle]

    # Jeżeli liczba elementów jest parzysta,
    # mediana jest średnią dwóch środkowych elementów.
    return (numbers[middle - 1] + numbers[middle]) / 2


# Funkcja zwraca listę zawierającą minimum i maksimum.
def min_max(array):

    smallest = array[0]
    largest = array[0]

    for number in array:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

    return [smallest, largest]


# Funkcja zamienia elementy listy na tekst oddzielony myślnikami.
def as_string(array):

    # Zamieniamy pierwszy element na tekst.
    result = str(array[0])

    # Kolejne elementy dopisujemy z myślnikiem.
    for i in range(1, len(array)):
        result += "-" + str(array[i])

    return result