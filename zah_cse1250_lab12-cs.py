# Zachary A. Hampton
# Lab Section 83005
# Date 11-19-2023
# Lab 12

# This program converts temperatures between Celsius, Fahrenheit, and Kelvin

# define a function to display a user greeting
def user_greeting():
    # Welcome message and display user instructions for program
    print("Hello and welcome to the temperature conversion program!"
          "\n\nThis program can convert Celsius, Farenheit, and Kelvin temperatures. "
          "Please enter numbers and decimals only.")

# define a function to ask the user if they want to run the program again, while checking for errors
def ask_again():
    while True:
        response = input("Do you want to run the program again? (yes/no): ")
        if response.lower() in ['yes', 'no']:
            return response.lower() == 'yes'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# define a function to get the conversion type from the user, while checking for errors
def get_conversion_type():
    while True:
        input_scale = input("\nEnter the scale of the input temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ")
        output_scale = input("Enter the scale of the output temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ")
        if input_scale.upper() in ['C', 'F', 'K'] and output_scale.upper() in ['C', 'F', 'K']:
            if input_scale.upper() != output_scale.upper():
                return input_scale.upper(), output_scale.upper()
            else:
                print("Invalid input. Please select two different temperature scales for conversion.")
        else:
            print("Invalid input. Please enter 'C', 'F', or 'K'.")

# Define the main program function
def main_program():
    # Get the conversion type
    input_scale, output_scale = get_conversion_type()

    # Get user input for temperature and convert to float, while checking for errors
    while True:
        try:
            temperature = float(input(f"\nEnter a temperature in degrees {input_scale}: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Perform arithmetic operations and store results in variables
    if input_scale == 'C' and output_scale == 'F':
        converted_temperature = (temperature * 9/5) + 32
    elif input_scale == 'F' and output_scale == 'C':
        converted_temperature = (temperature - 32) * 5/9
    elif input_scale == 'K' and output_scale == 'C':
        converted_temperature = temperature - 273.15
    elif input_scale == 'C' and output_scale == 'K':
        converted_temperature = temperature + 273.15
    elif input_scale == 'F' and output_scale == 'K':
        converted_temperature = (temperature + 459.67) * 5/9
    elif input_scale == 'K' and output_scale == 'F':
        converted_temperature = (temperature * 9/5) - 459.67
    else: # input_scale == output_scale
        converted_temperature = temperature

    print(f"\n{temperature} degrees {input_scale} is equal to {converted_temperature:.1f} degrees {output_scale}.\n")

    # Ask the user if they want to run the program again
    return ask_again()

# Call the User Greeting function
user_greeting()

# Initialize run_program variable and call the main program function
run_program = True

while run_program:
    run_program = main_program()

# Exit message
print("\nHave a great day!")
