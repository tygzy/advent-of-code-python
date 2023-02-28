import operator

data = open('data.in', 'r').read().splitlines()
ops = {'+': operator.add, '*': operator.mul}

monkeys = {}
inspected = {}
outcomes = {}
cm = 0

for line in data:
    line = line.split()
    if line:
        if line[0] == 'Monkey':
            monkeys[int(line[1][:-1])] = []
            cm = int(line[1][:-1])
            inspected[int(line[1][:-1])] = 1
            print(int(line[1][:-1]))

for line in data:
    line = line.split()
    if line:
        if line[0] == 'Starting':
            for l in line[2:]:
                monkeys[cm].append(int(l.replace(',','')))
        elif line[0] == 'Operation:':
            for i in monkeys[cm]:
                if line[-1] != 'old':
                    monkeys[cm][monkeys[cm].index(i)] = ops[line[-2]](i, int(line[-1]))
                else:
                    monkeys[cm][monkeys[cm].index(i)] = ops[line[-2]](i, i)
        elif line[0] == 'Test:':
            for i in monkeys[cm]:
                v = int(line[-1])
                if not i % v:
                    dt = True
                    outcomes[i] = False
                else:
                    dt = True
                    outcomes[i] = True
        elif line[1] == 'true:':
            for k, v in monkeys.items():
                inspected[k] += 1
            for i in monkeys[cm]:
                for k, v in outcomes.items():
                    if v:
                        if i == k:
                            item = monkeys[cm][monkeys[cm].index(i)]
                            monkeys[cm].pop(monkeys[cm].index(i))
                            monkeys[int(line[-1])].append(item)
        elif line[1] == 'false:':
            for k, v in monkeys.items():
                inspected[k] += 1
            for i in monkeys[cm]:
                for k, v in outcomes.items():
                    if not v:
                        if i == k:
                            item = monkeys[cm][monkeys[cm].index(i)]
                            monkeys[cm].pop(monkeys[cm].index(i))
                            monkeys[int(line[-1])].append(item)

print(inspected)

print(monkeys)