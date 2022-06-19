# from turtle import Screen, Turtle
from turtle import *
# import turtle
import Triangles
import Quadilaterals
import hexagon
import pentagon
import Heptagon
import threeD

CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'bold')

def exit_onclick(x, y):
    Screen().bye()

def triangle_onclick(x, y):
    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(-300, -150)
    button.write("Equilateral Triangle", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(Triangles.Triangles().makeEquilateral)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(-100, -150)
    button.write("Right Angled Triangle", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(Triangles.Triangles().makeRightAngled)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(100, -150)
    button.write("Scalene Triangle", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(Triangles.Triangles().makeScalene)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(300, -150)
    button.write("Isosceles Triangle", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(Triangles.Triangles().makeIsosceles)
    button.showturtle()


def quad_onclick(x, y):
    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(-300, -150)
    button.write("Parallelogram", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(Quadilaterals.Quadrilateral().makeParallelogram)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(-175, -150)
    button.write("Rhombus", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(Quadilaterals.Quadrilateral().makeRhombus)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(-50, -150)
    button.write("Square", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(Quadilaterals.Quadrilateral().makeSquare)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(50, -150)
    button.write("Rectangle", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(Quadilaterals.Quadrilateral().makeRectangle)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(160, -150)
    button.write("Kite", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(Quadilaterals.Quadrilateral().makeKite)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(250, -150)
    button.write("Trapezium", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(Quadilaterals.Quadrilateral().makeTrapezium)
    button.showturtle()

def pent_onclick(x, y):
    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(-150, -150)
    button.write("Regular Pentagon", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(pentagon.Pentagon().regular)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(150, -150)
    button.write("Irregular Pentagon", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(pentagon.Pentagon().irregular)
    button.showturtle()

def hex_onclick(x, y):
    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(-150, -150)
    button.write("Regular Hexagon", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(hexagon.Hexagon().regular)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(150, -150)
    button.write("Irregular Hexagon", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(hexagon.Hexagon().irregular)
    button.showturtle()

def hept_onclick(x, y):
    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(-150, -150)
    button.write("Regular Heptagon", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(Heptagon.Heptagon().regular)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(150, -150)
    button.write("Irregular Heptagon", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(Heptagon.Heptagon().irregular)
    button.showturtle()

def threeD_onclick(x, y):
    button = Turtle()
    button.hideturtle()
    button.shape('square')
    button.fillcolor('red')
    button.penup()
    button.goto(-300, -150)
    button.write("Cube", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(threeD.threeD().cube)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('square')
    button.fillcolor('red')
    button.penup()
    button.goto(-100, -150)
    button.write("Cuboid", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(threeD.threeD().cuboid)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('square')
    button.fillcolor('red')
    button.penup()
    button.goto(100, -150)
    button.write("Cylinder", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(threeD.threeD().cylinder)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(300, -150)
    button.write("Sphere", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 150)
    button.onclick(threeD.threeD().sphere)
    button.showturtle()


def show_onclick(x, y):

    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(350, -300)
    button.write("Exit", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE - 300)
    button.onclick(exit_onclick)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('triangle')
    button.fillcolor('red')
    button.penup()
    button.goto(-300, 0)
    button.write("Triangle", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE)
    button.onclick(triangle_onclick)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('square')
    button.fillcolor('red')
    button.penup()
    button.goto(-150, 0)
    button.write("Quadrilateral", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE)
    button.onclick(quad_onclick)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(0, 0)
    button.write("Pentagon", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE)
    button.onclick(pent_onclick)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(150, 0)
    button.write("Hexagon", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE)
    button.onclick(hex_onclick)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(300, 0)
    button.write("Heptagon", align='center', font=FONT)
    button.sety(CURSOR_SIZE + FONT_SIZE)
    button.onclick(hept_onclick)
    button.showturtle()


def start():
    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(-150, 150)
    button.write("Polygon", align='center', font=FONT)
    button.sety(150 + CURSOR_SIZE + FONT_SIZE)
    button.onclick(show_onclick)
    button.showturtle()

    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(150, 150)
    button.write("3D", align='center', font=FONT)
    button.sety(150 + CURSOR_SIZE + FONT_SIZE)
    button.onclick(threeD_onclick)
    button.showturtle()

start()

turtle = Turtle()
turtle.hideturtle()

screen = Screen()
screen.mainloop()


















# import turtle as t
# win = t.getscreen()
# win.setup(800, 600)
# win.bgcolor('black')
#
# tt = t.Turtle()
# tt.color('blue')
#
# def work():
#     for i in range(4):
#         tt.lt(90)
#         tt.forward(100)
#
# work()