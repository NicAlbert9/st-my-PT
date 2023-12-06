import turtle

turtle.bgcolor('black')
turtle.pensize(2)
turtle.color('red')

for i in range(12):
    for colours in ['red', 'yellow', 'green', 'orange', 'blue', 'purple']:
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(5)
        turtle.speed(20)
turtle.done()

