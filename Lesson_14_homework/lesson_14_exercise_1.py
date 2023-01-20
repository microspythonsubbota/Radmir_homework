class Computer:
    def __init__(self, owner, processor, ozu, hdd, monitor):
        self.owner = owner
        self.processor = processor
        self.ozu = ozu
        self.hdd = hdd
        self.monitor = monitor
        self.say_computer_name()

    def __str__(self):
        print(f'Класс Computer с полями: owner: ' \
               f'{self.owner}, processor: {self.processor}, ozu: {self.ozu}, ' \
               f'hdd: {self.hdd}, monitor: {self.monitor}')

    def say_computer_name(self):
        print(f'Владелец компьютера {self.owner}')
    def __eq__(self, other):
        return self.ozu == other.ozu
    def __lt__(self, other):
        return self.ozu < other.ozu
    def __le__(self, other):
        return self.ozu <= other.ozu
    def __gt__(self, other):
        return self.ozu > other.ozu
    def __ge__(self, other):
        return self.ozu >= other.ozu

pc1 = Computer('Bob', 'i7', 2, '100gb', '24inch')
pc2 = Computer('Caty', 'i9', 4, '100gb', '24inch')
print(pc1.say_computer_name())
print(pc2.say_computer_name())
print(pc1 < pc2)
print(pc1 > pc2)
print(pc1 == pc2)
print(pc1 <= pc2)