my_name = 'Marcell Lévai'
my_age = 24 # not a lie
my_height = 175 # cms
my_weight = 66.5 # kgs
my_eyes = 'Dark Brown'
my_teeth = 'White'
my_hair = 'Dark Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} centimeters tall.")
print(f"He's {my_weight} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")


# Study Drills

name = 'Marcell Lévai'
age = 24 # not a lie
height = 175 # cms
weight = 66.5 # kgs
eyes = 'Dark Brown'
teeth = 'White'
hair = 'Dark Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"He's {weight} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

kgs_to_pounds = 2.20462
cms_to_inches = 0.393701
print(f"{weight} kilograms equals {weight * kgs_to_pounds} pounds.")
print(f"{height} centimeters are about {round(height * cms_to_inches)} inches.")