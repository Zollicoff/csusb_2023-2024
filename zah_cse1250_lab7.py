# Zachary Hampton
# Lab Section 83005
# Date: October 8, 2023
# Lab 7

# This program prompts the user to enter either 'A', 'B', or 'C', and displays a corresponding word.

# Welcome message salutation
print("Welcome to the fruit program!\n")

# Get user input and apply to fruit variable
while True:
    fruit = input("Please enter 'A' for Apple, 'B' for Banana, or 'C' for Coconut: ")
    if fruit in ['A', 'B', 'C']:
        break
    else:
        print("Invalid input. Please enter 'A', 'B', or 'C'.")

# Check user input and display corresponding word
if fruit == 'A':
    print("\nYou got an Apple!")
elif fruit == 'B':
    print("\nYou got a Banana!")
elif fruit == 'C':
    print("\nYou got a Coconut!")

# Exit message salutation
print("\nThank you for using the fruit program.\n\n"
      "Have a nice day!")

input("\nPress enter to exit the program...")