from turtle import Turtle
from dimensions import HEIGHT


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.writeText(f"{self.left_score} : {self.right_score}")

    def writeText(self, to_write: str):
        self.reset()
        self.penup()
        self.goto((0, (HEIGHT/2)-60))
        self.color('white')
        self.hideturtle()
        style = ('Courier', 30, 'bold')
        self.write(to_write, font=style, align='center')

    def increaseScore(self, to_increase: str):
        if(to_increase == 'left'):
            self.left_score += 1
        elif(to_increase == 'right'):
            self.right_score += 1
        self.writeText(f"{self.left_score} : {self.right_score}")
