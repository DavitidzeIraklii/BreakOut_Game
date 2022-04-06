from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.xmove = 3
        self.ymove = 3
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.xmove
        y = self.ycor() + self.ymove
        self.goto(x, y)

    def bounce_x(self):
        self.xmove *= -1

    def bounce_y(self):
        self.ymove *= -1

    def reset_pos(self):
        self.goto(0, -230)
