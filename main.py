import turtle
import random
my_turtle = turtle.Turtle()
screen = turtle.Screen()

#my_turtle.shape("turtle")
#my_turtle.color("lime")

# Draw a Dashed line
# for _ in range(10):
#   my_turtle.forward(10)
#   my_turtle.penup()
#   my_turtle.forward(10)
#   my_turtle.pendown()

# colors = ["red", "orange", "yellow", "green", "pink", "blue", "violet", "black", "blueviolet"]
# for n in range(1,9):
#   my_turtle.color(colors[n])
#   for _ in range(n + 2):
#     sides = n+2
#     print(sides)
#     my_turtle.forward(100)
#     my_turtle.right(360/sides)

colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "brown", "gray", "black", "cyan",
          "magenta", "lime", "olive", "maroon", "navy", "teal", "silver", "gold"]
directions = [0, 90, 180, 270]
my_turtle.pensize(10)
speed_turtle = 1
for _ in range(1000):
  my_turtle.speed(speed_turtle)
  my_turtle.color(random.choice(colors))
  my_turtle.forward(25)
  my_turtle.right(random.choice(directions))
  speed_turtle += 1





screen.exitonclick()
