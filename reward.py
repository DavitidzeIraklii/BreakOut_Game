from turtle import Turtle
import random

colors = ['red', 'white', 'blue', 'yellow', 'green', 'purple', "light blue", "orange", "gold", "maroon", "violet", "magenta", "navy", "skyblue", "cyan", "turquoise", "lightgreen", "darkgreen", "chocolate", "brown"]

class Reward(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.setheading(random.randint(0, 270))
        self.color(random.choice(colors))
        self.goto(random.randint(-350, 350), random.randint(-380, 380))