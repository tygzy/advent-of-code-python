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
    line = d.split(' ')
    taken_list = columns[line[3]][len(line[3]) - int(line[1]):int(line[1])]
    columns[line[5]].append(taken_list)
    # for i in range(int(line[1])):
    #     columns[line[3]].pop(len(columns[line[3]]) - 1 - (int(line[1]) + i))
    # print(columns[line[3]][len(line[3]) - int(line[1]):int(line[1])], line[1])

print(columns)

for k, v in columns.items():
    print(v)