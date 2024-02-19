



def electric_fields_and_forces():
    # Function to solve problems related to electric fields and forces
    # Ask for known values
    q = float(input("Enter the charge (in Coulombs): "))
    r = float(input("Enter the distance from the charge (in meters): "))
    # Calculate the electric field
    E = k * q / r**2
    # Calculate the force
    F = k * q1 * q2 / r**2
    # Print the results
    print("The electric field at a distance of", r, "meters from the charge is", E, "N/C.")
    print("The force between two charges", q1, "C and", q2, "C at a distance of", r, "meters is", F, "N.")
    
def gauss_law_applications():
    # Function to solve problems related to Gauss's law applications
    # Ask for known values
    q = float(input("Enter the charge enclosed by the Gaussian surface (in Coulombs): "))
    A = float(input("Enter the area of the Gaussian surface (in square meters): "))
    # Calculate the electric field
    E = q / (epsilon0 * A)
    # Print the result
    print("The electric field through the Gaussian surface is", E, "N/C.")
    
def electric_potential_and_potential_energy():
    # Function to solve problems related to electric potential and potential energy
    # Ask for known values
    q = float(input("Enter the charge (in Coulombs): "))
    r = float(input("Enter the distance from the charge (in meters): "))
    # Calculate the electric potential
    V = k * q / r
    # Calculate the potential energy
    U = k * q1 * q2 / r
    # Print the results
    print("The electric potential at a distance of", r, "meters from the charge is", V, "V.")
    print("The potential energy between two charges", q1, "C and", q2, "C at a distance of", r, "meters is", U, "J.")
    
def capacitance_and_dielectrics():
    # Function to solve problems related to capacitance and dielectrics
    # Ask for known values
    A = float(input("Enter the area of the capacitor plates (in square meters): "))
    d = float(input("Enter the distance between the capacitor plates (in meters): "))
    k = float(input("Enter the dielectric constant: "))
    # Calculate the capacitance
    C = (k * epsilon0 * A) / d
    # Print the result
    print("The capacitance of the capacitor is", C, "F.")
    
def current_resistance_and_emf():
    # Function to solve problems related to current, resistance, and electromotive force
    # Ask for known values
    V = float(input("Enter the voltage (in volts): "))
    R = float(input("Enter the resistance (in ohms): "))
    # Calculate the current
    I = V / R
    # Print the result
    print("The current in the circuit is", I, "A.")
    
def direct_current_circuits():
    # Function to solve problems related to direct current circuits
    # Ask for known values
    V = float(input("Enter the voltage (in volts): "))
    R1 = float(input("Enter the resistance of the first resistor (in ohms): "))
    R2 = float(input("Enter the resistance of the second resistor (in ohms): "))
    # Calculate the equivalent resistance
    Req = R1 + R2
    # Calculate the current
    I = V / Req
    # Print the results
    print("The equivalent resistance of the circuit is", Req, "ohms.")
    print("The current in the circuit is", I, "A.")
    
def magnetic_fields_and_forces():
    # Function to solve problems related to magnetic fields and forces
    # Ask for known values
    I = float(input("Enter the current (in amperes): "))
    r = float(input("Enter the distance from the wire (in meters): "))
    # Calculate the magnetic field
    B = (mu0 * I) / (2 * pi * r)
    # Print the result
    print("The magnetic field at a distance of", r, "meters from the wire is", B, "T.")
    
def sources_of_the_magnetic_field():
    # Function to solve problems related to sources of the magnetic field
    # Ask for known values
    N = float(input("Enter the number of turns in the coil: "))
    I = float(input("Enter the current in the coil (in amperes): "))
    A = float(input("Enter the area of the coil (in square meters): "))
    # Calculate the magnetic field
    B = (mu0 * N * I) / A
    # Print the result
    print("The magnetic field inside the coil is", B, "T.")
    
def faradays_law():
    # Function to solve problems related to Faraday's law
    # Ask for known values
    N = float(input("Enter the number of turns in the coil: "))
    B = float(input("Enter the magnetic field (in teslas): "))
    A = float(input("Enter the area of the coil (in square meters): "))
    t = float(input("Enter the time interval (in seconds): "))
    # Calculate the induced emf
    emf = -N * B * A / t
    # Print the result
    print("The induced emf in the coil is", emf, "V.")
    
def inductance():
    # Function to solve problems related to inductance
    # Ask for known values
    N = float(input("Enter the number of turns in the coil: "))
    A = float(input("Enter the area of the coil (in square meters): "))
    l = float(input("Enter the length of the coil (in meters): "))
    mu = float(input("Enter the permeability of the material: "))
    # Calculate the inductance
    L = (mu * N**2 * A) / l
    # Print the result
    print("The inductance of the coil is", L, "H.")
    
def electromagnetic_oscillations_and_alternating_current():
    # Function to solve problems related to electromagnetic oscillations and alternating current
    # Ask for known values
    L = float(input("Enter the inductance (in henrys): "))
    C = float(input("Enter the capacitance (in farads): "))
    # Calculate the resonant frequency
    f = 1 / (2 * pi * (L * C)**0.5)
    # Print the result
    print("The resonant frequency of the circuit is", f, "Hz.")
    
