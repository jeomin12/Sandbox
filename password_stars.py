MIN_LENGTH= 8
password = input("Enter password: ")

while len(password) < MIN_LENGTH:
    print("Password too short! Try again.")
    password = input("Enter password (minimum {} characters): ")

print("*" * len(password))