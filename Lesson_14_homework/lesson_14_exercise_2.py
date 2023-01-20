class Animal:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        print(f'Название животного: {self.name}')
class Bird(Animal):
    def __init__(self, name, colour, habitat, wingspan, ration):
        super(Bird, self).__init__(name)
        self.colour = colour
        self.habitat = habitat
        self.wingspan = wingspan
        self.ration = ration

    def say_about_animal(self):
        print(f"Название животного: {self.name}, Цвет: {self.colour}, Место обитания: {self.habitat}" \
              f"Размах крыльев: {self.wingspan}, Питается: {self.ration}.")
class Mammal(Animal):
    def __init__(self, name, colour, habitat, size, ration):
        super(Mammal, self).__init__(name)
        self.colour = colour
        self.habitat = habitat
        self.size = size
        self.ration = ration
    def say_about_animal(self):
        print(f"Название животного: {self.name},  Цвет: {self.colour}, Место обитания: {self.habitat}" \
              f", Размер: {self.size}, Питается: {self.ration}.")

class Reptiles(Animal):
    def __init__(self, name, habitat, scalesize, size, ration):
        super(Reptiles, self).__init__(name)
        self.habitat = habitat
        self.scalesize = scalesize
        self.size = size
        self.ration = ration
    def say_about_animal(self):
        print(f"Название животного: {self.name}, Место обитания: {self.habitat}, "\
              f"Размер чешуи: {self.scalesize}" \
              f", Размер: {self.size}, Питается: {self.ration}")

class Fish(Animal):
    def __init__(self, name, habitat, colour, ration):
        super(Fish, self).__init__(name)
        self.habitat = habitat
        self.colour = colour
        self.ration = ration
    def say_about_animal(self):
        print(f"Название рыбы: {self.name}, Место обитания: {self.habitat}, "\
              f"Цвет: {self.colour}" \
              f", Питается: {self.ration}")
#########################
animal1 = Bird('Орел', 'Коричневый', 'Горы', '2 метра', 'Рыба и мелкие животные')
animal1.say_about_animal()
animal2 = Mammal('Кошка', 'Любой цвет', 'Домашнее животное', 'Маленький', 'Корм для кошек')
animal2.say_about_animal()
animal3 = Reptiles('Ящерица', 'Пустыня', 'Мелкий', 'До 1 метра', 'Насекомые')
animal3.say_about_animal()
fish4 = Fish('Форель', 'Реки', 'Серый', 'Водоросли')
fish4.say_about_animal()

animal1 = Bird('Курица', 'Оранжевый', 'Сарай', '35 см', 'Корм')
animal1.say_about_animal()
animal2 = Mammal('Обезьяна', 'Черный', 'Дикое', 'Среднмй', 'Баннаны')
animal2.say_about_animal()
animal3 = Reptiles('Змея', 'Леса и горы', 'Мелкий', 'от 30 см до 3м', 'Мелкие животные и насекомые')
animal3.say_about_animal()
fish4 = Fish('Белая акула', 'Океан', 'Серый', 'Мелкая рыба')
fish4.say_about_animal()