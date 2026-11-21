# ZADANIE: Wyświetl informacje o elementach listy.

arr = [2, 3, 7, 5, 4]

# 1. Wyświetlenie całej listy.
print("Array:", arr)

# 2. len() zwraca liczbę elementów listy.
print("Number of elements:", len(arr))

# 3. Pierwszy element ma indeks 0.
print("First value:", arr[0])

# 4. Drugi element ma indeks 1.
print("Second value:", arr[1])

# 5. Ostatni element – indeks to długość listy minus 1.
print("Last value:", arr[len(arr) - 1])

# 6. Przedostatni element – nie używamy indeksu ujemnego.
print("Last but one value:", arr[len(arr) - 2])

# 7. Dodajemy pierwszy i ostatni element.
print("Sum of first and last value:", arr[0] + arr[len(arr) - 1])

# 8. Środkowy element.
# len(arr) // 2 oznacza dzielenie całkowite: 5 // 2 = 2.
print("Middle value:", arr[len(arr) // 2])

# 9. Wyświetlamy wszystkie elementy za pomocą pętli for.
print("All values:", end=" ")

for value in arr:
    print(value, end=" ")  # end=" " zastępuje domyślny znak nowej linii spacją.

print()  # Przejście do nowej linii po zakończeniu pętli.