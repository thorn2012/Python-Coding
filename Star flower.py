import turtle
turtle.speed(0)
def draw_star(size):
    for i in range(5):
        turtle.forward(size)
        turtle.left(144)
size = 50
for s in range(30):
    draw_star(size)
    turtle.left(15)
    size = size + 10
