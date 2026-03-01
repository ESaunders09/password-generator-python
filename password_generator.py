import random, pyperclip

# Define characters that can be in the password
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&()_+-="
all_chars = letters + numbers + symbols # Combine everything


# Use validation to check for invalid inputs
while True:
    # Ask the user for the number of passwords they want
    num_passwords = input("How many passwords do you want? ")
    try:
        num_passwords = int(num_passwords)
        if num_passwords <= 0:
            print("Invalid input, must be greater than 0.")
        else:
            break
    except ValueError:
        print("Invalid input, not a valid number.")

for p_num in range(num_passwords):
    password = ""
    # Use validation to check for invalid inputs
    while True:
        # Ask the user how long they want the password
        length = input("How long do you want your password to be? ")
        try:
            length = int(length)
            if length <= 0:
                print("Invalid input, must be greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid input, not a valid number.")


    print("Password length set to:", length)

    # Generate the random password
    for _ in range(length):
        password += random.choice(all_chars)
    print("Your password #" + str((p_num+1)), "is:", password)
    copy_check = input("Would you like to copy this password to clipboard? (y/n) ")
    if copy_check.upper() == "Y":
        pyperclip.copy(password)
        print("Password copied to clipboard!")
    else:
        print("Password not copied.")