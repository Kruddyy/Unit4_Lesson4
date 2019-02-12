from turtle import *


dog = Turtle()
screen = Screen()
screen.bgcolor("purple")

dog.color("green")
dog.pensize(4)
dog.speed(4)dog.shape("turtle")

for x in range(12):
	dog.circle(80)
	dog.left(30)


mainloop()