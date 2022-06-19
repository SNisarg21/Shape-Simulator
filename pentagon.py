import turtle
import IrregularAreaCalculator
from math import *
from turtle import colormode
from random import randint

class Pentagon():

    def regular(self, x, y):
        turtle.clearscreen()
        colormode(255)
        turtle.width(4)
        turtle.bgcolor(randint(1, 255),
          randint(1, 255),
          randint(1, 255))
        turtle.width(4)
        side = turtle.textinput("Pentagon", "Enter the Side")
        self.__side = float(side)
        turtle.fillcolor(randint(1, 255),
          randint(1, 255),
          randint(1, 255))
        turtle.begin_fill()
        for i in range(5):
            turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
            turtle.forward(self.__side)
            turtle.left(72)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.end_fill()
        turtle.color('white')
        turtle.penup()
        turtle.goto(self.__side*0.5, -20)
        turtle.color('white')
        turtle.write(f'{self.__side}', font=('Algerian', 15, 'bold'))
        turtle.goto(-250, -80)
        turtle.write(f'Area => {1.7205*self.__side**2} square-units.', font=('Algerian', 15, 'bold'))
        turtle.goto(-250, -140)
        turtle.write(f'Perimeter => {5*self.__side} units.', font=('Algerian', 15, 'bold'))
        turtle.goto(-250, -200)
        turtle.write(f'Interior Angle => {72}{chr(176)}.', font=('Algerian', 15, 'bold'))
        turtle.goto(0, -40)
        turtle.pendown()
        turtle.write('Regular Pentagon', font=('Algerian', 15, 'bold'))
        turtle.forward(self.__side*1.5)

    def irregular(self, x, y):

        turtle.clearscreen()
        colormode(255)
        turtle.width(4)
        turtle.bgcolor(randint(1, 255),
                randint(1, 255),
                randint(1, 255))

        side1 = turtle.textinput("Pentagon", "Enter the Side1")
        self.__side1 = float(side1)
        side2 = turtle.textinput("Pentagon", "Enter the Side2")
        self.__side2 = float(side2)
        side3 = turtle.textinput("Pentagon", "Enter the Side3")
        self.__side3 = float(side3)
        side4 = turtle.textinput("Pentagon", "Enter the Side4")
        self.__side4 = float(side4)
        side5 = turtle.textinput("Pentagon", "Enter the Side5")
        self.__side5 = float(side5)

        iT12 = turtle.textinput("Pentagon", "Enter the angle between Side1 and side2")
        self.__iT12 = float(iT12)
        iT23 = turtle.textinput("Pentagon", "Enter the angle between Side2 and side3")
        self.__iT23 = float(iT23)
        iT34 = turtle.textinput("Pentagon", "Enter the angle between Side3 and side4")
        self.__iT34 = float(iT34)
        iT45 = turtle.textinput("Pentagon", "Enter the angle between Side4 and side5")
        self.__iT45 = float(iT45)

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
        turtle.end_fill()
        turtle.color('white')
        X = [x1, x2, x3, x4, x5]
        Y = [y1, y2, y3, y4, y5]
        self.__area = IrregularAreaCalculator.polygonArea(X, Y, 5)
        turtle.penup()
        turtle.setheading(0)
        turtle.goto(-275, 275)
        turtle.write(f"Area => {self.__area} square-units", font=('Algerian', 15, 'bold'))
        turtle.goto(-275, 215)
        turtle.write(f"Perimeter => {sum(X)} units", font=('Algerian', 15, 'bold'))
        turtle.goto(x1, y1 - 40)
        turtle.write(f"Irregular pentagon", font=('Algerian', 15, 'bold'))
        turtle.pendown()
        turtle.forward(x2- x1)
