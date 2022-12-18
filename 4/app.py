x = open('id_data.txt', 'r').read().splitlines()

t = 0
h = 0
j = 0

for i in x:
    e1, e2 = i.split(',')

    a, b = [int(r) for r in e1.split('-')]
    c, d = [int(r) for r in e2.split('-')]

    if (a <= c and b >= d) or (c <= a and d >= b):
        t += 1

    if d >= a >= c or b >= c >= a:
        h += 1

if __name__ == '__main__':
    print(t, h)
