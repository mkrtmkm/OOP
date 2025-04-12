from math import gcd

class RationalError(Exception):
    INVALID_FORMAT = 0
    DENOMINATOR_ERROR = 1
    INVALID_KEY = 2
    INVALID_VALUE = 3

    def __init__(self, err_code, message):
        super(RationalError, self).__init__()
        self.err_code = err_code
        self.message = message

    def __str__(self):
        return f'{self.err_code}: {self.message}'

class Rational:
    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, str):
            parts = numerator.strip().split('/')
            if len(parts) != 2:
                raise RationalError(RationalError.INVALID_FORMAT, "Invalid format")
            numerator, denominator = int(parts[0]), int(parts[1])

        if denominator == 0:
            raise RationalError(RationalError.DENOMINATOR_ERROR, "Invalid denominator")

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
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if isinstance(other, Rational):
            return Rational(self.n * other.d - other.n * self.d, self.d * other.d)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if isinstance(other, Rational):
            return Rational(self.n * other.n, self.d * other.d)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if isinstance(other, Rational):
            if other.n == 0:
                raise RationalError(RationalError.DENOMINATOR_ERROR, "Invalid denominator")
            return Rational(self.n * other.d, self.d * other.n)
        return NotImplemented

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, key):
        if key == "n":
            return self.n
        elif key == "d":
            return self.d
        else:
            raise RationalError(RationalError.INVALID_KEY, "Invalid key")

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise RationalError(RationalError.INVALID_VALUE, "Invalid value")
        if key == "n":
            self.n = value
        elif key == "d":
            if value == 0:
                raise RationalError(RationalError.DENOMINATOR_ERROR, "Invalid denominator")
            self.d = value
        else:
            raise RationalError(RationalError.INVALID_KEY, "Invalid key")
        common = gcd(self.n, self.d)
        self.n //= common
        self.d //= common
        if self.d < 0:
            self.n *= -1
            self.d *= -1

    def __str__(self):
        return f"{self.n}/{self.d}"
