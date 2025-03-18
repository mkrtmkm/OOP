import math

class Equation:
    def __init__(self, b, c):
        self.b = b
        self.c = c

    def solve(self):
        if self.b == 0:
            if self.c == 0:
                return ("InfSolutions",)
            return ("No solution",)
        return (-self.c / self.b,)

    def show(self):
        return f"{self.b}x + {self.c} = 0"

class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        super().__init__(b, c)
        self.a = a

    def solve(self):
        if self.a == 0:
            return super().solve()
        d = self.b ** 2 - 4 * self.a * self.c
        if d < 0:
            return "No solution"
        if d == 0:
            return (-self.b / (2 * self.a),)
        return ((-self.b + math.sqrt(d)) / (2 * self.a), (-self.b - math.sqrt(d)) / (2 * self.a))

    def show(self):
        return f"{self.a}x^2 + {self.b}x + {self.c} = 0"

class BiquadraticEquation(QuadraticEquation):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def solve(self):
        quadratic_solutions = super().solve()
        solutions = set()

        for sol in quadratic_solutions:
            if isinstance(sol, (int, float)) and sol >= 0:
                sqrt_sol = math.sqrt(sol)
                solutions.add(-sqrt_sol)
                solutions.add(sqrt_sol)

        return tuple(solutions) if solutions else ("No solution",)

    def show(self):
        return f"{self.a}x^4 + {self.b}x^2 + {self.c} = 0"

a = BiquadraticEquation(1, -5, 4)
result = a.solve()
print(result)
