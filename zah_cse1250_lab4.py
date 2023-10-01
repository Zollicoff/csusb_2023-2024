# Zachary Hampton
# October 1, 2023
# Lab Section 83005
# Lab 4

# This program lets a user enter two integers and displays the results of all arithmetic operations

# Welcome message and user instructions for program
print("This program will let you enter two integer values "
      "then it will show you all of the possible answers.")
print("Please enter only whole numbers.")
print()

# Get user input for two integers
num1 = int(input("Please enter the first integer: "))
num2 = int(input("Please enter the second integer: "))
print()

# Perform arithmetic operations and store results in variables
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponentiation = num1 ** num2

# Display results
print(f"{num1} + {num2} = {addition:,}")
print(f"{num1} - {num2} = {subtraction:,}")
print(f"{num1} * {num2} = {multiplication:,}")
print(f"{num1} / {num2} = {division:,.2f}")
print(f"{num1} // {num2} = {floor_division:,}")
print(f"{num1} % {num2} = {modulus:,}")
print(f"{num1} ** {num2} = {exponentiation:,}")
print()

# end of program salutation
print("Have a great day!")
print()

# Require user to press enter to exit program
input("Press Enter to exit the program...")
