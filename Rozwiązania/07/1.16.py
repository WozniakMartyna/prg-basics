# ZADANIE: Posortuj trzy listy za pomocą gotowej funkcji sorted().
#
# 1. Odległości – od najmniejszej do największej.
# 2. Temperatury – od największej do najmniejszej.
# 3. Nazwy plików – alfabetycznie.

# Lista przechowująca pokonane odległości.
distances_traveled = [120, 150, 180, 90, 200, 175, 160]

# sorted() zwraca nową listę posortowaną rosnąco.
# Najmniejsza wartość znajdzie się na początku.
sorted_distances = sorted(distances_traveled)

print("Distances ascending:", sorted_distances)


# Lista zawierająca temperatury z kolejnych dni.
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]

# Argument reverse=True odwraca kolejność sortowania.
# Dzięki temu otrzymujemy kolejność malejącą.
sorted_temperatures = sorted(daily_temperatures, reverse=True)

print("Temperatures descending:", sorted_temperatures)


# Lista zawierająca nazwy plików.
file_names = [
    "report.docx",
    "presentation.pptx",
    "data.csv",
    "photo.jpg",
    "notes.txt",
    "invoice.pdf",
    "resume.docx",
    "budget.xlsx",
    "meeting.mp4",
    "schedule.pdf"
]

# Sortujemy nazwy plików alfabetycznie.
# Ponieważ nie podajemy reverse=True, sortowanie jest rosnące.
sorted_file_names = sorted(file_names)

print("File names ascending:", sorted_file_names)