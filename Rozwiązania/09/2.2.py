# ZADANIE 2.2:
# Usunięcie powtarzających się adresów e-mail za pomocą zbioru.

# Lista zawiera cztery adresy, ale jeden z nich występuje dwa razy.
emails = [
    "john@example.com",
    "jane@example.com",
    "john@example.com",
    "alex@example.com"
]

# set() zamienia listę na zbiór.
# Zbiór automatycznie usuwa powtarzające się elementy.
unique_emails = set(emails)

# Wyświetlamy zbiór bez duplikatów.
print(unique_emails)


# set(emails) – tworzy zbiór na podstawie listy.
# Zbiór nie przechowuje duplikatów.
# Kolejność wyświetlania elementów zbioru nie jest gwarantowana.