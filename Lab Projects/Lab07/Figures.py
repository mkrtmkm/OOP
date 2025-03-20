import math

class Error1(Exception):
    pass

class Figure:
    def dimention(self):   #вимірність
        raise NotImplementedError

    def perimetr(self):  #периметр
        raise NotImplementedError

    def square(self):  #площа
        raise NotImplementedError

    def squareSurface(self):  #площа бічної поверхні
        raise NotImplementedError

    def squareBase(self): #площа основи
        raise NotImplementedError

    def height(self):  #висота
        raise NotImplementedError

    def volume(self):  #міра фігури (площа чи об'єм)
        raise NotImplementedError


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        if not self._is_valid(side1, side2, side3):
            raise Error1(f"Трикутник з такими сторонами не існує")
        self.side1, self.side2, self.side3 = side1, side2, side3

    @staticmethod
    def _is_valid(side1, side2, side3):
        return side1 > 0 and side2 > 0 and side3 > 0 and side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2

    def dimention(self):
        return 2

    def perimetr(self):
        return self.side1 + self.side2 + self.side3

    def square(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        return self.square()


class Rectangle(Figure):
    def __init__(self, side1, side2):
        if not self._is_valid(side1, side2):
            raise Error1(f"Сторони прямокутника мають бути додатними")
        self.side1, self.side2 = side1, side2

    @staticmethod
    def _is_valid(side1, side2):
        return side1 > 0 and side2 > 0

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * (self.side1 + self.side2)

    def square(self):
        return self.side1 * self.side2

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        return self.square()


class Trapeze(Figure):
    def __init__(self, base1, base2, side1, side2):
        if not self._is_valid(base1, base2, side1, side2):
            raise Error1(f"Дана трапеція не існує")
        self.base1, self.base2, self.side1, self.side2 = base1, base2, side1, side2

    @staticmethod
    def _is_valid(base1, base2, side1, side2):
        if not (base1 > 0 and base2 > 0 and side1 > 0 and side2 > 0):
            return False
        if abs(base1 - base2) >= side1 + side2:
            return False
        diff = (base1 - base2) ** 2 + side1 ** 2 - side2 ** 2
        denominator = 2 * (base1 - base2)
        if denominator == 0:
            return False
        k = diff / denominator
        discriminant = side1 ** 2 - k ** 2
        return discriminant > 0

    def dimention(self):
        return 2

    def perimetr(self):
        return self.base1 + self.base2 + self.side1 + self.side2

    def square(self):
        height = math.sqrt(self.side1 ** 2 - (((self.base1 - self.base2) ** 2 + self.side1 ** 2 - self.side2 ** 2) / (
                2 * (self.base1 - self.base2))) ** 2)
        return (self.base1 + self.base2) / 2 * height

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        return self.square()


class Parallelogram(Figure):
    def __init__(self, side1, side2, height):
        if not self._is_valid(side1, side2, height):
            raise Error1(f"Даний паралелограм не існує")
        self.side1, self.side2, self.h = side1, side2, height

    @staticmethod
    def _is_valid(side1, side2, height):
        return side1 > 0 and side2 > 0 and height > 0 and height <= side2

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * (self.side1 + self.side2)

    def square(self):
        return self.side1 * self.h

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        return self.square()


class Circle(Figure):
    def __init__(self, radius):
        if not self._is_valid(radius):
            raise Error1(f"Дане коло не існує")
        self.radius = radius

    @staticmethod
    def _is_valid(radius):
        return radius > 0

    def dimention(self):
        return 2

    def perimetr(self):
        return 2 * math.pi * self.radius

    def square(self):
        return math.pi * self.radius ** 2

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        return self.square()


class Ball(Circle):
    def __init__(self, radius):
        super().__init__(radius)

    def dimention(self):
        return 3

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return 4 * super().square()

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3


class TriangularPyramid(Triangle):
    def __init__(self, baseSide, height):
        super().__init__(baseSide, baseSide, baseSide)
        if height <= 0:
            raise Error1("Висота трикутної піраміди має бути додатною")
        self.h = height

    def dimention(self):
        return 3

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return 3 * (self.side1 * math.sqrt(self.h ** 2 + self.side1**2 / 12)) / 2

    def squareBase(self):
        return (math.sqrt(3) / 4) * self.side1 ** 2

    def height(self):
        return self.h

    def volume(self):
        return (1 / 3) * self.squareBase() * self.h


class QuadrangularPyramid(Rectangle):
    def __init__(self, baseSide1, baseSide2, height):
        super().__init__(baseSide1, baseSide2)
        if height <= 0:
            raise Error1("Висота чотирикутної піраміди має бути додатною")
        self.h = height

    def dimention(self):
        return 3

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        l1 = math.sqrt((self.side1 / 2) ** 2 + self.h ** 2)
        l2 = math.sqrt((self.side2 / 2) ** 2 + self.h ** 2)
        return 2 * (self.side1 * l1 + self.side2 * l2)

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        return (1 / 3) * self.squareBase() * self.h


class RectangularParallelepiped(Rectangle):
    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2)
        if side3 <= 0:
            raise Error1("Сторона паралелепіпеда має бути додатною")
        self.side3 = side3

    def dimention(self):
        return 3

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return 2 * (self.side1 * self.side3 + self.side2 * self.side3)

    def squareBase(self):
        return super().square()

    def height(self):
        return self.side3

    def volume(self):
        return self.squareBase() * self.side3


