class Elves(object):

    def __init__(self):
        self.data = {}
        self.most_cal_elf = {'': 0}
        self.second_most_cal_elf = {'': 0}
        self.third_most_cal_elf = {'': 0}

    def get_data(self):
        with open('elf_data.txt', 'r') as f:
            data = f.read().split('\n\n')
            for i, d in enumerate(data):
                self.data['Elf {}'.format(i)] = d

        for k, v in self.data.items(): self.data[k] = v.split('\n')
        self.data = dict((k, [int(s) for s in v]) for k, v in self.data.items())

    def count_cals(self):
        for k, v in self.data.items():
            total_cals = 0
            for i in v:
                total_cals += i

            if total_cals > list(self.most_cal_elf.values())[0]:
                self.most_cal_elf = {k: total_cals}
        for k, v in self.data.items():
            total_cals = 0
            for i in v:
                total_cals += i
            f_me = list(self.most_cal_elf.values())[0]
            s_me = list(self.second_most_cal_elf.values())[0]
            if total_cals > s_me and total_cals != f_me:
                self.second_most_cal_elf = {k: total_cals}

        for k, v in self.data.items():
            total_cals = 0
            for i in v:
                total_cals += i

            f_me = list(self.most_cal_elf.values())[0]
            s_me = list(self.second_most_cal_elf.values())[0]
            t_me = list(self.third_most_cal_elf.values())[0]
            if total_cals > t_me and total_cals not in [f_me, s_me]:
                self.third_most_cal_elf = {k: total_cals}

    def total_top_3_elves(self):
        return list(self.most_cal_elf.values())[0] + list(self.second_most_cal_elf.values())[0] + list(self.third_most_cal_elf.values())[0]


if __name__ == '__main__' :
    e = Elves()
    e.get_data()
    e.count_cals()
    print(e.most_cal_elf)
    print(e.second_most_cal_elf)
    print(e.third_most_cal_elf)
    print('\n' + str(e.total_top_3_elves()))