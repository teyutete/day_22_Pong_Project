from turtle import Turtle, Screen
class Paddle(Turtle):
    screen = Screen()
    screen.tracer(0)
    def __init__(self,position_tuple):
        super().__init__()
        self.position_tuple = position_tuple
        self.pu()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position_tuple)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)