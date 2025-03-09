from Matrix2D import Matrix2D
from Vector2D import Vector2D

class Solver:
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.vector = vector

    def solve(self):
        det_A = self.matrix.determinant()
        if det_A == 0:
            return None  # Система рівнянь не має розв'язку

        # Створюємо матриці з підставленими стовпцями
        A_x = Matrix2D(self.vector.x, self.matrix.matrix[0][1],
                       self.vector.y, self.matrix.matrix[1][1])
        A_y = Matrix2D(self.matrix.matrix[0][0], self.vector.x,
                       self.matrix.matrix[1][0], self.vector.y)

        x = A_x.determinant() / det_A
        y = A_y.determinant() / det_A

        return Vector2D(x, y)