#    @Vipin Yadav
import turtle
from random import randint

# for header Beauty 
bla=turtle.Turtle()
bla.penup()
bla.shape('turtle')
bla.color('orange')
bla.goto(-100,180)
bla.speed(3)
bla.forward(30)
bla.write('Guess Your Lucky Turtle!!!')
bla.backward(50)

#for line drawing and number writing
vip=turtle.Turtle()
vip.penup()
vip.goto(-140,140)
vip.speed(0)



for step in range(15):
    vip.write(step, align='center')  # for text alignment
    vip.right(90)
    vip.forward(10)
    vip.pendown()
    vip.forward(150)
    vip.penup()
    vip.backward(160)
    vip.left(90)
    vip.forward(20)

    # First turtle properties
turtle1=turtle.Turtle()
turtle1.shape('turtle')
turtle1.color('red')
turtle1.penup()
turtle1.goto(-160,100)
turtle1.pendown()
   
# second Turtle properties    
tur=turtle.Turtle()
tur.shape('turtle')
tur.color('green')
tur.penup()
tur.goto(-160,80)
tur.pendown()

#Third turtle properties
turtle3=turtle.Turtle()
turtle3.shape('turtle')
turtle3.color('pink')
turtle3.penup()
turtle3.goto(-160,60)
turtle3.pendown()
 
# fourth turtle properties  
turtle4=turtle.Turtle()
turtle4.shape('turtle')
turtle4.color('yellow')
turtle4.penup()
turtle4.goto(-160,40)
turtle4.pendown()

# for fifth turtle properties
turtle5=turtle.Turtle()
turtle5.shape('turtle')
turtle5.color('blue')
turtle5.penup()
turtle5.goto(-160,20)
turtle5.pendown()

for turn in range(100):
    turtle1.forward(randint(1,5))   # turtle speed using random moduel
    tur.forward(randint(1,5))
    turtle3.forward(randint(1,5))
    turtle4.forward(randint(1,5))
    turtle5.forward(randint(1,5))                


