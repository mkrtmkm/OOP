import turtle
from random import randint, choice

class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self.position = (0, 0)
        self.vertex1 = (x1, y1) # позиція другої відносно першої вершини
        self.vertex2 = (x2, y2) # позиція третьої відносно першої вершини
        self.color = "black" # колір трикутника за промовчанням

    def set_position(self, x, y):
        self.position = (x, y)

    def set_color(self, color):
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.color(self.color)
        turtle.begin_fill()

        x0, y0 = self.position
        x1, y1 = x0 + self.vertex1[0], y0 + self.vertex1[1]
        x2, y2 = x0 + self.vertex2[0], y0 + self.vertex2[1]

        turtle.goto(x1, y1)
        turtle.goto(x2, y2)
        turtle.goto(x0, y0)

        turtle.end_fill()

def random_triangle():
    turtle.speed(0)
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]
    for _ in range (100):
        x1, y1 = randint(10, 100), randint(10, 100)
        x2, y2 = randint(-100, 100), randint(-100, 100)
        x, y = randint(-200, 200), randint(-200, 200)
        color = choice(colors)
        triangle = Triangle(x1, y1, x2, y2)
        triangle.set_position(x, y)
        triangle.set_color(color)
        triangle.draw()

turtle.hideturtle()
random_triangle()
turtle.done()