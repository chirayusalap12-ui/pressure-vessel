YIELD_STRENGTH = 250.0
P = float(input("Enter Internal Pressure (MPa): "))
R=float(input("Enter Internal Radius (mm): "))
T=float(input("Enter Wall Thickness (mm): "))
hoop_stress = (P * R) / T
longitudinal_stress = (P * R) / (2 * T)
print("Hoop Stress: {:.2f} MPa".format(hoop_stress))
print("Longitudinal Stress: {:.2f} MPa".format(longitudinal_stress))
if hoop_stress > YIELD_STRENGTH:
    print("Hoop Stress exceeds yield strength!")
else:
    print("Hoop Stress is within yield strength.")
if longitudinal_stress > YIELD_STRENGTH:
    print("Longitudinal Stress exceeds yield strength!")
else:
    print("Longitudinal Stress is within yield strength.")
