import turtle

turtle.color('black')
style = ('Algerian', 30, 'italic')
greet = 'Shape Simulator!!'
turtle.penup()
turtle.goto(-200, 100)
turtle.write(greet, font=style)
turtle.penup()
turtle.pendown()
turtle.left(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(378)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(378)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.color('green')
turtle.speed(5)

def makeShape(numsides):
    for i in range(numsides):
        turtle.forward(100)
        turtle.left(360.0/numsides)

for i in range(2,8):
    makeShape(i)

turtle.mainloop()


