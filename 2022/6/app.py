data = open('data.txt', 'r').read()


def unique(s):
    uchars = set()
    for c in s:
        if c in uchars:
            return False
        uchars.add(c)
    return True


for pos, char in enumerate(data[:-3]):
    all_chars = ''
    for i in range(1, 15):
        all_chars += data[pos+i]
    not_unique = False
    if unique(all_chars):
        print(pos+15)
        break
