# ZADANIE 09.2.4:
# Znalezienie wiadomości, których adresy znajdują się na liście spamu.

# Zbiór odebranych adresów e-mail.
emails_received = {
    "john@example.com",
    "spam1@example.com",
    "spam2@example.com",
    "jane@example.com"
}

# Zbiór adresów oznaczonych jako spam.
spam_list = {
    "spam1@example.com",
    "spam2@example.com"
}

# Operator & zwraca elementy występujące w obu zbiorach.
spam_emails = emails_received & spam_list

# Wyświetlamy znalezione adresy spamowe.
print("Spam emails:", spam_emails)


# emails_received & spam_list oznacza część wspólną obu zbiorów. Adres musi znajdować się w obu, aby pojawił się w wyniku.