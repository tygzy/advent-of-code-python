with open('input.in') as f:
    instructions = f.readlines()

instruction_set_a = instructions[0].split(',')
instruction_set_b = instructions[1].split(',')

directions = {'L': -1, 'R': 1, 'U': -1, 'D': 1}
axis = ['U', 'D']

x, y, a, b = 0, 0, 0, 0
steps_a, steps_b, steps_a_intersects, steps_b_intersects = [], [], [], []
positions_a, positions_b, intersects = [], [], []

for instruction in instruction_set_a:
    if instruction[0] in axis:
        y += directions[instruction[0]] * int(instruction[1:])
        steps_a.append([0, abs(directions[instruction[0]] * int(instruction[1:]))])
    else:
        x += directions[instruction[0]] * int(instruction[1:])
        steps_a.append([abs(directions[instruction[0]] * int(instruction[1:])), 0])
    positions_a.append([x, y])

for instruction in instruction_set_b:
    if instruction[0] in axis:
        b += directions[instruction[0]] * int(instruction[1:])
        steps_b.append([0, abs(directions[instruction[0]] * int(instruction[1:]))])
    else:
        a += directions[instruction[0]] * int(instruction[1:])
        steps_b.append([abs(directions[instruction[0]] * int(instruction[1:])), 0])
    positions_b.append([a, b])

for h in range(0, len(positions_b) - 1):
    for j in range(0, len(positions_a) - 1):
        if positions_a[j+1][0] <= positions_b[h][0] <= positions_b[h+1][0]:
            if positions_b[h][1] <= positions_a[j+1][1] <= positions_a[j][1]:
                intersects.append([positions_b[h][0], positions_a[j+1][1]])
                steps_a_intersects.append([int(sum(list(list(zip(*steps_a[:j]))[0])) - abs(abs(positions_b[h][0]) - abs(positions_b[h+1][0]))), int(sum(list(list(zip(*steps_a[:j]))[1])) - abs(abs(positions_a[j][1]) - abs(positions_b[j+1][1])))])
                steps_b_intersects.append([int(sum(list(list(zip(*steps_b[:h]))[0])) - abs(abs(positions_a[h][0]) - abs(positions_a[h+1][0]))), int(sum(list(list(zip(*steps_b[:h]))[1])) - abs(abs(positions_b[j][1]) - abs(positions_a[j+1][1])))])


manhattan_distance = abs(min(intersects)[0]) + abs(min(intersects)[1])


print('Part 1:', manhattan_distance)
print('Part 2:', min([sum(min(steps_a_intersects)), sum(min(steps_b_intersects))]))

