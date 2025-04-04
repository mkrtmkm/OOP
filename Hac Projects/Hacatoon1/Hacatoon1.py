from turtle import *

scale_x = 40
scale_y = 60

hor_up = 1
hor_down = 2
descent = 3
ascend = 4
vert = 6

elements = {
    0: (),
    1: (hor_up,),
    2: (hor_down,),
    3: (descent,),
    4: (ascend,),
    5: (hor_up, ascend),
    6: (vert,),
    7: (hor_up, vert),
    8: (hor_down, vert),
    9: (hor_up, hor_down, vert)
}

def draw_element(element):
    down()
    goto(0, scale_y)


    if element == hor_up:
        goto(0, scale_y)
        goto(scale_x, scale_y)
        up()


    elif element == hor_down:
        goto(0, 2*scale_y/3)
        goto(scale_x, 2*scale_y/3)
        up()


    elif element == descent:
        goto(0, scale_y)
        goto(scale_x, 2*scale_y/3)
        up()


    elif element == ascend:
        goto(0, 2*scale_y/3)
        goto(scale_x, scale_y)
        up()

    elif element == vert:
        up()
        goto(scale_x, scale_y)
        down()
        goto(scale_x, 2*scale_y/3)
        up()

    penup()
    goto(0, 0)



def draw_digit(digit):
    if digit not in elements:
        return
    penup()
    goto(0, 0)
    pendown()
    for elem in elements[digit]:
        draw_element(elem)


draw_digit(6)



mainloop()