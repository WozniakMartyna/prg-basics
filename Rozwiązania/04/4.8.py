# ZADANIE 4.8
# Należy napisać funkcję time_string(hours, minutes, time_format),
# która zamienia podaną godzinę i minuty na tekst.
#
# Funkcja ma obsługiwać dwa formaty:
# '24' - format 24-godzinny, np. 15:38.
# '12' - format 12-godzinny, np. 3:38pm.
#
# Godziny są z zakresu 0-23, a minuty z zakresu 0-59.
# Na końcu należy sprawdzić funkcję dla przykładów z polecenia.


# def tworzy funkcję o nazwie time_string.
# hours, minutes i time_format to parametry funkcji.
def time_string(hours, minutes, time_format):

    # Sprawdzamy, czy użytkownik chce format 24-godzinny.
    if time_format == '24':

        # f przed cudzysłowem oznacza, że używamy f-stringa.
        # Wartości zmiennych umieszczamy w nawiasach klamrowych {}.
        # :02d oznacza wyświetlenie liczby całkowitej na co najmniej
        # dwóch miejscach, z zerem z przodu, jeśli jest potrzebne.
        # Dzięki temu np. 8 zostanie wyświetlone jako 08.
        return f'{hours:02d}:{minutes:02d}'

    # Sprawdzamy, czy użytkownik chce format 12-godzinny.
    elif time_format == '12':

        # Dla godziny 0 wyświetlamy 12 i oznaczenie am.
        if hours == 0:
            display_hour = 12
            suffix = 'am'

        # Dla godzin od 1 do 11 zostawiamy numer godziny
        # i dodajemy oznaczenie am.
        elif hours < 12:
            display_hour = hours
            suffix = 'am'

        # Godzina 12 pozostaje 12 i otrzymuje oznaczenie pm.
        elif hours == 12:
            display_hour = 12
            suffix = 'pm'

        # Dla godzin większych niż 12 odejmujemy 12.
        # Dodajemy oznaczenie pm.
        else:
            display_hour = hours - 12
            suffix = 'pm'

        # f przed cudzysłowem oznacza f-string.
        # {display_hour} wstawia numer godziny.
        # {minutes:02d} wyświetla minuty na dwóch miejscach,
        # np. 5 jako 05.
        # {suffix} wstawia oznaczenie am albo pm.
        return f'{display_hour}:{minutes:02d}{suffix}'


# Testujemy funkcję dla formatu 24-godzinnego.
print(time_string(15, 38, '24'))  # Wynik: 15:38
print(time_string(8, 3, '24'))    # Wynik: 08:03
print(time_string(0, 5, '24'))    # Wynik: 00:05

# Testujemy funkcję dla formatu 12-godzinnego.
print(time_string(11, 15, '12'))  # Wynik: 11:15am
print(time_string(0, 7, '12'))    # Wynik: 12:07am
print(time_string(7, 30, '12'))   # Wynik: 7:30am
print(time_string(12, 46, '12'))  # Wynik: 12:46pm
print(time_string(13, 10, '12'))  # Wynik: 1:10pm
print(time_string(19, 2, '12'))   # Wynik: 7:02pm


# - Co robi return? Zwraca wynik funkcji i kończy jej działanie.
# - Co oznacza ==? Porównuje dwie wartości.
# - Co oznacza f przed tekstem? Tworzy f-string, w którym można
#   wstawiać wartości zmiennych za pomocą nawiasów klamrowych {}.
# - Co oznacza :02d? Wyświetla liczbę całkowitą na co najmniej
#   dwóch miejscach, dodając zero z przodu, jeśli potrzeba.
# - Dlaczego dla godziny 0 wyświetlamy 12? W formacie 12-godzinnym
#   północ zapisujemy jako 12:00am.
# - Dlaczego dla godziny większej niż 12 odejmujemy 12?
#   Ponieważ format 12-godzinny liczy godziny od 1 do 12.
# - W przykładzie z polecenia zapis 19, 02 należy w Pythonie
#   zapisać jako 19, 2. Liczby całkowite dziesiętne nie powinny
#   mieć zera na początku.
#
# Uwaga: funkcja zakłada poprawne dane wejściowe zgodnie z poleceniem:
# godziny 0-23, minuty 0-59, format '12' albo '24'.