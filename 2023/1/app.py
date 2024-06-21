data = open('input.in', 'r').read().splitlines()

total = 0

words = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

for line in data:
    first_int = None
    last_int = None

    last_sequence = []

    chars = line.split()[0]

    for char in chars:
        if char.isdigit():
            last_sequence = []
            first_int = int(char) if not first_int else first_int
            last_int = int(char)
        else:
            last_sequence.append(char)

    total += int(f'{first_int}{last_int}')

print(total)