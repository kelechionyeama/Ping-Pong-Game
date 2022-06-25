from turtle import Turtle, _Screen
from dimensions import WIDTH


class Paddle(Turtle):
    def __init__(self, position, screen: _Screen):
        super().__init__()
        screen.tracer(0)
        self.shape('square')
        self.color('white')
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(((WIDTH/2)-50, 0) if position ==
                  'right' else (-((WIDTH/2)-50), 0))
        self.screen = screen
        self.position_on_screen = position
        self.initalizeListeners()

    def go_up(self):
        self.goto((self.xcor(), self.ycor()+20))

    def go_down(self):
        self.goto((self.xcor(), self.ycor()-20))

    def initalizeListeners(self):
        self.screen.listen()
        if(self.position_on_screen == 'right'):
            self.screen.onkey(self.go_up, "Up")
            self.screen.onkey(self.go_down, "Down")
        elif self.position_on_screen == 'left':
            self.screen.onkey(self.go_up, "w")
            self.screen.onkey(self.go_down, "s")
