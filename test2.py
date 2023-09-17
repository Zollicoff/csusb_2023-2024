import math

# Ask the user which 3 properties they have
prop_type1 = input("Enter the first type of properties you have (sides or angles): ")
prop_type2 = input("Enter the second type of properties you have (sides or angles): ")
prop_type3 = input("Enter the third type of properties you have (sides or angles): ")

# Based on the user's input, ask for the values of the 3 properties
if prop_type1 == "sides" and prop_type2 == "sides" and prop_type3 == "angles":
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))
    B = math.degrees(math.acos((c**2 + a**2 - b**2) / (2*c*a)))
    C = 180 - A - B
    K = 0.5 * a * b * math.sin(math.radians(C))
elif prop_type1 == "sides" and prop_type2 == "angles" and prop_type3 == "sides":
    a = float(input("Enter the length of side a: "))
    B = float(input("Enter the measure of angle B: "))
    c = float(input("Enter the length of side c: "))
    A = math.degrees(math.asin((a * math.sin(math.radians(B))) / c))
    C = math.degrees(math.asin((c * math.sin(math.radians(A))) / a))
    b = math.sqrt(a**2 + c**2 - 2*a*c*math.cos(math.radians(B)))
    K = 0.5 * a * b * math.sin(math.radians(C))
elif prop_type1 == "angles" and prop_type2 == "sides" and prop_type3 == "sides":
    A = float(input("Enter the measure of angle A: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    a = math.sqrt(b**2 + c**2 - 2*b*c*math.cos(math.radians(A)))
    B = math.degrees(math.asin((b * math.sin(math.radians(A))) / a))
    C = math.degrees(math.asin((c * math.sin(math.radians(A))) / a))
    K = 0.5 * a * b * math.sin(math.radians(C))
else:
    print("Invalid combination of properties entered. Please enter 3 properties with 2 sides and 1 angle or 2 angles and 1 side.")

# Print out all 6 properties of the triangle
print("a =", a)
print("b =", b)
print("c =", c)
print("A =", A)
print("B =", B)
print("C =", C)
