

import secrets
import string

print("🔐 Password Generator")

while True:
    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length must be at least 4.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(secrets.choice(characters) for _ in range(length))

print("Generated Password:", password)
