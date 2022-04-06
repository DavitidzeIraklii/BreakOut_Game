from turtle import Screen, Turtle
from ball import Ball
from pad import Pad
from blocks import Block
from tables import Table
from reward import Reward
import time

screen = Screen()
screen.bgcolor('pink')
screen.setup(height=600, width=800)
screen.tracer(0)

ball = Ball()
pad = Pad((0, -250))
all_blocks = []

for n in range(68):
    block = Block()
    all_blocks.append(block)

block_x_cor = -358
block_y_cor = 0
for n in range(len(all_blocks)):
    all_blocks[n].goto(block_x_cor, block_y_cor)

    n_of_next_block = n + 1
    if n_of_next_block < len(all_blocks):
        block_x_cor += all_blocks[n].collision_x_dis + all_blocks[n_of_next_block].collision_x_dis - 15

    if all_blocks[n].xcor() > 300:
        block_x_cor = -358
        block_y_cor += 50


for block in all_blocks:
    if block.ycor() > 200:

        all_blocks.remove(block)
        block.hideturtle()

screen.listen()
screen.onkey(pad.go_left, "Left")
screen.onkey(pad.go_righr, "Right")

GAME = True

ball.reset_pos()

hited = 0
score = Table()
score.goto(180, 250)
score.write(f"Your score: {hited}", font=("Arial", 20, "bold"))

life = 5
lifes = Table()
lifes.goto(-350, 250)
lifes.write(f"Your lives: {life}", font=("Arial", 20, "bold"))

screen.update()
time.sleep(1)
while GAME:
    screen.update()
    ball.move()

    if ball.xcor() > 380 or ball.xcor() < -390:
        ball.bounce_x()
        
    if ball.ycor() > 290:
        ball.bounce_y()

    for block in all_blocks:
        # Collision of y-axis
        if abs(ball.ycor() - block.ycor()) < block.collission_y_dis and abs(ball.xcor() - block.xcor()) < 30:
            all_blocks.remove(block)
            ball.bounce_y()
            block.hideturtle()
            ball.color(block.color()[1])
            hited += 1
            score.clear()
            score.color(ball.color()[1])
            score.write(f"Your score: {hited}", font=("Arial", 20, "bold"))
            lifes.clear()
            lifes.color(ball.color()[1])
            lifes.write(f"Your lives: {life}", font=("Arial", 20, "bold"))

        # # Collision of x-axis
        elif abs(ball.xcor() - block.xcor()) < block.collision_x_dis and abs(ball.ycor() - block.ycor()) < 30:
            all_blocks.remove(block)
            ball.bounce_x()
            block.hideturtle()
            ball.color(block.color()[1])
            hited += 1
            score.clear()
            score.color(ball.color()[1])
            score.write(f"Your score: {hited}", font=("Arial", 20, "bold"))
            lifes.clear()
            lifes.color(ball.color()[1])
            lifes.write(f"Your lives: {life}", font=("Arial", 20, "bold"))

    # Adjusting an angle of ball
    if ball.xcor() - pad.xcor() < 50 and ball.xcor() - pad.xcor() > 0  and ball.ycor() < -230:
        ball.xmove = 3
        ball.bounce_y()
    elif ball.xcor() - pad.xcor() > -50 and ball.xcor() - pad.xcor() < 0  and ball.ycor() < -230:
        ball.xmove = -3
        ball.bounce_y()
    elif ball.xcor() - pad.xcor() < 80 and ball.xcor() - pad.xcor() > 0 and ball.ycor() < -230:
        ball.xmove = 6
        ball.bounce_y()
    elif ball.xcor() - pad.xcor() > -80 and ball.xcor() - pad.xcor() < 0 and ball.ycor() < -230:
        ball.xmove = -6
        ball.bounce_y()

    # Spend life
    if ball.ycor() < -280:
        ball.bounce_y()
        ball.reset_pos()
        pad.reset_position()
        life -= 1
        lifes.clear()
        lifes.write(f"Your lives: {life}", font=("Arial", 20, "bold"))
        screen.update()
        time.sleep(1)

    # Win
    if all_blocks == []:
        win = Table()
        win.goto(-220, -50)
        win.color(ball.color()[1])
        screen.update()
        time.sleep(1)
        win.write('You Win!', font=("Arial", 100, "bold"))
        for n in range(1000):
            reward = Reward()
            screen.update()
        GAME = False

    # Lose
    if life == 0:
        game_over = Table()
        game_over.goto(-250, -150)
        game_over.color(ball.color()[1])
        game_over.write('Game Over', font=("Arial", 100, "bold"))
        GAME = False

screen.exitonclick()