class Figura:
    def __init__(self, name):
        self.name = name
class Triangle(Figura):
    def __init__(self, name, side_a, side_b, side_c):
        super(Triangle, self).__init__(name)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    def _calculate(self):
        print(f"***{self.name}***")
        p = ((self.side_a) + (self.side_b) + (self.side_c) / 2)
        print(f"Периметр равен: {p}")
        area1 = ((p*(p-(self.side_a))*(p-(self.side_b))*(p-(self.side_c))) ** 0.5)
        print(f"Площадь ровна {area1}")


class Square(Figura):
    def __init__(self, name, side_a, side_b):
        super(Square, self).__init__(name)
        self.side_a = side_a
        self.side_b = side_b
    def _calculate(self):
        print(f"***{self.name}***")
        p = ((self.side_a) + (self.side_b) // 2)
        print(f"Периметр равен: {p}")
        area1 = self.side_a * self.side_b
        print(f"Площадь равна: {area1}")

class Circle(Figura):
    def __init__(self, name, radius):
        super(Circle, self).__init__(name)
        self.radius = radius
    def _calculate(self):
        print(f"***{self.name}***")
        import math
        from math import pi
        area1 = self.radius * pi ** 2
        p = area1 = self.radius * pi * 2
        print(f"Периметр круга равен: {p}")
        print(f"Площадь круга равна: {area1}")

###########################
param1 = Triangle('Треугольник', 1, 2, 3)
param2 = Square('Прямоугольник', 1, 2)
param3 = Circle('Круг', 3)

params = [param1, param2, param3]
for param in params:
    param._calculate()
