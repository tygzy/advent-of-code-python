lower = 265275
upper = 781584
part_1, part_2 = 0, 0


def find_double(num):
    num = list(str(num))
    group_int = None
    results = (0, 0)

    n = 0

    while n < len(num) - 1:

        if num[n] == num[n + 1]:
            results = (1, 0)
            if n <= 3:
                if num[n] == num[n + 2]:
                    results = (0, 0)
                    group_int = num[n]
                    j = False
            if num[n] != group_int:
                results = (1, 1)
                break

        j = True
        n += 1 if j else 0

    return results


def find_increase(num):
    num = list(str(num))
    for n in range(0, len(num) - 1):
        if num[n] > num[n + 1]:
            return False
    return True


for i in range(lower, upper):
    if find_increase(i):
        counts = find_double(i)
        part_1 += counts[0]
        part_2 += counts[1]

print(part_1, part_2)
