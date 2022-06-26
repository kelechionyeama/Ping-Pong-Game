from turtle import Screen
from ball import Ball
from scoreboard import ScoreBoard
from dimensions import *
from paddle import Paddle
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=WIDTH, height=HEIGHT)
screen.title('Kelechi\'s Ping Pong')
scoreboard = ScoreBoard()
paddle_left = Paddle('left', screen)
paddle_right = Paddle('right', screen)
ball = Ball(paddle_left, paddle_right, scoreboard)

game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(ball.game_speed)
screen.exitonclick()
