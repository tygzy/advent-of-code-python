data = open('data.in', 'r').read().splitlines()

c, x, s = [], 1, 0
crt = ""

for line in data:
    c.append(x)
    if line.split()[0] == 'addx':
        c.append(x)
        x += int(line.split()[1])

for i in [20, 60, 100, 140, 180, 220]:
    s += i*c[i-1]

for cycle in range(len(c)):
    cur_x = c[cycle]
    if cur_x <= (cycle%40)+1 <= cur_x+2:
        crt += '#'
    else:
        crt += '.'
    if cycle+1 in [40, 80, 120, 160, 200, 240]:
        crt += '\n'

print(crt)
print(s)
