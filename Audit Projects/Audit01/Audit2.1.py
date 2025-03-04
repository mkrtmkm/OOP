import math

class QuadraticEquation:
    def __init__(self, a,b = None, c = None):
        if isinstance(a, QuadraticEquation):
            self._a = a.a
            self._b = b.b
            self._c = c.c
        else:
            self._a = a
            self._b = b
            self._c = c

    def _discriminant(self):
        return self._b ** 2 - 4 * self._a * self._c

    