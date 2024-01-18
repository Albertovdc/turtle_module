import random
import turtle
luis = turtle.Turtle()
turtle.colormode(255)
def random_color():
  r = random.randint(0,255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)

directions = [0, 90, 180, 270]
luis.pensize(10)
speed_turtle = 10
for _ in range(1000):
  luis.speed(speed_turtle)
  luis.color(random_color())
  luis.forward(25)
  luis.right(random.choice(directions))


