name = 'Zed A. Shaw'
age = 35 # Not a lie
height_in = 74 # Inches
height_cm = round(height_in * 2.54)
weight_lb = 180 # lbs
weight_kg = round(weight_lb / 2.2)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Lets talk about {name}.")
print(f"He's {height_cm} cm tall.")
print(f"He's {weight_kg} kg heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height_in + weight_lb
print(f"If I add {age}, {height_in} and {weight_lb}, I get {total}.")
