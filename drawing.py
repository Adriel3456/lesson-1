import turtle
import random

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("different shapes")

pen = turtle.Turtle()
pen.speed(20)

pen.penup
def draw_square():
    for i in range(4):
        pen.forward(50)
        pen.right(90)
        pen.pendown
    
pen.penup
def draw_triangle():
    for t in range(3):
        pen.forward(50)
        pen.right(120)
        pen.pendown

pen.penup
def draw_circle():
    pen.circle(25)
    pen.pendown

for i in range(10):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    pen.penup
    pen.goto(x, y)
    pen.pendown()


    pen.pencolor(random.choice(["red", "green", "blue", "orange", "purple", "black"]))

    shape_type = random.randint(1, 3)
