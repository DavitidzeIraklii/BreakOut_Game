from turtle import Turtle
import random
colors = ['red', 'white', 'blue', 'yellow', 'green', 'purple', "light blue", "orange", "gold", "maroon", "violet", "magenta", "navy", "skyblue", "cyan", "turquoise", "lightgreen", "darkgreen", "chocolate", "brown"]
class Pad(Turtle):

    def __init__(self, position):
        super().__init__()

        self.color(random.choice(colors))
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.goto(position)

    def go_left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())

    def go_righr(self):
        self.goto(self.xcor() + 30, self.ycor())

    def reset_position(self):
        self.goto(0, -250)
