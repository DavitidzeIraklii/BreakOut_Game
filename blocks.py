from turtle import Turtle
import random

colors = ['red', 'white', 'blue', 'yellow', 'green', 'purple', "light blue", "orange", "gold", "maroon", "violet", "magenta", "navy", "skyblue", "cyan", "turquoise", "lightgreen", "darkgreen", "chocolate", "brown"]

stretch_len = [2, 2.5, 3]
class Block(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color(random.choice(colors))
        self.width = random.choice(stretch_len)
        self.shapesize(stretch_wid=2, stretch_len=self.width)
        self.collision_x_dis = self.width * 10 + 10
        self.collission_y_dis = 30
        self.all_blocks = []


