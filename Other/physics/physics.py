def electric_field(k, q, x_q, y_q, x_p, y_p):
    try:
        r_x = x_p - x_q
        r_y = y_p - y_q
        r = (r_x**2 + r_y**2)**0.5
        if r == 0:
            print("Error: Point and charge cannot be at the same location.")
            return None, None
        else:
            e = k * q / r**2
            ex = e * r_x / r
            ey = e * r_y / r
            return ex, ey
    except ValueError as e:
        print(f"Error: {e}")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input, please enter a number.")

def get_coordinates_input(prompt, other_coordinates=None):
    while True:
        try:
            x, y = map(float, input(prompt).split())
            if other_coordinates is not None and x == other_coordinates[0] and y == other_coordinates[1]:
                print("Invalid input, charge and point cannot be at the same location. Please enter different coordinates.")
            else:
                return x, y
        except ValueError:
            print("Invalid input, please enter two numbers separated by space.")

# Main program
k = 9e9  # Coulomb's constant

q = get_float_input("Enter charge q (in coulombs): ")
x_q, y_q = get_coordinates_input("Enter charge coordinates x_q, y_q (separated by space): ")
x_p, y_p = get_coordinates_input("Enter point coordinates x_p, y_p (separated by space): ", other_coordinates=(x_q, y_q))

ex, ey = electric_field(k, q, x_q, y_q, x_p, y_p)
if ex is not None and ey is not None:
    print("Electric Field Components at the Point: Ex = {:.2e} N/C, Ey = {:.2e} N/C".format(ex, ey))