c, x, s, crt = [], 1, 0, ''

for line in open('data.in', 'r').read().splitlines():
    c.append(x)
    if line.split()[0] == 'addx':
        c.append(x)
        x += int(line.split()[1])

for i in [20, 60, 100, 140, 180, 220]:
    s += i * c[i - 1]

for cycle in range(len(c)):
    crt += '#' if c[cycle] <= (cycle % 40) + 1 <= c[cycle] + 2 else '.'
    if cycle + 1 in [40, 80, 120, 160, 200, 240]:
        crt += '\n'

print(crt, s)
