import math

# Define the values of R, L, C, and frequency (f)
r_1 = float(input("Enter R(ohm): ")) # Resistance in ohms
l_1 = float(input("Enter L(henrys): ")) # Inductance in henrys
c_1 = float(input("Enter C(farads): ")) # Capacitance in farads
f_1 = float(input("Enter f(Hertz): ")) # Frequency in Hertz

def calculate_impedance(r, l, c, f):
        # Calculate inductive reactance (X_L)
        X_l = 2 * math.pi * f * l
        
        # Calculate capacitive reactance (X_C), handle potential division by zero
        X_c = 1 / (2 * math.pi * f * C)
        
        # Calculate impedance (Z)
        Z = math.sqrt(r**2 + (X_l - X_c)**2)
        return Z

Z_total = calculate_impedance(r_1,l_1,c_1,f_1) 

print(f"Impedance (Z) = {Z_total} ohms")
