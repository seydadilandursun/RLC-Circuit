import math

# Define the values of R, L, C, and frequency (f)
R1 =float(input("Enter R(ohm): ")) # Resistance in ohms
L1 = float(input("Enter L(henrys): ")) # Inductance in henrys
C1 = float(input("Enter C(farads): ")) # Capacitance in farads
f1 = float(input("Enter f(Hertz): ")) # Frequency in Hertz

def calculate_impedance(R, L, C, f):
        # Calculate inductive reactance (X_L)
        X_L = 2 * math.pi * f * L
        
        # Calculate capacitive reactance (X_C), handle potential division by zero
        X_C = 1 / (2 * math.pi * f * C)
        
        # Calculate impedance (Z)
        Z = math.sqrt(R**2 + (X_L - X_C)**2)
        return Z

Z_total=calculate_impedance(R1,L1,C1,f1) 

print(f"Impedance (Z) = {Z_total} ohms")
