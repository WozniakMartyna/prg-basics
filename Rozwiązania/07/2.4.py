# ZADANIE:
# Wyświetlenie tygodniowego planu posiłków.
# Każdy wiersz listy zawiera śniadanie, obiad i kolację.

# Tworzymy listę dwuwymiarową.
# Każdy wiersz oznacza kolejny dzień tygodnia.
# W każdej liście znajdują się trzy posiłki:
# śniadanie, obiad i kolacja.
meal_plan = [
    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
    ["Pancakes", "Sandwich", "Steak"],
    ["Smoothie", "Chicken Wrap", "Salmon"],
    ["Eggs", "Pasta", "Soup"],
    ["Toast", "Burrito", "Pizza"],
    ["Cereal", "Salad", "Fish Tacos"],
    ["Bagel", "Rice and Beans", "Stir-fry"]
]


# Funkcja zwraca nazwę dnia tygodnia.
# Argument n oznacza numer dnia:
# 1 - Monday, 2 - Tuesday itd.
def weekday(n):

    # Lista nazw siedmiu dni tygodnia.
    weekdays = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]

    # Indeksowanie zaczyna się od 0.
    # Dlatego odejmujemy 1 od numeru dnia.
    # Dla n = 1 otrzymamy weekdays[0], czyli Monday.
    return weekdays[n - 1]


# Funkcja zwraca posiłki dla wybranego dnia.
# meal_plan - lista wszystkich posiłków.
# day_number - numer dnia od 1 do 7.
def day_meal_plan(meal_plan, day_number):

    # Pobieramy listę posiłków dla danego dnia.
    # Odejmujemy 1, ponieważ indeksy zaczynają się od 0.
    meals = meal_plan[day_number - 1]

    # Łączymy trzy posiłki w jeden tekst.
    # join() wstawia przecinek i spację pomiędzy elementy.
    # Przykład: ["Oatmeal", "Salad", "Spaghetti"]
    # zmienia się w "Oatmeal, Salad, Spaghetti".
    return ", ".join(meals)


# Wyświetlamy nagłówek planu.
print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
print("==========================")

# Pętla przechodzi po numerach dni od 1 do 7.
# range(1, 8) oznacza: zacznij od 1 i zakończ przed 8.
for day_number in range(1, 8):

    # Wywołujemy funkcję weekday(), aby uzyskać nazwę dnia.
    day_name = weekday(day_number)

    # Wywołujemy funkcję day_meal_plan(), aby pobrać posiłki.
    meals = day_meal_plan(meal_plan, day_number)

    # Wyświetlamy nazwę dnia i posiłki.
    print(day_name + ": " + meals)