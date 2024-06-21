import math

fuel = []
total, recurring_total = 0, 0

with open('input.in') as f:
    input = f.readlines()

for x, i in enumerate(input):
    og = int(i)
    mass = math.floor(og / 3) - 2
    fuel.append(mass)
    total += mass
    new_mass = mass
    while new_mass > 0:
        operation = math.floor(new_mass / 3) - 2
        if operation < 0:
            break
        new_mass = operation
        fuel.append(new_mass)
        recurring_total += new_mass

print(fuel)
print(total, total + recurring_total)