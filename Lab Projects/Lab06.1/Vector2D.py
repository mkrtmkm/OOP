class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def from_input():
        values = list(map(float, input("Введіть 2 числа для вектора: ").split()))
        return Vector2D(*values)

    @staticmethod
    def from_file(filename):
        with open(filename, "r", encoding="utf-8") as file:
            values = list(map(float, file.readline().split()))
            return Vector2D(*values)

    def to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(self))

    def __str__(self):
        return f"({self.x}, {self.y})"