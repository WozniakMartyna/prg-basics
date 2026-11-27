# import queue

# create a visited_websites
# visited_websites = queue.LifoQueue()

# some previously visited websites
# visited_websites.put('instagram.com')
# visited_websites.put('uek.krakow.pl')
# visited_websites.put('microsoft.com')

# while True:
#   website = input('Enter website name (0 for back): ')

#   if website == '0':
#      if visited_websites.empty():
#         break
#      else:
#         print('<-- Going back to a previously visited website')
#         website = ...
#   elif ... != "":
#      ...
#
#   # print name of website you are currently viewing
#   print('You are currently viewing:', website)
#   print()

# Plik back.py przed modyfikacją ^


# ZADANIE 3.2:
# Symulacja przycisku Back w przeglądarce za pomocą stosu.

import queue

# Tworzymy stos odwiedzonych stron.
visited_websites = queue.LifoQueue()

# Dodajemy wcześniej odwiedzone strony.
visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

while True:
    website = input('Enter website name (0 for back): ')

    # Jeśli użytkownik wpisze 0, wykonujemy cofanie.
    if website == '0':

        # Jeśli stos jest pusty, kończymy program.
        if visited_websites.empty():
            break
        else:
            print('<-- Going back to a previously visited website')

            # Pobieramy poprzednią stronę ze stosu.
            website = visited_websites.get()

    # Jeśli użytkownik wpisał nazwę strony,
    # dodajemy ją na stos.
    elif website != "":
        visited_websites.put(website)

    # Wyświetlamy aktualnie odwiedzaną stronę.
    print('You are currently viewing:', website)
    print()


# W oryginalnym kodzie były dwa miejsca do uzupełnienia:
# - website = ... → website = visited_websites.get()
# - elif ... != "": → elif website != "":
# - ... → visited_websites.put(website)
# Ważne: get() pobiera i usuwa ostatnią stronę ze stosu, natomiast put() dodaje nową stronę.