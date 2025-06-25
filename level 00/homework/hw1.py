from turtle import *

#we want to paint a house
#step 1: draw a square
color("purple")
width(6)


#start of the square
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
#end of the square


backward(200)
#start of the roof
right(220)
forward(160) #height of the roof
right(100.5)
forward(155) #height of the roof
#end of the roof


right(40)
penup()
goto(200, 0)
pendown()
right(90)


#start of the door
forward(95)
color("green") #color of the door
right(90)
forward(70) #height of the door
left(90)
forward(40)
left(90)
forward(70)
color("purple") #height of the door
right(90)
#end of the door


forward(65)
exitonclick()