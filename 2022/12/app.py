import string, pandas, numpy as np, time

data = open('data.in', 'r').read().splitlines()
for i, line in enumerate(data):
    data[i] = [*line]
data = pandas.DataFrame(data)

alph = string.ascii_lowercase

steps = 0

i, j = np.where(data == 'S')

y = i[0]
x = j[0]

cc = 'a'

while alph.find(cc) != 25:

    cc = data[x][y]
    uc = data[x][y - 1] if y != 0 else 'a'
    dc = data[x][y + 1] if y != data.shape[1] - 1 else 'a'
    lc = data[x - 1][y] if x != 0 else 'a'
    rc = data[x + 1][y] if x != data.shape[0] - 1 else 'a'
    cc = 'a' if cc == 'S' else cc
    cc = 'z' if cc == 'E' else cc
    print(data[x][y])

    if alph.find(cc) < alph.find(rc):
        x += 1
    elif alph.find(cc) < alph.find(lc):
        x -= 1
    elif alph.find(cc) < alph.find(dc):
        y += 1
    elif alph.find(cc) < alph.find(uc):
        y -= 1

    if alph.find(cc) == alph.find(rc):
        x += 1
    elif alph.find(cc) == alph.find(lc):
        x -= 1
    elif alph.find(cc) == alph.find(dc):
        y += 1
    elif alph.find(cc) == alph.find(uc):
        y -= 1
