# Exercise

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

# Inserting the value of the variable afterwards with .format(varname)
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

# concatenation
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)


# Study Drills

print(joke_evaluation)

# error:
# print(joke_evaluation.format())