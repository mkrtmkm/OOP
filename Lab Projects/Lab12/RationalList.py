from Rational import Rational, RationalValueError

class RationalList:
    def __init__(self, items=None):
        self.data = []
        if items:
            for item in items:
                self.append(item)

    def append(self, item):
        if isinstance(item, int):
            item = Rational(item, 1)
        elif not isinstance(item, Rational):
            raise RationalValueError("Дозволено додавати лише Rational або int")
        self.data.append(item)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        if isinstance(value, int):
            value = Rational(value, 1)
        elif not isinstance(value, Rational):
            raise RationalValueError("Дозволено призначати лише Rational або int")
        self.data[index] = value

    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        result = RationalList(self.data)
        if isinstance(other, RationalList):
            for item in other.data:
                result.append(item)
        elif isinstance(other, (Rational, int)):
            result.append(other)
        else:
            raise RationalValueError("Можна додати лише RationalList, Rational або int")
        return result

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for item in other.data:
                self.append(item)
        elif isinstance(other, (Rational, int)):
            self.append(other)
        else:
            raise RationalValueError("Можна додати лише RationalList, Rational або int")
        return self

    def sum(self):
        total = Rational(0, 1)
        for item in self.data:
            total += item
        return total

    def __str__(self):
        return "[" + ", ".join(str(r) for r in self.data) + "]"

    def __iter__(self):
        sorted_data = sorted(self.data, key=lambda r: (-r["d"], -r["n"]))
        return iter(sorted_data)
