# Zachary Hampton
# Lab Section 83005
# October 22, 2023
# Lab 8

# This program lets a user do calculations with two numbers.
# The calculations include: addition, subtraction, multiplication, division, truncating division, and exponentiation.

# User greeting
print("\nWelcome to the Number Calculator!")
print("You can perform calculations with two numbers.")
print("Enter '+' for addition, '-' for subtraction, '*' for multiplication, '/' for division, '//' for truncating division, and '**' for exponentiation.\n")

# Initialize a variable to control the Program Loop
run_program = 'Y'

while run_program.upper() == 'Y':
    # Get the user input for the type of calculation
    operation = input("Please enter the operation you want to perform: ").lower()

    # Error check this input using a while loop
    while operation not in ['+', '-', '*', '/', '//', '**']:
        operation = input("Invalid input. Please enter '+', '-', '*', '/', '//', or '**': ").lower()

    # Get the user input for first and second number
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the appropriate calculation and assign the correct words to the variable
    if operation == '+':
        result = num1 + num2
        message = 'plus'
    elif operation == '-':
        result = num1 - num2
        message = 'minus'
    elif operation == '*':
        result = num1 * num2
        message = 'multiplied by'
    elif operation == '/':
        result = num1 / num2
        message = 'divided by'
    elif operation == '//':
        result = num1 // num2
        message = 'truncating division by'
    elif operation == '**':
        result = num1 ** num2
        message = 'raised to the power of'

    # Display and format the answer
    print("\n{} {} {} equals {:,}\n".format(num1, message, num2, result))

    # Ask the user if they want to run the program again
    run_program = input("Do you want to run the program again? (Y/N): ")

    # Error check this input
    while run_program.upper() not in ['Y', 'N']:
        run_program = input("Invalid input. Please enter 'Y' or 'N': ")

# Display an exit message
print("\nThank you for using the Number Calculator. Goodbye!\n")