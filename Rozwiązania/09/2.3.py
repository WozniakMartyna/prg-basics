# ZADANIE 09.2.3:
# Znalezienie uczniów, którzy są nieobecni.

# Zbiór wszystkich uczniów w klasie.
all_students = {"Alice", "John", "Sara", "Bob"}

# Zbiór uczniów, którzy przyszli na lekcję.
attended_students = {"Alice", "Bob"}

# Operator - zwraca elementy pierwszego zbioru,
# których nie ma w drugim zbiorze.
absent_students = all_students - attended_students

# Wyświetlamy uczniów nieobecnych.
print("Absent students:", absent_students)


# all_students - attended_students oznacza: wszyscy uczniowie minus uczniowie obecni. Pozostają osoby nieobecne.