import string


class Backpacks(object):

    def __init__(self):
        self.lower_chars = string.ascii_lowercase
        self.upper_chars = string.ascii_uppercase
        self.points = 0

    def get_items(self):
        with open('backpack_data.txt', 'r') as f:
            backpacks = f.read().split('\n')
            for backpack in backpacks:
                first_compartment, second_compartment = backpack[:len(backpack) // 2], backpack[len(backpack) // 2:]
                for char in self.lower_chars:
                    if char in first_compartment and char in second_compartment:
                        self.points += self.lower_chars.find(char) + 1
                for char in self.upper_chars:
                    if char in first_compartment and char in second_compartment:
                        self.points += self.upper_chars.find(char) + 27

    def get_items_part_2(self):
        with open('backpack_data.txt', 'r') as f:
            backpacks = f.read().split('\n')
            for backpack_1, backpack_2, backpack_3 in zip(*[iter(backpacks)]*3):
                for char in self.lower_chars:
                    if char in backpack_1 and char in backpack_2 and char in backpack_3:
                        self.points += self.lower_chars.find(char) + 1
                for char in self.upper_chars:
                    if char in backpack_1 and char in backpack_2 and char in backpack_3:
                        self.points += self.upper_chars.find(char) + 27


if __name__ == '__main__':
    b = Backpacks()
    b.get_items_part_2()
    print(b.points)
