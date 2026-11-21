# ZADANIE: Posortuj listę liczb za pomocą algorytmu Bubble Sort.
#
# Algorytm porównuje sąsiednie elementy listy.
# Jeżeli lewy element jest większy od prawego,
# zamienia je miejscami.
# Proces powtarzamy, aż lista będzie uporządkowana.

def bubble_sort(arr):
    # len(arr) zwraca liczbę elementów listy.
    # Zapisujemy tę liczbę w zmiennej n.
    n = len(arr)

    # Pierwsza pętla określa liczbę przebiegów algorytmu.
    # range(n) generuje liczby od 0 do n-1.
    for i in range(n):

        # Druga pętla porównuje sąsiednie elementy.
        # Po każdym przebiegu największy element trafia na koniec.
        # Dlatego nie musimy ponownie sprawdzać ostatnich i elementów.
        for j in range(n - i - 1):

            # Sprawdzamy, czy lewy element jest większy od prawego.
            if arr[j] > arr[j + 1]:

                # Zamieniamy elementy miejscami.
                # Python pozwala przypisać dwie wartości jednocześnie.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Zwracamy posortowaną listę.
    return arr


# Lista przedstawiająca zużycie paliwa samochodów.
car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]

print("Fuel consumption before sorting:", car_fuel_consumption)

# Wywołujemy funkcję bubble_sort().
# Funkcja zmienia kolejność elementów listy.
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)

print("Fuel consumption after sorting:", sorted_car_fuel_consumption)


# Lista przedstawiająca transakcje bankowe.
# Wartości ujemne oznaczają wydatki, a dodatnie wpływy.
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]

print("Transactions before sorting:", bank_transactions)

# Sortujemy transakcje rosnąco.
sorted_bank_transactions = bubble_sort(bank_transactions)

print("Transactions after sorting:", sorted_bank_transactions)