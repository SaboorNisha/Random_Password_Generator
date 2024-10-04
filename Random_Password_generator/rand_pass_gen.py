import random
import string

# Function to generate a random password
def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    # Create character pools based on user preferences
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters  # Includes both lowercase and uppercase letters
    if use_numbers:
        characters += string.digits  # Includes numbers (0-9)
    if use_symbols:
        characters += string.punctuation  # Includes symbols (!, @, #, $, etc.)

    # Ensure at least one character type is selected
    if not characters:
        print("You must select at least one character type (letters, numbers, or symbols).")
        return ""

    # Randomly generate the password from the selected characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main function for the command-line tool
def main():
    print("Welcome to the Random Password Generator!")

    # Get the desired password length from the user
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 1:
                print("Please enter a positive integer for the length.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Ask the user if they want to include letters, numbers, and symbols
    use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    # Generate the password based on user-defined criteria
    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if password:
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
