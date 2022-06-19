from tkinter import Button
import turtle
from turtle import *
from math import *
from turtle import colormode
from random import randint

CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Algerian', FONT_SIZE, 'bold')

class Triangles():

    def makeEquilateral(self, x, y):
        turtle.clearscreen()
        turtle.width(4)
        colormode(255)
        turtle.bgcolor(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        side = turtle.textinput("Equilateral Triangle", "Enter the Side")
        self.__side = float(side)
        turtle.penup()
        turtle.goto(-250, 0)
        turtle.pendown()
        turtle.fillcolor(randint(1, 255),
          randint(1, 255),
          randint(1, 255))
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(self.__side)
            turtle.left(120)
        turtle.penup()
        turtle.end_fill()
        turtle.goto(-242,0)
        turtle.color('white')
        turtle.write(f"{60}{chr(186)}", font=('Algerian', 13, 'italic'))
        turtle.penup()
        turtle.goto(-287+self.__side,0)
        turtle.color('white')
        turtle.write(f"{60}{chr(186)}", font=('Algerian', 13, 'italic'))
        turtle.penup()
        turtle.goto(-262+(self.__side/2), (sqrt(3)*self.__side/2)-38)
        turtle.color('white')
        turtle.write(f"{60}{chr(186)}", font=('Algerian', 13, 'italic'))
        turtle.goto(-250, -20)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.penup()
        turtle.write("Equilateral Triangle", font=('Algerian', 13, 'italic'))
        turtle.pendown()
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.forward(180)
        turtle.penup()
        turtle.goto(150, 150)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.write(f'Area = {sqrt(3)/4*self.__side**2} square-units',font=('Algerian', 13, 'bold'))
        turtle.goto(150, 0)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.write(f'Perimeter = {self.__side*3} units',font=('Algerian', 13, 'bold'))
        turtle.goto(150, -150)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.write(f'Exterior Angle 120{chr(186)}',font=('Algerian', 13, 'bold'))
        return

    def makeRightAngled(self, x, y):
        turtle.clearscreen()
        turtle.width(4)
        colormode(255)
        turtle.bgcolor(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        base = turtle.textinput("Right-Angled Triangle", "Enter the Base")
        self.__base = float(base)
        height = turtle.textinput("Right-Angled Triangle", "Enter the Height")
        self.__height = float(height)
        hypotenuse = sqrt((self.__base)**2 + (self.__height)**2)
        self.__hypotenuse = float('{:.2f}'.format(hypotenuse))
        turtle.penup()
        turtle.goto(-50, 0)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.pendown()
        theta = atan(self.__height/self.__base)
        self.__theta = theta*180/pi
        turtle.fillcolor(randint(1, 255),
          randint(1, 255),
          randint(1, 255))
        turtle.begin_fill()
        turtle.forward(self.__base)
        turtle.left(180-self.__theta)
        turtle.forward(self.__hypotenuse)
        turtle.left(90+self.__theta)
        turtle.forward(self.__height)
        turtle.end_fill()
        turtle.setheading(0)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.penup()
        turtle.goto(-50, -40)
        turtle.write("Right Angled Triangle", font=('Algerian', 13, 'italic'))
        turtle.pendown()
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.forward(1.5*self.__base)
        turtle.penup()
        self.__theta = '{:.2f}'.format(self.__theta)
        turtle.goto(-50 + self.__base/2, -20)
        turtle.color('white')
        turtle.write(f"{self.__base}", font=('Algerian', 13, 'bold'))
        turtle.goto(-58, self.__height/2)
        turtle.color('white')
        turtle.write(f"{self.__height}", font=('Algerian', 13, 'bold'))
        turtle.goto(-76+self.__base, 10)
        turtle.color('white')
        turtle.write(f"{self.__theta}{chr(176)}", font=('Algerian', 13, 'bold'))
        turtle.goto(-50,10)
        turtle.color('white')
        turtle.write(f"{90}{chr(176)}", font=('Algerian', 13, 'bold'))
        turtle.goto(-50, self.__height-20)
        turtle.color('white')
        ang = 90-float(self.__theta)
        self.__ang = '{:.2f}'.format(ang)
        turtle.write(f"{self.__ang}{chr(176)}", font=('Algerian', 13, 'bold'))
        turtle.goto(200,150)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.write(f'Area is {0.5*self.__base*self.__height} square-units', font=('Algerian', 13, 'bold'))
        turtle.goto(150,0)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.write(f'Perimeter is {self.__base+self.__height+self.__hypotenuse} units', font=('Algerian', 13, 'bold'))
        turtle.goto(150,-150)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.write(f'Hypotenuse is {(self.__hypotenuse)} units', font=('Algerian', 13, 'bold'))
        turtle.pendown()
        turtle.penup()

    def makeScalene(self, x, y):
        turtle.clearscreen()
        turtle.width(4)
        colormode(255)
        turtle.bgcolor(randint(1, 255),
                randint(1, 255),
                randint(1, 255))

        op = turtle.textinput("Scalene Triangle", "Choose The option : 1.SSS 2.SAS")
        side1 = turtle.textinput("Scalene Triangle", "Enter the Side1")
        self.__side1 = float(side1)
        side2 = turtle.textinput("Scalene Triangle", "Enter the Side2")
        self.__side2 = float(side2)
        if op == '1':
            side3 = turtle.textinput("Scalene Triangle", "Enter the Side3")
            self.__side3 = float(side3)
            iT12 = acos((self.__side1**2 + self.__side2**2 - self.__side3**2)/(2*self.__side1*self.__side2))
            self.__iT12 = float('{:.2f}'.format(iT12))
        elif op == '2':
            iT12 = float(turtle.textinput("Scalene Triangle", "Enter the Angular Included in degrees"))
            self.__iT12 = float('{:.2f}'.format(iT12*pi/180))
            side3 = sqrt(self.__side1**2 + self.__side2**2 - 2*self.__side1*self.__side2*cos(self.__iT12))
            self.__side3 = float('{:.2f}'.format(side3))

        iT13 = asin(self.__side2/self.__side3*sin(self.__iT12))
        self.__iT13 = float('{:.2f}'.format(iT13))
        iT23 = asin(self.__side1/self.__side3*sin(self.__iT12))
        self.__iT23 = float('{:.2f}'.format(iT23))

        turtle.penup()
        turtle.goto(150, 0)
        turtle.pendown()
        turtle.fillcolor(randint(1, 255),
          randint(1, 255),
          randint(1, 255))
        turtle.begin_fill()
        turtle.forward(self.__side1)
        turtle.left(180-self.__iT12*180/pi)
        turtle.forward(self.__side2)
        x, y = turtle.position()
        turtle.left(180-self.__iT23*180/pi)
        turtle.forward(self.__side3)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(150 + self.__side1/2, -20)
        turtle.color('white')
        turtle.write(f"{self.__side1}", font=('Algerian', 13, 'bold'))
        turtle.goto((150+self.__side1+x)/2, y/2)
        turtle.color('white')
        turtle.write(f"{self.__side2}", font=('Algerian', 13, 'bold'))
        turtle.goto((150+x)/2,y/2)
        turtle.color('white')
        turtle.write(f"{self.__side3}", font=('Algerian', 13, 'bold'))
        turtle.setheading(0)
        turtle.goto(150, -40)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.write("Scalene Triangle", font=('Algerian', 13, 'bold'))
        turtle.pendown()
        turtle.goto(325, -40)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.penup()
        turtle.goto(-250,150)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.write(f"Angles => A : {'{:.2f}'.format(self.__iT23*180/pi)} ; B : {'{:.2f}'.format(self.__iT13*180/pi)} ; C : {'{:.2f}'.format(self.__iT12*180/pi)}", font=('Algerian', 13, 'bold'))
        turtle.goto(-250,100)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.write(f"Sides => AB : {self.__side3} ; BC : {self.__side1} ; AC : {self.__side2}",font=('Algerian', 13, 'bold'))
        turtle.goto(-250,-80)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.write(f"Area => {0.5*self.__side1*self.__side2*sin(iT12)} square-units", font=('Algerian', 13, 'bold'))
        turtle.goto(-250, -250)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.write(f"Perimeter => {self.__side1 + self.__side2 + self.__side3} units", font=('Algerian', 13, 'bold'))
    

    def makeIsosceles(self, x, y):
        turtle.clearscreen()
        turtle.width(4)
        colormode(255)
        turtle.bgcolor(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        base = float(turtle.textinput("Isosceles Triangle", "Enter the base"))
        self.__base = base
        commonSide = float(turtle.textinput("Isosceles Triangle", "Enter the commonSide"))
        self.__commonSide = commonSide

        self.__iT12 = (acos(self.__base**2/(2*self.__base*self.__commonSide)))*180/pi
        self.__iT23 = (acos((2*(self.__commonSide**2) - self.__base**2)/(2*self.__commonSide**2)))*180/pi

        turtle.penup()
        turtle.goto(-50, -275)
        turtle.pendown()
        turtle.setheading(0)
        turtle.fillcolor(randint(1, 255),
          randint(1, 255),
          randint(1, 255))
        turtle.begin_fill()
        turtle.forward(self.__base)
        turtle.left(180-self.__iT12)
        turtle.forward(self.__commonSide)
        x, y = turtle.position()
        turtle.left(180 - self.__iT23)
        turtle.forward(self.__commonSide)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(-50, -305)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.write("Isosceles Triangle", font=('Algerian', 13, 'italic'))
        turtle.pendown()
        turtle.goto(120, -305)
        turtle.penup()
        turtle.goto(-50+(self.__base/2), -290)
        turtle.color('white')
        turtle.write(f"{self.__base}", font=('Algerian', 13, 'bold'))
        turtle.goto((-50 + self.__base + x)/2, (-275 + y)/2)
        turtle.color('white')
        # turtle.write(f"{self.__commonSide}", font=('Algerian', 13, 'bold'))
        # turtle.goto((-50 + x)/2, (-275 + y)/2)
        turtle.color('white')
        turtle.write(f"{self.__commonSide}", font=('Algerian', 13, 'bold'))
        turtle.goto(-50, 250)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.write(f"Angles => A : {'{:.2f}'.format(self.__iT23)} ; B : {'{:.2f}'.format(self.__iT12)} ; C : {'{:.2f}'.format(self.__iT12)}", font=('Algerian', 13, 'bold'))
        turtle.goto(-50,175)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.write(f"Sides => AB : {self.__commonSide} ; BC : {self.__base} ; AC : {self.__commonSide}",font=('Algerian', 13, 'bold'))
        turtle.goto(-50,75)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.write(f"Area => {0.5*self.__base*self.__commonSide*sin(self.__iT12*pi/180)} square-units", font=('Algerian', 13, 'bold'))
        turtle.goto(-50, 0)
        turtle.color(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        turtle.write(f"Perimeter => {self.__base + 2*self.__commonSide} units", font=('Algerian', 13, 'bold'))
    


# t = Triangles()
# t.makeEquilateral()
# t.makeRightAngled()
# t.makeScalene()
# t.makeIsosceles()
# t.start()

