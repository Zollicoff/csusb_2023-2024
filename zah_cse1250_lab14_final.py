# Zachary A. Hampton
# Lab 83005
# 12-08-2023
# Lab 14 Final

# This program calculates the total due for a shipment of products.

# Define user greeting function
def user_greeting():
    print("This program lets the user enter products to be shipped and calculates the subtotal, tax, shipping and handling, and the total due.")

# Define get product info function
def get_product_info():
    product_info = []
    item_quantity = 1
    while item_quantity != 0:
        item_quantity = int(input("\nEnter item quantity (enter 0 if done): "))
        if item_quantity != 0:
            item_weight = float(input("Enter item weight: "))
            item_cost = float(input("Enter cost of item: "))
            product_info.append([item_quantity, item_weight, item_cost])
    return product_info

# Define get state function
def get_state():
    states = ['CA']
    state = input("Enter your state abbreviation: ")
    while state not in states:
        state = input("Invalid state. Please enter a valid state abbreviation: ")
    return state

# Define calculate function
def calculate(product_info):
    box_weight = 0
    sub_total = 0
    for item in product_info:
        item_quantity, item_weight, item_cost = item
        box_weight += item_quantity * item_weight
        sub_total += item_quantity * item_cost
    shipping_cost = box_weight * .25
    if box_weight < 10:
        handling = 1
    elif box_weight > 100:
        handling = 5
    else:
        handling = 3
    shipping_handling = shipping_cost + handling
    return sub_total, shipping_handling

# Define run again function
def run_again():
    run = input("Would you like to run the program again? (y/n): ")
    while run not in ['y', 'n']:
        run = input("Invalid input. Please enter 'y' or 'n': ")
    return run == 'y'

# Define main function
def main():
    user_greeting()
    run_program = True
    while run_program:
        product_info = get_product_info()
        sub_total, shipping_handling = calculate(product_info)
        state = get_state()
        tax = sub_total * .08 if state == 'CA' else 0
        total_due = sub_total + shipping_handling + tax
        print(format('Subtotal:', '<25'), format(sub_total, '>10,.2f'))
        print(format('Tax:', '<25'), format(tax, '>10,.2f'))
        print(format('Shipping and Handling:', '<25'), format(shipping_handling, '>10,.2f'))
        print(format('Total Due:', '<25'), format(total_due, '>10,.2f'))
        run_program = run_again()

# Call main function
if __name__ == "__main__":
    main()
