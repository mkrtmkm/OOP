import math

class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = sorted([a, b, c])
        if self.a + self.b <= self.c:
            raise ValueError(f"Сторони ({a}, {b}, {c}) не утворюють трикутник")

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        discriminant = s * (s - self.a) * (s - self.b) * (s - self.c)
        return math.sqrt(discriminant) if discriminant > 0 else 0

    def __str__(self):
        return (f"Трикутник: a={self.a}, b={self.b}, c={self.c}. "
                f"Площа={self.area():.2f}, Периметр={self.perimeter():.2f}")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __str__(self):
        return (f"Прямокутник: width={self.width}, height={self.height}. "
                f"Площа={self.area():.2f}, Периметр={self.perimeter():.2f}")

class Trapeze:
    def __init__(self, base1, base2, side1, side2):
        self.base1, self.base2 = sorted([base1, base2])
        self.side1, self.side2 = side1, side2

    def perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2

    def area(self):
        s = (self.side1 + self.side2 + abs(self.base2 - self.base1)) / 2
        discriminant = s * (s - self.side1) * (s - self.side2) * (s - abs(self.base2 - self.base1))

        if discriminant <= 0:
            return 0
        height = (2 * math.sqrt(discriminant)) / abs(self.base2 - self.base1)
        return (self.base1 + self.base2) * height / 2

    def __str__(self):
        return (f"Трапеція: base1={self.base1}, base2={self.base2}, "
                f"side1={self.side1}, side2={self.side2}. "
                f"Площа={self.area():.2f}, Периметр={self.perimeter():.2f}")

class Parallelogram:
    def __init__(self, base, side, height):
        self.base = base
        self.side = side
        self.height = height

    def perimeter(self):
        return 2 * (self.base + self.side)

    def area(self):
        return self.base * self.height

    def __str__(self):
        return (f"Паралелограм: base={self.base}, side={self.side}, "
                f"height={self.height}. "
                f"Площа={self.area():.2f}, Периметр={self.perimeter():.2f}")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return (f"Коло: radius={self.radius}. "
                f"Площа={self.area():.2f}, Довжина кола={self.perimeter():.2f}")