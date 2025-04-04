from collections import defaultdict


class Polynome(defaultdict):
    def __init__(self, **kwargs):
        super().__init__(float, **kwargs)

    def fromstring(s):
        p = Polynome()
        s = s.replace('+', ' ')
        ls = s.split()
        for m in ls:
            c = m.split('*x**')
            k = int(c[1])
            v = float(c[0])
            p[k] = v
        return p

    fromstring = staticmethod(fromstring)

    def add_monom(self, deg, coeff):
        if coeff != 0:
            self[deg] += coeff

    def get_degree(self):
        return max(self, default=0)

    def __str__(self):
        monomials = list(self.items())
        if not monomials:
            return "0.0*x**0"
        monomials.sort(reverse=True)
        return ' + '.join(f"{v}*x**{k}" for k, v in monomials)

    def __call__(self, x):
        return sum(v * x ** k for k, v in self.items())

    def __add__(self, other):
        p = Polynome()
        keys = set(self.keys()) | set(other.keys())
        for k in keys:
            p[k] = self[k] + other[k]
        return self._delzeroes(p)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        p = Polynome()
        keys = set(self.keys()) | set(other.keys())
        for k in keys:
            p[k] = self[k] - other[k]
        return self._delzeroes(p)

    def __rsub__(self, other):
        p = Polynome()
        keys = set(self.keys()) | set(other.keys())
        for k in keys:
            p[k] = other[k] - self[k]
        return self._delzeroes(p)

    def __mul__(self, other):
        p = Polynome()
        for k1 in self:
            for k2 in other:
                p[k1 + k2] += self[k1] * other[k2]
        return self._delzeroes(p)

    def __rmul__(self, other):
        return self.__mul__(other)

    def deriv(self, n=1):
        p = self
        for _ in range(n):
            p = self._deriv(p)
        return self._delzeroes(p)

    def _deriv(self, p):
        pp = Polynome()
        for k in p:
            if k != 0:
                pp[k - 1] = p[k] * k
        return pp

    def _delzeroes(self, p):
        pp = Polynome()
        for k in p:
            if p[k] != 0:
                pp[k] = p[k]
        return pp

    def __iter__(self):
        return iter(sorted(self.keys(), reverse=True))


if __name__ == '__main__':
    p1 = Polynome.fromstring('3.7*x**3 + 0.3*x**1 + -1.2*x**0')
    print('p1 =', p1)
    p2 = Polynome.fromstring('2.2*x**3 + -1.3*x**2 + 0.2*x**1')
    print('p2 =', p2)
    # print('Значення p1 у точці x=2:', p1(2))
    # print('Сума p1+p2:', p1 + p2)
    # print('Різниця p1-p2:', p1 - p2)
    # print('Добуток p1*p2:', p1 * p2)
    # print('2 похідна p1:', p1.deriv(2))

    print("Мономи p1 у порядку спадання степенів:")
    for term in p1:
        print(term)