import random

# Define characters that can be in the password
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&()_+-="
all_chars = letters + numbers + symbols # Combine everything

#Ask the user for the number of passwords they want
numPasswords = int(input("How many passwords do you want? "))

for _ in range(numPasswords):
    # Ask the user how long they want the password
    length = int(input("How long do you want your password to be? "))
    print("Password length set to:", length)

    # Generate the random password
    password = ""
    for _ in range(length):
        password += random.choice(all_chars)
    print("Your password is:", password)