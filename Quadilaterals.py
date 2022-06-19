import turtle
from math import *
from turtle import colormode
from random import randint

CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Algerian', FONT_SIZE, 'bold')

class Quadrilateral():

    def makeParallelogram(self, x, y):
        turtle.clearscreen()
        turtle.width(4)
        colormode(255)
        turtle.bgcolor(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        side1 = turtle.textinput("Parallelogram", "Enter the Side1")
        self.__side1 = float(side1)
        side2 = turtle.textinput("Parallelogram", "Enter the Side2")
        self.__side2 = float(side2)
        iT12 = turtle.textinput("Parallelogram", "Enter the Angle included in degrees")
        self.__iT12 = float(iT12)
        turtle.penup()
        turtle.goto(-100, 100) 
        turtle.pendown()
        
        turtle.fillcolor(randint(1, 255),
          randint(1, 255),
          randint(1, 255))
        turtle.begin_fill()
        turtle.forward(self.__side1)
        turtle.left(self.__iT12)
        turtle.forward(self.__side2)
        x, y = turtle.position()
        turtle.left(180 - self.__iT12)
        turtle.forward(self.__side1)
        turtle.left(self.__iT12)
        turtle.forward(self.__side2)
        turtle.end_fill()
        turtle.setheading(0)
        turtle.penup()
        turtle.goto(-100 + (self.__side1 / 2), 80)
        turtle.color('white')
        turtle.write(f'{self.__side1}', font=('Algerian', 13, 'bold'))
        turtle.goto((-100 + self.__side1 + x) / 2, (100 + y) / 2)
        turtle.color('white')
        turtle.write(f'{self.__side2}', font=('Algerian', 13, 'bold'))
        turtle.penup()
        turtle.goto(-100, 60)
        turtle.penup()
        turtle.write("Parallelogram", font=('Algerian', 13, 'bold'))
        turtle.pendown()
        turtle.forward(self.__side1)
        turtle.penup()
        turtle.goto(-100, -50)
        if self.__iT12 > 90:
            turtle.write(f"Area => {self.__side1*self.__side2*sin((180 - self.__iT12)*pi/180)} square-units", font=('Algerian', 13, 'bold'))
            turtle.goto(-100, -150)
            turtle.write(f"Obtuse Angle => {self.__iT12}{chr(176)} ......... Acute Angle => {180 - self.__iT12}{chr(176)}", font=('Algerian', 13, 'bold'))
        elif self.__iT12 == 90:
            turtle.write(f'Area => {self.__side1*self.__side2} square-units', font=('Algerian', 13, 'bold'))
            turtle.goto(-100, -150)
            turtle.write(f"Right Angles => {self.__iT12}{chr(176)}", font=('Algerian', 13, 'bold'))
        else:
            turtle.write(f"Area => {self.__side1*self.__side2*sin(self.__iT12*pi/180)} square-units", font=('Algerian', 13, 'bold'))
            turtle.goto(-100, -150)
            turtle.write(f"Acute Angle => {self.__iT12}{chr(176)} ......... Obtuse Angle => {180 - self.__iT12}{chr(176)}", font=('Algerian', 13, 'bold'))
        turtle.goto(-100, -100)
        turtle.write(f"Perimeter => {2*(self.__side1 + self.__side2)}", font=('Algerian', 13, 'bold'))


    def makeRhombus(self, x, y):
        turtle.clearscreen()
        colormode(255)
        turtle.width(4)
        turtle.bgcolor(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        side = turtle.textinput("Rhombus", "Enter the Side")
        self.__side = float(side)
        iT = turtle.textinput("Rhombus", "Enter the Angle included in degrees")
        self.__iT = float(iT)
        turtle.penup()
        turtle.goto(-120, 100)
        turtle.pendown()
        
        turtle.fillcolor(randint(1, 255),
          randint(1, 255),
          randint(1, 255))
        turtle.begin_fill()
        turtle.forward(self.__side)
        turtle.left(self.__iT)
        turtle.forward(self.__side)
        x, y = turtle.position()
        turtle.left(180 - self.__iT)
        turtle.forward(self.__side)
        turtle.left(self.__iT)
        turtle.forward(self.__side)
        turtle.end_fill()
        turtle.setheading(0)
        turtle.penup()
        turtle.color('white')
        turtle.goto(-120 + (self.__side/2), 80)
        turtle.write(f'{self.__side}', font=('Algerian', 13, 'bold'))
        turtle.goto(-120, -150)
        if self.__iT > 90:
            turtle.write(f"Area => {(self.__side**2)*sin((180 - self.__iT)*pi/180)} square-units", font=('Algerian', 13, 'bold'))
            turtle.goto(-120, -250)
            turtle.write(f"Obtuse Angle => {self.__iT}{chr(176)} ............. Acute Angle => {180 - self.__iT}{chr(176)}", font=('Algerian', 13, 'bold'))
        elif self.__iT == 90:
            turtle.write(f'Area => {self.__side**2} square-units', font=('Algerian', 13, 'bold'))
            turtle.goto(-120, -250)
            turtle.write(f"Right Angles => {self.__iT}{chr(176)}", font=('Algerian', 13, 'bold'))
        else:
            turtle.write(f"Area => {(self.__side**2)*sin(self.__iT*pi/180)} square-units", font=('Algerian', 13, 'bold'))
            turtle.goto(-120, -250)
            turtle.write(f"Acute Angle => {self.__iT}{chr(176)} ......... Obtuse Angle => {180 - self.__iT}{chr(176)}", font=('Algerian', 13, 'bold'))
        turtle.goto(-120, -200)
        turtle.write(f"Perimeter => {4*self.__side}", font=('Algerian', 13, 'bold'))
        turtle.penup()
        turtle.goto(-120, 60)
        turtle.penup()
        turtle.write("Rhombus", font=('Algerian', 13, 'bold'))
        turtle.pendown()
        turtle.forward(self.__side)

    def makeSquare(self, x, y):
        turtle.clearscreen()
        colormode(255)
        turtle.width(4)
        turtle.bgcolor(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        side = turtle.textinput("Square", "Enter the Side")
        self.__side = float(side)
        turtle.penup()
        turtle.goto(80, 100)
        turtle.pendown()
        turtle.fillcolor(randint(1, 255),
          randint(1, 255),
          randint(1, 255))
        turtle.begin_fill()
        def makeShape(numsides):
            for i in range(numsides):
                turtle.forward(self.__side)
                turtle.left(360.0/numsides)
        makeShape(4)
        turtle.end_fill()
        turtle.color('white')
        turtle.penup()
        turtle.goto(80, 60)
        turtle.penup()
        turtle.write("Square", font=('Arial', 10, 'italic'))
        turtle.pendown()
        turtle.forward(self.__side)
        turtle.penup()
        turtle.goto(80 + (self.__side / 2),80)
        turtle.color('white')
        turtle.write(f'{self.__side}',font=('Algerian', 13, 'bold'))
        turtle.goto(-250, 250)
        turtle.write(f'Area = {self.__side**2} square-units',font=('Algerian', 13, 'bold'))
        turtle.goto(-250, 0)
        turtle.write(f'Perimeter = {self.__side*4} units',font=('Algerian', 13, 'bold'))

    def makeRectangle(self, x, y):
        turtle.clearscreen()
        colormode(255)
        turtle.width(4)
        turtle.bgcolor(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        length = turtle.textinput("Rectangle", "Enter the Length")
        self.__length = float(length)
        breadth = turtle.textinput("Rectangle", "Enter the Breadth")
        self.__breadth = float(breadth)
        turtle.penup()
        turtle.goto(-300, -150)
        turtle.pendown()
        turtle.fillcolor(randint(1, 255),
          randint(1, 255),
          randint(1, 255))
        turtle.begin_fill()
        def makeShape(numsides):
            for i in range(numsides):
                if i % 2 == 0:
                 turtle.forward(self.__length)
                else:
                    turtle.forward(self.__breadth)
                turtle.left(360.0/numsides)
        makeShape(4)
        turtle.end_fill()
        turtle.color('white')
        turtle.penup()
        turtle.goto(-300, -190)
        turtle.write("Rectangle", font=('Algerian', 13, 'bold'))
        turtle.pendown()
        turtle.forward(self.__length)
        turtle.penup()
        turtle.goto(-300 + (self.__length / 2), -170)
        turtle.color('white')
        turtle.write(f'{self.__length}', font=('Algerian', 13, 'bold'))
        turtle.goto(-300 + self.__length, -150 + (self.__breadth / 2))
        turtle.color('white')
        turtle.write(f'{self.__breadth}', font=('Algerian', 13, 'bold'))
        turtle.goto(100, 250)
        turtle.write(f'Area => {self.__breadth*self.__length} square-units', font=('Algerian', 13, 'bold'))
        turtle.goto(100, 150)
        turtle.write(f'Perimeter => {2*(self.__breadth+self.__length)} units.', font=('Algerian', 13, 'bold'))


    def makeKite(self, x, y):
        turtle.clearscreen()
        colormode(255)
        turtle.width(4)
        turtle.bgcolor(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        side1 = turtle.textinput("Kite", "Enter the side1")
        self.__side1 = float(side1)
        side2 = turtle.textinput("Kite", "Enter the side2")
        self.__side2 = float(side2)
        iT12 = turtle.textinput("Kite", "Enter the Angle included between sides side1 and side2")
        self.__iT12 = float(iT12)
        op = turtle.textinput("Kite", "Enter the Option number ... 1. Included between 2 sides of side1 2. Included between 2 sides of side2")
        if op == '1':
            iT1 =  float(turtle.textinput("Kite", "Enter the Angle included between sides of side1"))
            self.__iT1 = iT1
            self.__iT2 = 360 - 2*self.__iT12 - self.__iT1
        elif op == '2':
            iT2 = float(turtle.textinput("Kite", "Enter the Angle included between sides of side2"))
            self.__iT2 = iT2
            self.__iT1 = 360 - 2*self.__iT12 - self.__iT2
        turtle.penup()
        turtle.goto(-120, 0)
        turtle.pendown()
        turtle.right(self.__iT1/2)
        turtle.fillcolor(randint(1, 255),
          randint(1, 255),
          randint(1, 255))
        turtle.begin_fill()
        turtle.forward(self.__side1)
        xd, yd = turtle.pos()
        turtle.left(180 - self.__iT12)
        turtle.forward(self.__side2)
        xr, yr = turtle.pos()
        turtle.left(180 - self.__iT2)
        turtle.forward(self.__side2)
        xt, yt = turtle.pos()
        d1 = yt - yd
        d2 = xr + 120
        turtle.left(180 - self.__iT12)
        turtle.forward(self.__side1)
        turtle.end_fill()
        turtle.setheading(0)
        turtle.penup()
        turtle.goto((-120 + xd) / 2, yd / 2)
        turtle.color('white')
        turtle.write(f"{self.__side1}", font=('Algerian', 13, 'bold'))
        turtle.goto((xr + xd) / 2, (yd + yr) / 2)
        turtle.color('white')
        turtle.write(f"{self.__side2}", font=('Algerian', 13, 'bold'))
        turtle.goto(xd, yd + 10)
        turtle.color('white')
        turtle.write(f"{self.__iT12}{chr(176)}", font=('Algerian', 13, 'bold'))
        turtle.goto(-120, yt + 200)
        turtle.write(f"Area => {0.5*d1*d2} square-units", font=('Algerian', 13, 'bold'))
        turtle.goto(-120, yt + 150)
        turtle.write(f"Perimeter => {2*(self.__side1 + self.__side2)} units", font=('Algerian', 13, 'bold'))
        turtle.goto(-120, yt + 100)
        turtle.write(f"Diagonal lenghts => {d1}, {d2} units", font=('Algerian', 13, 'bold'))
        turtle.goto(-120, yd - 100)
        turtle.write(f"Angles => Angle included between sides of length {self.__side1} and {self.__side2} is {self.__iT12}{chr(176)}\n\t Angle included between two sides of length {self.__side1} is {self.__iT1}{chr(176)}\n\tAngle included between two sides of length {self.__side2} is {self.__iT2}{chr(176)}", font=('Algerian', 13, 'bold'))
        turtle.goto(-120, yd -25)
        turtle.write("Kite", font=('Algerian', 13, 'bold'))
        turtle.pendown()
        turtle.forward(2*max(self.__side1,self.__side2))


    def makeTrapezium(self, x, y):
        turtle.clearscreen()
        colormode(255)
        turtle.width(4)
        turtle.bgcolor(randint(1, 255),
                randint(1, 255),
                randint(1, 255))
        side1 = turtle.textinput("Trapezium", "Enter the side1")
        self.__side1 = float(side1)
        side2 = turtle.textinput("Trapezium", "Enter the side2")
        self.__side2 = float(side2)
        side3 = turtle.textinput("Trapezium", "Enter the side3")
        self.__side3 = float(side3)
        side4 = turtle.textinput("Trapezium", "Enter the side4")
        self.__side4 = float(side4)
        iT12 = turtle.textinput("Trapezium", "Enter the angle included between side1 and side2")
        self.__iT12 = float(iT12)
        iT14 = turtle.textinput("Trapezium", "Enter the angle included between side1 and side4")
        self.__iT14 = float(iT14)
        turtle.penup()
        turtle.goto(20, -150)
        turtle.pendown()
        turtle.fillcolor(randint(1, 255),
          randint(1, 255),
          randint(1, 255))
        turtle.begin_fill()
        turtle.forward(self.__side1)
        xrd, yrd = turtle.pos()
        turtle.left(180 - self.__iT12)
        turtle.forward(self.__side2)
        xrt, yrt = turtle.pos()
        turtle.left(self.__iT12)
        turtle.forward(self.__side3)
        xlt, ylt = turtle.pos()
        turtle.left(self.__iT14)
        turtle.forward(self.__side4)
        turtle.end_fill()
        turtle.setheading(0)
        turtle.penup()
        turtle.goto(30, -145)
        turtle.color('white')
        turtle.write(f"{self.__iT14}{chr(176)}", font=('Algerian', 13, 'bold'))
        turtle.goto(xrd - 10 , -145)
        turtle.color('white')
        turtle.write(f"{self.__iT12}{chr(176)}", font=('Algerian', 13, 'bold'))
        turtle.goto((20 + xrd) / 2, -150)
        turtle.color('white')
        turtle.write(f"{self.__side1}", font=('Algerian', 13, 'bold'))
        turtle.goto((xrt + xrd) / 2, (-150 + yrt) / 2)
        turtle.color('white')
        turtle.write(f"{self.__side2}", font=('Algerian', 13, 'bold'))
        turtle.goto((xlt + xrt) / 2, (ylt + yrt) / 2)
        turtle.color('white')
        turtle.write(f"{self.__side3}", font=('Algerian', 13, 'bold'))
        turtle.goto((20 + xlt) / 2, (-150 + ylt) / 2)
        turtle.color('white')
        turtle.write(f"{self.__side4}", font=('Algerian', 13, 'bold'))
        turtle.goto(-250, 250)
        turtle.write(f"Area => {((self.__side1 + self.__side3) / 2) * (ylt+150)} square-units", font=('Algerian', 13, 'bold'))
        turtle.goto(-250, 150)
        turtle.write(f"Perimeter => {self.__side1 + self.__side2 + self.__side3 + self.__side4} units", font=('Algerian', 13, 'bold'))
        turtle.goto(-250, 50)
        turtle.write(f"Interior Angles => {self.__iT12}{chr(176)}, {180 - self.__iT12}{chr(176)}, {180 - self.__iT14}{chr(176)}, {self.__iT14}{chr(176)}", font=('Algerian', 13, 'bold'))
        turtle.goto(20, -190)
        turtle.write("Trapezium", font=('Algerian', 13, 'bold'))
        turtle.pendown()
        turtle.forward(160)


# q = Quadrilateral()
# q.makeParallelogram()
# q.makeRhombus()
# q.makeSquare()
# q.makeRectangle()
# q.makeKite()
# q.makeTrapezium()
# q.start()

