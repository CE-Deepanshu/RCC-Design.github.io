# User input
column_load = float(input("Enter the column load (in kN): "))
soil_bearing_capacity = float(input("Enter the safe bearing capacity of the soil (in kN/m^2): "))
column_width = float(input("Enter the width of the column (in m): "))

# Step 1: Determine the size of the footing
self_weight_factor = 0.1
total_load = column_load + (column_load * self_weight_factor)
factored_load = 1.5 * total_load
footing_area = factored_load / (2 * soil_bearing_capacity)
footing_width = math.sqrt(footing_area)

print(f"The size of the square footing is {footing_width:.2f} m x {footing_width:.2f} m.")

# Step 2: Find net upward ultimate soil pressure
net_upward_pressure = (1.5 * column_load) / (footing_width * footing_width)

# Step 3: Find depth of footing from bending moment
bending_moment = net_upward_pressure * (footing_width / 8) * ((footing_width - column_width) ** 2)
concrete_grade = 20  # M20 concrete
steel_grade = 415  # Fe 415 steel
effective_depth = math.sqrt(bending_moment / (0.138 * concrete_grade * footing_width))
total_depth = effective_depth + 0.05  # Assuming 50 mm cover

print(f"The effective depth of the footing is {effective_depth:.2f} m, and the total depth is {total_depth:.2f} m.")

# Step 4: Calculate the area of steel required
steel_area = bending_moment / (0.87 * 415 * (effective_depth - (415 * steel_area / (0.446 * concrete_grade * footing_width))))
min_steel_area = 0.0012 * footing_width * effective_depth

print(f"The required steel area is {steel_area:.2f} m^2, and the minimum steel area is {min_steel_area:.2f} m^2.")

# Step 5: Check for one-way shear (beam shear)
shear_force = net_upward_pressure * footing_width * ((footing_width - column_width) / 2 - effective_depth)
nominal_shear_stress = shear_force / (footing_width * effective_depth)
shear_strength = 0.25 * 0.5 * math.sqrt(concrete_grade)

print(f"The nominal shear stress is {nominal_shear_stress:.2f} N/mm^2, and the shear strength is {shear_strength:.2f} N/mm^2.")
if nominal_shear_stress < shear_strength:
    print("The one-way shear check is satisfied.")
else:
    print("The one-way shear check is not satisfied.")

# Step 6: Check for two-way shear (punching shear)
perimeter_critical_section = 4 * (column_width + effective_depth)
punching_shear_force = net_upward_pressure * (footing_width ** 2 - (column_width + effective_depth) ** 2)
nominal_punching_shear_stress = punching_shear_force / (perimeter_critical_section * effective_depth)
punching_shear_strength = 0.25 * (0.5 + 40 * column_width / footing_width) * math.sqrt(concrete_grade)

print(f"The nominal punching shear stress is {nominal_punching_shear_stress:.2f} N/mm^2, and the punching shear strength is {punching_shear_strength:.2f} N/mm^2.")
if nominal_punching_shear_stress < punching_shear_strength:
    print("The two-way shear (punching shear) check is satisfied.")
else:
    print("The two-way shear (punching shear) check is not satisfied.")

# Step 7: Check for development length
bond_stress = 1.2  # Assuming a design bond stress of 1.2 N/mm^2
development_length = (87 * 415 * math.sqrt(effective_depth)) / (4 * bond_stress)
available_embedment_length = (footing_width - column_width) / 2

print(f"The required development length is {development_length:.2f} m, and the available embedment length is {available_embedment_length:.2f} m.")
if available_embedment_length >= development_length:
    print("The development length check is satisfied.")
else:
    print("The development length check is not satisfied.")
