import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
t.speed(10)
# Need this line for rgb colors
turtle.colormode(255)

def draw_circle(times):
  t.speed("fastest")
  for _ in range(int(360 / times)):
    t.circle(100)
    # t.right(10)
    t.setheading(t.heading() + times)
    t.color(random_color())

def random_color():
  r = random.randint(0,255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)

draw_circle(10)


screen.exitonclick()