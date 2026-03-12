# import turtle
# turtle.speed(0)
# def flower():
#     for i in range(30):
#         turtle.foward(100)
#         turtle.right(90)


# flower()

import turtle
turtle.speed(0)
def draw_square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
        turtle.forward(size)

size = 5

for s in range(20):
    draw_square(size)
    turtle.left(15)
    size = size +10
