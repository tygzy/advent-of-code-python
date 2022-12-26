data = open('crate_data.txt', 'r').read().splitlines()

columns = {}
for r in range(0, 9):
    columns[str(r+1)] = []

for i in range(0, 8):
    for j in range(0, 9):
        if data[i][(4 * j) + 1] != ' ':
            columns[str(j+1)].append(data[i][(4 * j) + 1] )

for k, v in columns.items():
    v.reverse()

for d in data[10:]:
    x, y, z = (d.split()[1], d.split()[3], d.split()[5])
    a = columns[y][-int(x):]
    a.reverse() # comment out for part 2, leave in for part 1
    columns[z].extend(a)
    columns[y] = columns[y][:len(columns[y]) - int(x)]

print(columns)