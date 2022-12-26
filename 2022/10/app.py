data = open('data.in', 'r').read().splitlines()

c, x = [], 1

for line in data:
    c.append(x)
    if line.split()[0] == 'addx':
        x += int(line.split()[1])
        c.append(x)

s = (20 * c[19]) + (60 * c[59]) + (100 * c[99]) + (140 * c[139]) + (180 * c[179]) + (220 * c[219])

print(s)
