
# ZADANIE 4.5:
# Główny program wyświetlający informacje z wiadomości e-mail.

from emails import email_sender, email_recipient, email_subject, email_body
# Importujemy cztery funkcje z naszego modułu emails.py.
# Oba pliki .py muszą znajdować się w tym samym folderze.

print("SENDER:")
print(email_sender())

print("\nRECIPIENT:")
print(email_recipient())

print("\nSUBJECT:")
print(email_subject())

print("\nBODY:")
print(email_body())


# do terminala
# # cd "Rozwiązania/08/4.5"
# python read_email.py