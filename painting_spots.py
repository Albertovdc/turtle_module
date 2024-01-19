import random
import turtle

# data = colorgram.extract("image.jpg", 30)
# color_list = []
# n = 0
# for _ in data:
#   r = data[n].rgb.r
#   g = data[n].rgb.g
#   b = data[n].rgb.b
#   color_list.append((r, b, g))
#   n += 1
#
# print(color_list)

color_list = [(202, 110, 164), (240, 241, 245), (236, 243, 239), (149, 50, 75), (222, 136, 201), (53, 123, 93), (170, 41, 154), (138, 20, 31)]

screen = turtle.Screen()
timmy = turtle.Turtle()
turtle.colormode(255)

timmy.penup()
timmy.hideturtle()
x_cor = -300
y_cor = -250
timmy.goto(x_cor, y_cor)
draw = True
while draw:
  timmy.dot(20, random.choice(color_list))
  timmy.forward(50)
  if timmy.xcor() > 250:
    y_cor += 50
    timmy.goto(x_cor, y_cor)
  elif x_cor >= 250 and y_cor == 250:
    timmy.dot(25, random.choice(color_list))
    draw = False
  print(y_cor)

screen.exitonclick()
