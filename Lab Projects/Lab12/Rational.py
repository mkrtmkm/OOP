from math import gcd

class RationalError(ZeroDivisionError):
    def __init__(self, message="Знаменник не може дорівнювати нулю"):
        super().__init__(message)

class RationalValueError(ValueError):
    def __init__(self, message="Некоректний тип для операції з Rational"):
        super().__init__(message)

class Rational:
    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, str):
            parts = numerator.strip().split('/')
            if len(parts) != 2:
                raise ValueError("Некоректний формат рядка. Очікується 'n/d'")
            numerator, denominator = int(parts[0]), int(parts[1])

        if denominator == 0:
            raise RationalError()

        common = gcd(numerator, denominator)
        self.n = numerator // common
        self.d = denominator // common
        if self.d < 0:
            self.n *= -1
            self.d *= -1

    def __copy__(self):
        return Rational(self.n, self.d)

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if isinstance(other, Rational):
            return Rational(self.n * other.d + other.n * self.d, self.d * other.d)
        raise RationalValueError()

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if isinstance(other, Rational):
            return Rational(self.n * other.d - other.n * self.d, self.d * other.d)
        raise RationalValueError()

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if isinstance(other, Rational):
            return Rational(self.n * other.n, self.d * other.d)
        raise RationalValueError()

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if isinstance(other, Rational):
            if other.n == 0:
                raise RationalError("Не можна ділити на нуль")
            return Rational(self.n * other.d, self.d * other.n)
        raise RationalValueError()

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == "n":
            return self.n
        elif key == "d":
            return self.d
        else:
            raise KeyError("Невірний ключ. Використовуйте 'n' або 'd'")

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise ValueError("Значення має бути цілим")
        if key == "n":
            self.n = value
        elif key == "d":
            if value == 0:
                raise RationalError()
            self.d = value
        else:
            raise KeyError("Невірний ключ. Використовуйте 'n' або 'd'")
        common = gcd(self.n, self.d)
        self.n //= common
        self.d //= common
        if self.d < 0:
            self.n *= -1
            self.d *= -1

    def __str__(self):
        return f"{self.n}/{self.d}"
