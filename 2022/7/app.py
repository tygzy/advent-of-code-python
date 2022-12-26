data = open('data.txt', 'r').read().splitlines()

path = []
k_paths = {'/': 0}
ts = 0

for d in data:
    words = d.split()
    if words[1] == 'cd':
        if words[2] == '..':
            path.pop()
        else:
            path.append(words[2])
    elif words[0] == 'dir':
        if words[1] not in k_paths:
            k_paths['_'.join(path) + '_' + words[1]] = 0
    else:
        for i, p in enumerate(path):
            k_paths['_'.join(path[0:i + 1])] += int(words[0])

sl = max(k_paths, key=k_paths.get)

for k, v in k_paths.items():
    if int(v) < 100000:
        ts += int(v)
    if k_paths['/'] - 40000000 < int(v) < k_paths[sl]:
        sl = k

print(ts) # part 1
print(k_paths[sl]) # part 2