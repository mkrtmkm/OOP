import numpy as np

class Matrix2D:
    def __init__(self, a11, a12, a21, a22):
        self.matrix = np.array([[a11, a12], [a21, a22]])

    @staticmethod
    def from_input():
        values = list(map(float, input("Введіть 4 числа для матриці: ").split()))
        return Matrix2D(*values)

    @staticmethod
    def from_file(filename):
        with open(filename, "r", encoding="utf-8") as file:
            values = list(map(float, file.readline().split()))
            return Matrix2D(*values)

    def to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(str(self))

    def determinant(self):
        return np.linalg.det(self.matrix)

    def is_singular(self):
        return self.determinant() == 0

    def __str__(self):
        return f"[{self.matrix[0][0]} {self.matrix[0][1]}]\n[{self.matrix[1][0]} {self.matrix[1][1]}]"