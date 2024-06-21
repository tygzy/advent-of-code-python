import random, math

with open('input.in') as f:
    input = f.read().split(',')

for x in range(0, len(input)):
    input[x] = int(input[x])


def return_output(input_arr):
    arr = input_arr[:]
    for x in range(0, len(arr), 4):
        num_a = arr[arr[x + 1]]
        num_b = arr[arr[x + 2]]
        if arr[x] == 99:
            break
        elif arr[x] == 1:
            try:
                arr[arr[x + 3]] = num_a + num_b
            except IndexError:
                continue
        elif arr[x] == 2:
            try:
                arr[arr[x + 3]] = num_a * num_b
            except IndexError:
                continue
    return arr[0]


for j in range(0, 99):
    input[1] = j
    for i in range(0, 99):
        input[2] = i

        value = return_output(input)
        if value == 19690720:
            print(100 * j + i)
            break

print(input)