from turtle import Turtle, Screen
import time

from random import randint

# turtle.color("red")
# turtle.begin_fill()
# turtle.circle(50)
# turtle.end_fill()
# turtle.color("black")
# turtle.forward(200)
# turtle.color("blue")
# turtle.begin_fill()
# turtle.circle(100)
# turtle.end_fill()
# turtle.forward(80)
# turtle.goto(-30, -50)
# turtle.write((0, 0), True, font=("Times New Roman", 30, "bold"))
# turtle.forward(50)

screen = Screen()
screen.setup(1200, 900)

turtle = Turtle()

turtle.forward(200)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(80)
turtle.left(180)
turtle.begin_fill()
turtle.color("red")
turtle.forward(40)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(200)
turtle.end_fill()
turtle.penup()
# turtle.forward(300)
turtle.goto(80, 50)
turtle.write("POLAND")

time.sleep(5)

# def throw():
#     number = randint(1, 6)
#     print(number)
#
#
# resignation = False
# while not resignation:
#     throw()
#     answer = input("Do you want to play again? ")
#     if answer.lower() == "yes":
#         continue
#     else:
#         resignation = True
