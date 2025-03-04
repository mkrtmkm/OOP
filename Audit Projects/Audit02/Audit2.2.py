import time
import turtle
from random import randint, choice
import math


class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self.position = (0, 0)
        self.vertex1 = (x1, y1)  # позиція другої відносно першої вершини
        self.vertex2 = (x2, y2)  # позиція третьої відносно першої вершини
        self.color = "black"  # колір трикутника за промовчанням
        self.rotation = 0  # кут повороту у радіанах
        self.scale = (1, 1)  # коефіцієнти розтягу по осях x та y

    def set_position(self, x, y):
        self.position = (x, y)

    def set_color(self, color):
        self.color = color

    def set_rotation(self, rotation):
        self.rotation = rotation

    def set_scale(self, scale_x, scale_y):
        self.scale = (scale_x, scale_y)

    def transform_vertex(self, vertex):
        x, y = vertex[0] * self.scale[0], vertex[1] * self.scale[1]
        x_rot = x * math.cos(self.rotation) - y * math.sin(self.rotation)
        y_rot = x * math.sin(self.rotation) + y * math.cos(self.rotation)
        return x_rot, y_rot

    def draw(self):
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.color(self.color)
        turtle.begin_fill()

        x0, y0 = self.position
        x1, y1 = self.transform_vertex(self.vertex1)
        x2, y2 = self.transform_vertex(self.vertex2)

        turtle.goto(x0 + x1, y0 + y1)
        turtle.goto(x0 + x2, y0 + y2)
        turtle.goto(x0, y0)

        turtle.end_fill()


def animate_rotation():
    turtle.speed(0)
    triangle = Triangle(50, 0, 25, 50)
    triangle.set_position(0, 0)
    triangle.set_color("blue")

    for angle in range(0, 360, 5):
        turtle.clear()
        triangle.set_rotation(math.radians(angle))
        triangle.draw()
        turtle.update()
        time.sleep(0.05)

def animate_scaling():
    turtle.speed(0)
    triangle = Triangle(50, 0, 25, 50)
    triangle.set_position(0, 0)
    triangle.set_color("red")

    for scale in range(1, 10):
        turtle.clear()
        triangle.set_scale(scale * 0.2, scale * 0.2)
        triangle.draw()
        turtle.update()


#animate_rotation()
#animate_scaling()

turtle.hideturtle()
turtle.tracer(0, 0)
turtle.done()
