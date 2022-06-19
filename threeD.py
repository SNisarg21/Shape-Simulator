from turtle import *
import turtle 
from turtle import colormode
from random import randint

CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Algerian', FONT_SIZE, 'bold')

class threeD():
    def cube(self, x, y):  
        turtle.clearscreen()
        turtle.width(4)
        colormode(255)
        turtle.bgcolor(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.fillcolor(randint(1, 255),
          randint(1, 255),
          randint(1, 255))
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(100)
            turtle.left(90)
        turtle.goto(50,50)
        for i in range(4):
            turtle.forward(100)
            turtle.left(90)
        turtle.goto(150,50)
        turtle.goto(100,0)
        turtle.goto(100,100)
        turtle.goto(150,150)
        turtle.goto(50,150)
        turtle.goto(0,100)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-300, 300)
        turtle.write("Surface Area of Cube = 6(side)^2 in square units", font=('Algerian', 13, 'italic'))
        turtle.goto(-300, 150)
        turtle.write("Volume of cube = (side)^3 cubic units", font=('Algerian', 13, 'italic'))
        turtle.goto(-300, -50)
        turtle.write("Area of one face = Area of a square = (side)^2", font=('Algerian', 13, 'italic'))
        turtle.goto(-300, -200)
        turtle.write("Lateral surface area (excluding the top and bottom faces) = 4 × Area of one face LSA = 4(side)^2", font=('Algerian', 13, 'italic'))

    def cuboid(self, x, y):
        turtle.clearscreen()
        turtle.width(4)
        colormode(255)
        turtle.bgcolor(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.fillcolor(randint(1, 255),
          randint(1, 255),
          randint(1, 255))
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(150)
            turtle.left(90)
        turtle.goto(50,50)
        for i in range(2):
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(150)
            turtle.left(90)
        turtle.goto(150,50)
        turtle.goto(100,0)
        turtle.goto(100,150)
        turtle.goto(150,200)
        turtle.goto(50,200)
        turtle.goto(0,150)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-300, 340)
        turtle.write("Surface Area of Cuboid = 2 x (length x width) + (width x height) + (length x height) in  square units", font=('Algerian', 13, 'italic'))
        turtle.goto(-300, 200)
        turtle.write("Volume of Cuboid = (length x width x height) cubic units", font=('Algerian', 13, 'italic'))
        turtle.goto(-300, -50)
        turtle.write("Area of one face = Area of a rectangle square units", font=('Algerian', 13, 'italic'))
        turtle.goto(-300, -200)
        turtle.write("Perimeter = 4(length + width + height) units", font=('Algerian', 13, 'italic'))

    def sphere(self, x, y):
        turtle.clearscreen()
        turtle.width(4)
        colormode(255)
        turtle.bgcolor(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.fillcolor(randint(1, 255),
          randint(1, 255),
          randint(1, 255))
        turtle.begin_fill()
        def draw(rad):
            for i in range(2):
                turtle.circle(rad,90)
                turtle.circle(rad//2,90)
        val=10
        turtle.speed(100)
        for i in range(36):
            turtle.seth(-val)
            draw(80)
            val+=10
        turtle.hideturtle()
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-300, 200)
        turtle.write("The Surface Area of a Sphere(SA) = 4π(radius)^2 Square units", font=('Algerian', 13, 'italic'))
        turtle.goto(-300, -200)
        turtle.write("Volume of cube = (4/3) x π x (radius)^3 cubic units", font=('Algerian', 13, 'italic'))
        

    def cylinder(self, x, y):
        turtle.clearscreen()
        turtle.width(4)
        colormode(255)
        turtle.bgcolor(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        cursor_size = 20
        rad, heigh = [50, 200] 
        turtle.shape('square')
        turtle.shapesize(rad*2 / cursor_size, heigh / cursor_size)
        turtle.fillcolor('dark blue')
        turtle.stamp()
        turtle.shape('circle')
        turtle.shapesize(stretch_len=rad / cursor_size)
        turtle.fillcolor('light blue')
        turtle.backward(heigh/2)
        turtle.stamp()
        turtle.forward(5)
        turtle.stamp()
        turtle.forward(heigh - 5)
        turtle.color('white')
        turtle.stamp()
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(-300, 200)
        turtle.write("Curved Surface Area = 2 x π x radius x height square units", font=('Algerian', 13, 'italic'))
        turtle.goto(-300, -100)
        turtle.write("Total surface area, A = 2 x π x radius x (radius + height) square units", font=('Algerian', 13, 'italic'))
        turtle.goto(-300, -300)
        turtle.write("Volume of the Cylinder, V = π x (radius)2 x height cubic units", font=('Algerian', 13, 'italic'))
        
        
