import turtle

import colorgram
from turtle import Turtle, Screen
import random

rgb_colors = []
colors = colorgram.extract("hirst.jpg", 30)

tim = Turtle()
tim.hideturtle()
tim.up()

turtle.colormode(255)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.r
#     b = color.rgb.r
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(0, 0, 55), (91, 56, 84), (93, 52, 25), (27, 47, 30)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_dots = 100

for col in range(1, num_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if col % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

window = Screen()
window.exitonclick()