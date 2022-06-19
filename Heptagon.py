import turtle
import IrregularAreaCalculator
from math import *
from turtle import colormode
from random import randint

class Heptagon():

    def regular(self, x, y):
        turtle.clearscreen()
        colormode(255)
        turtle.width(4)
        turtle.bgcolor(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.penup()
        turtle.goto(-150,-250)
        turtle.pendown()
        side = turtle.textinput("Heptagon", "Enter the Side")
        self.__side = float(side)
        turtle.fillcolor(randint(1, 255),
          randint(1, 255),
          randint(1, 255))
        turtle.begin_fill()
        for i in range(7):
            turtle.forward(self.__side)
            turtle.left(360/7)
        turtle.end_fill()
        turtle.color('white')
        turtle.penup()
        turtle.goto(-150, 250)
        turtle.write(f'Area => {3.6339*self.__side**2} square-units.', font=('Algerian', 15, 'bold'))
        turtle.goto(-150, 200)
        turtle.write(f'Perimeter => {7*self.__side} units.', font=('Algerian', 15, 'bold'))
        turtle.goto(-142 + (self.__side/2), -280)
        turtle.write(f'{self.__side}', font=('Algerian', 15, 'bold'))
        turtle.goto(-150, -305)
        turtle.pendown()
        turtle.write('Regular Heptagon', font=('Algerian', 12, 'bold'))
        turtle.forward(1.5*self.__side)

    def irregular(self, x, y):
        turtle.clearscreen()
        colormode(255)
        turtle.width(4)
        turtle.bgcolor(randint(1, 255),
                randint(1, 255),
                randint(1, 255))

        # side1 = turtle.textinput("Heptagon", "Enter the Side1")
        self.__side1 = float(134.2)
        # side2 = turtle.textinput("Heptagon", "Enter the Side2")
        self.__side2 = float(84.8)
        # side3 = turtle.textinput("Heptagon", "Enter the Side3")
        self.__side3 = float(63.2)
        # side4 = turtle.textinput("Heptagon", "Enter the Side4")
        self.__side4 = float(82.4)
        # side5 = turtle.textinput("Heptagon", "Enter the Side5")
        self.__side5 = float(80.6)
        # side6 = turtle.textinput("Heptagon", "Enter the Side6")
        self.__side6 = float(102.4)
        # side7 = turtle.textinput("Heptagon", "Enter the Side7")
        self.__side7 = float(82.4)

        # iT12 = turtle.textinput("Heptagon", "Enter the angle between Side1 and side2")
        self.__iT12 = float(101.34)
        # iT23 = turtle.textinput("Heptagon", "Enter the angle between Side2 and side3")
        self.__iT23 = float(145.43)
        # iT34 = turtle.textinput("Heptagon", "Enter the angle between Side3 and side4")
        self.__iT34 = float(147.63)
        # iT45 = turtle.textinput("Heptagon", "Enter the angle between Side4 and side5")
        self.__iT45 = float(107.17)
        # iT56 = turtle.textinput("Heptagon", "Enter the angle between Side5 and side6")
        self.__iT56 = float(137.89)
        # iT67 = turtle.textinput("Heptagon", "Enter the angle between Side6 and side7")
        self.__iT67 = float(143.01)

        turtle.fillcolor(randint(1, 255),
          randint(1, 255),
          randint(1, 255))
        turtle.begin_fill()
        x1 , y1 = turtle.pos()
        turtle.forward(self.__side1)
        x2 , y2 = turtle.pos()
        turtle.left(180 - self.__iT12)
        turtle.forward(self.__side2)
        x3 , y3 = turtle.pos()
        turtle.left(180 - self.__iT23)
        turtle.forward(self.__side3)
        x4 , y4 = turtle.pos()
        turtle.left(180 - self.__iT34)
        turtle.forward(self.__side4)
        x5 , y5 = turtle.pos()
        turtle.left(180 - self.__iT45)
        turtle.forward(self.__side5)
        x6 , y6 = turtle.pos()
        turtle.left(180 - self.__iT56)
        turtle.forward(self.__side6)
        x7 , y7 = turtle.pos()
        turtle.left(180 - self.__iT67)
        turtle.forward(self.__side7)
        turtle.end_fill()
        turtle.color('white')
        X = [x1, x2, x3, x4, x5, x6, x7]
        Y = [y1, y2, y3, y4, y5, y6, y7]
        self.__area = IrregularAreaCalculator.polygonArea(X, Y, 7)
        turtle.penup()
        turtle.setheading(0)
        turtle.goto(-275, 275)
        turtle.write(f"Area => {self.__area} square-units", font=('Algerian', 12, 'bold'))
        turtle.goto(-275, 215)
        turtle.write(f"Perimeter => {sum(X)} units", font=('Algerian', 12, 'bold'))
        turtle.goto(x1, y1 - 40)
        turtle.write(f"Irregular Heptagon", font=('Algerian', 12, 'bold'))
        turtle.pendown()
        turtle.forward(x2- x1)