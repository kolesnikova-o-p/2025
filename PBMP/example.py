import turtle

t = turtle.Turtle()
t.speed(5)
turtle.bgcolor("skyblue")

t.penup()
t.goto(-100, -100)  
t.pendown()
t.color("brown")
t.begin_fill()
for i in range(2):
    t.forward(200)  
    t.left(90)
    t.forward(150)   
    t.left(90)
t.end_fill()

t.penup()
t.goto(-40, -40)
t.pendown()
t.color("yellow")
t.begin_fill()
for i in range(4):
    t.forward(80)
    t.left(90)
t.end_fill()


t.penup()
t.goto(-100, 50) 
t.pendown()
t.color("peru")
t.begin_fill()
t.goto(0, 150)     # вершина крыши (по центру)
t.goto(100, 50)    # правая точка крыши
t.goto(-100, 50)   # возвращаемся влево
t.end_fill()

t.penup()
t.goto(40, 80)   
t.pendown()
t.color("sienna")
t.begin_fill()
for i in range(2):
    t.forward(30)
    t.left(90)
    t.forward(60)
    t.left(90)
t.end_fill()


t.penup()
t.goto(55, 140)  
t.pendown()
t.color("gray")
for r in [15, 20, 25]:
    t.penup()
    t.goto(55, 140 + r * 2) 
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()

turtle.done()