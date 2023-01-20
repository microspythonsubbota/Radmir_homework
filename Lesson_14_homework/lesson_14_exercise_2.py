class Animal:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'Название животного: {self.name}'
animal1 = Animal("Lion")
