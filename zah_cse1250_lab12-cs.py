# Zachary A. Hampton
# Lab Section 83005
# Date 11-19-2023
# Lab 12

# This program will convert degrees Celsius to degrees Fahrenheit.

# define a function to display a user greeting
def user_greeting():
    # Welcome message and user instructions for program
    print("This program will convert degrees Celsius to degrees Fahrenheit.")
    print("Please enter the temperature in Celsius; you may use decimals.")
    print()

# define a function to ask the user if they want to run the program again
def ask_again():
    while True:
        response = input("Do you want to run the program again? (yes/no): ")
        if response.lower() in ['yes', 'no']:
            return response.lower() == 'yes'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Call the User Greeting function
user_greeting()

# Initialize a variable to control the main program loop
run_program = True

# Main program loop
while run_program:
    try:
        # Get user input for degrees Celsius and convert to float, while checking for errors
        celsius = float(input("Enter a temperature in degrees Celsius: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Perform arithmetic operations and store results in variables
    fahrenheit = (celsius * 9/5) + 32

    # Display results
    print()
    print(f"{celsius} degrees Celsius is equal to {fahrenheit:.1f} degrees Fahrenheit.")
    print()

    # Ask the user if they want to run the program again
    run_program = ask_again()

# Exit message
print("Have a great day!")
