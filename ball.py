from turtle import Turtle
from scoreboard import ScoreBoard
from dimensions import WIDTH, HEIGHT


class Ball(Turtle):
    def __init__(self, paddle_left: Turtle, paddle_right: Turtle, scoreboard: ScoreBoard):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.direction_vertical = 'up'
        self.direction_horizontal = 'right'
        self.paddle_left = paddle_left
        self.paddle_right = paddle_right
        self.scoreboard = scoreboard
        self.game_speed = 0.1

    def move(self):
        new_x = self.xcor() + (10 if self.direction_horizontal == 'right' else -10)
        new_y = self.ycor() + (10 if self.direction_vertical == 'up' else -10)

        if self.direction_vertical == 'up' and (HEIGHT/2) - self.ycor() <= 20:
            self.direction_vertical = 'down'
            new_y = self.ycor()-10
        if self.direction_vertical == 'down' and (HEIGHT/2) - (-self.ycor()) <= 20:
            self.direction_vertical = 'up'
            new_y = self.ycor()+10

        if self.direction_horizontal == 'right' and \
            (WIDTH/2) - new_x <= 50 and\
                self.distance(self.paddle_right) < 60:
            self.game_speed *= 0.9
            self.direction_horizontal = 'left'
            new_x = self.xcor()-10
        if self.direction_horizontal == 'left' and \
            (WIDTH/2) - abs(new_x) <= 50 and\
                self.distance(self.paddle_left) < 60:
            self.game_speed *= 0.9
            self.direction_horizontal = 'right'
            new_x = self.xcor()+10

        if self.direction_horizontal == 'right' and (WIDTH/2)-self.xcor() < 0:
            self.scoreboard.increaseScore('left')
            self.resetBall()
            return
        if self.direction_horizontal == 'left' and (WIDTH/2)-abs(self.xcor()) < 0:
            self.scoreboard.increaseScore('right')
            self.resetBall()
            return

        self.goto((new_x, new_y))

    def resetBall(self):
        self.direction_horizontal = 'right' if self.direction_horizontal == 'left' else 'left'
        self.direction_vertical = 'up' if self.direction_horizontal == 'down' else 'down'
        self.game_speed = 0.1
        self.goto((0, 0))