class Cone(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        if height <= 0:
            raise Error1("Висота конуса має бути додатною")
        self.h = height

    def dimention(self):
        return 3

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        l = math.sqrt(self.radius ** 2 + self.h ** 2)
        return super().perimetr() * l

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        return (1 / 3) * self.squareBase() * self.h


class TriangularPrism(Triangle):
    def __init__(self, side1, side2, side3, height):
        super().__init__(side1, side2, side3)
        if height <= 0:
            raise Error1("Висота призми має бути додатною")
        self.h = height

    def dimention(self):
        return 3

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return super().perimetr() * self.h

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        return self.squareBase() * self.h


def process_figures_from_files(filenames):
    figure_classes = {
        'Triangle': Triangle,
        'Rectangle': Rectangle,
        'Trapeze': Trapeze,
        'Parallelogram': Parallelogram,
        'Circle': Circle,
        'Ball': Ball,
        'TriangularPyramid': TriangularPyramid,
        'QuadrangularPyramid': QuadrangularPyramid,
        'RectangularParallelepiped': RectangularParallelepiped,
        'Cone': Cone,
        'TriangularPrism': TriangularPrism
    }

    figures = []
    invalid_figures = []

    for filename in filenames:
        try:
            with open(filename, 'r') as f:
                for line in f:
                    if line.strip():
                        parts = line.split()
                        figure_type = parts[0]
                        try:
                            params = [float(x) for x in parts[1:]]
                            if figure_type in figure_classes:
                                figure = figure_classes[figure_type](*params)
                                figures.append((figure, line.strip()))
                            else:
                                invalid_figures.append(f"Невідомий тип фігури: {line.strip()}")
                        except Error1 as e:
                            invalid_figures.append(f"Некоректна фігура: {line.strip()} - {str(e)}")
                        #except Exception as e:
                           #invalid_figures.append(f"Error processing: {line.strip()} - {str(e)}")
        except FileNotFoundError:
            invalid_figures.append(f"Файл {filename} не знайдено")

    if not figures:
        return None, invalid_figures

    max_figure, max_line = max(figures, key=lambda x: x[0].volume())
    return (max_figure, max_line, max_figure.volume()), invalid_figures


def write_uml_to_file(filename):
    uml = [
        "[Figure] (abstract)",
        "  |",
        "  +-- [Triangle]",
        "  |     |",
        "  |     +-- [TriangularPyramid]",
        "  |     +-- [TriangularPrism]",
        "  |",
        "  +-- [Rectangle]",
        "  |     |",
        "  |     +-- [QuadrangularPyramid]",
        "  |     +-- [RectangularParallelepiped]",
        "  |",
        "  +-- [Trapeze]",
        "  |",
        "  +-- [Parallelogram]",
        "  |",
        "  +-- [Circle]",
        "  |     |",
        "  |     +-- [Ball]",
        "  |     +-- [Cone]",

    ]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write('\n'.join(uml))


def main():
    input_files = ["input01.txt", "input02.txt", "input03.txt"]
    result, invalid = process_figures_from_files(input_files)

    with open("output.txt", 'w', encoding="utf-8") as f:
        if result:
            max_figure, max_line, max_measure = result
            f.write("Фігура з максимальною мірою:\n")
            f.write(f"Опис: {max_line}\n")
            if max_figure.dimention() == 2:
                f.write(f"Міра(площа): {max_measure:.2f}\n")
            else:
                f.write(f"Міра(об'єм): {max_measure:.2f}\n")
        else:
            f.write("Не вдалося знайти валідну фігуру\n")

        if invalid:
            f.write("\nПомилки:\n")
            f.writelines('\n'.join(invalid) + '\n')

    write_uml_to_file("uml.txt")
    print("Результати збережено в output.txt, UML-діаграма в uml.txt")


if __name__ == "__main__":
    main()