def maxwells_equations_and_electromagnetic_waves():
    # Function to solve problems related to Maxwell's equations and electromagnetic waves
    # Ask for known values
    I = float(input("Enter the current (in amperes): "))
    A = float(input("Enter the area of the loop (in square meters): "))
    r = float(input("Enter the distance from the loop (in meters): "))
    # Calculate the magnetic field
    B = (mu0 * I * A) / (2 * pi * r**3)
    # Print the result
    print("The magnetic field at a distance of", r, "meters from the loop is", B, "T.")
    
# Constants
k = 8.99 * 10**9  # Coulomb's constant
epsilon0 = 8.85 * 10**-12  # Permittivity of free space
mu0 = 4 * pi * 10**-7  # Permeability of free space
pi = 3.14159  # Value of pi


# Introduction/Welcome Message
print("Welcome to the Physics 2 Problem Solver!")
print("Please select the type of problem you would like to solve:")
print("1. Electric Fields and Forces")
print("2. Gauss's Law Applications")
print("3. Electric Potential and Potential Energy")
print("4. Capacitance and Dielectrics")
print("5. Current, Resistance, and Electromotive Force")
print("6. Direct Current Circuits")
print("7. Magnetic Fields and Forces")
print("8. Sources of the Magnetic Field")
print("9. Faraday's Law")
print("10. Inductance")
print("11. Electromagnetic Oscillations and Alternating Current")
print("12. Maxwell's Equations and Electromagnetic Waves")

# Problem Selection
problem = int(input("Enter the number of the problem type you would like to solve: "))
if problem == 1:
    print("You have selected Electric Fields and Forces.")
    print("This problem type involves the calculation of electric fields and forces.")
    print("Please enter the known values and the program will calculate the unknown values.")
    # Call the function to solve the problem
    electric_fields_and_forces()
elif problem == 2:
    print("You have selected Gauss's Law Applications.")
    print("This problem type involves the application of Gauss's law to calculate electric fields.")
    print("Please enter the known values and the program will calculate the unknown values.")
    # Call the function to solve the problem
    gauss_law_applications()
elif problem == 3:
    print("You have selected Electric Potential and Potential Energy.")
    print("This problem type involves the calculation of electric potential and potential energy.")
    print("Please enter the known values and the program will calculate the unknown values.")
    # Call the function to solve the problem
    electric_potential_and_potential_energy()
elif problem == 4:  
    print("You have selected Capacitance and Dielectrics.")
    print("This problem type involves the calculation of capacitance and the effect of dielectrics.")
    print("Please enter the known values and the program will calculate the unknown values.")
    # Call the function to solve the problem
    capacitance_and_dielectrics()
elif problem == 5:
    print("You have selected Current, Resistance, and Electromotive Force.")
    print("This problem type involves the calculation of current, resistance, and electromotive force in circuits.")
    print("Please enter the known values and the program will calculate the unknown values.")
    # Call the function to solve the problem
    current_resistance_and_emf()
elif problem == 6:
    print("You have selected Direct Current Circuits.")
    print("This problem type involves the analysis of direct current circuits.")
    print("Please enter the known values and the program will calculate the unknown values.")
    # Call the function to solve the problem
    direct_current_circuits()
elif problem == 7:
    print("You have selected Magnetic Fields and Forces.")
    print("This problem type involves the calculation of magnetic fields and forces.")
    print("Please enter the known values and the program will calculate the unknown values.")
    # Call the function to solve the problem
    magnetic_fields_and_forces()
elif problem == 8:
    print("You have selected Sources of the Magnetic Field.")
    print("This problem type involves the analysis of sources of the magnetic field.")
    print("Please enter the known values and the program will calculate the unknown values.")
    # Call the function to solve the problem
    sources_of_the_magnetic_field()
elif problem == 9:
    print("You have selected Faraday's Law.")
    print("This problem type involves the application of Faraday's law to calculate induced emf and magnetic fields.")
    print("Please enter the known values and the program will calculate the unknown values.")
    # Call the function to solve the problem
    faradays_law()
elif problem == 10:
    print("You have selected Inductance.")
    print("This problem type involves the calculation of inductance in circuits.")
    print("Please enter the known values and the program will calculate the unknown values.")
    # Call the function to solve the problem
    inductance()
elif problem == 11:
    print("You have selected Electromagnetic Oscillations and Alternating Current.")
    print("This problem type involves the analysis of electromagnetic oscillations and alternating current circuits.")
    print("Please enter the known values and the program will calculate the unknown values.")
    # Call the function to solve the problem
    electromagnetic_oscillations_and_alternating_current()
elif problem == 12:
    print("You have selected Maxwell's Equations and Electromagnetic Waves.")
    print("This problem type involves the application of Maxwell's equations to analyze electromagnetic waves.")
    print("Please enter the known values and the program will calculate the unknown values.")
    # Call the function to solve the problem
    maxwells_equations_and_electromagnetic_waves()
else:
    print("Invalid input. Please enter a number between 1 and 12.")
    
# End of program

