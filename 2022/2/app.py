x = open('game_data.txt', 'r').read().splitlines()

p = 0
j = 0

tools = [('X', 1), ('Y', 2), ('Z', 3)]

for i in x:
    p += 6 if i in ['A Y', 'B Z', 'C X'] else 0
    p += 3 if i in ['A X', 'B Y', 'C Z'] else 0
    p += 1 if i[2] == 'X' else 0
    p += 2 if i[2] == 'Y' else 0
    p += 3 if i[2] == 'Z' else 0

    if i[2] == 'Z':
        j += 6
        j += 2 if i[0] == 'A' else 0
        j += 3 if i[0] == 'B' else 0
        j += 1 if i[0] == 'C' else 0

    if i[2] == 'Y':
        j += 3
        j += 1 if i[0] == 'A' else 0
        j += 2 if i[0] == 'B' else 0
        j += 3 if i[0] == 'C' else 0

    if i[2] == 'X':
        j += 3 if i[0] == 'A' else 0
        j += 1 if i[0] == 'B' else 0
        j += 2 if i[0] == 'C' else 0