from turtle import Turtle
class Size:
    def __init__(self):
        self.SCREEN_LENGTH = 512
        self.SCREEN_WIDTH = 512

class Border:
    def __init__(self):
        self.SCREEN_LENGTH = 512
        self.SCREEN_WIDTH = 512
        border = Turtle()
        border.color("white")
        border.penup()
        border.goto(-self.SCREEN_LENGTH/2,-self.SCREEN_WIDTH/2)
        border.pendown()
        border.forward(self.SCREEN_WIDTH)
        border.setheading(90)
        border.forward(self.SCREEN_LENGTH)
        border.setheading(180)
        border.forward(self.SCREEN_WIDTH)
        border.setheading(270)
        border.forward(self.SCREEN_LENGTH)
        border.penup()
        border.hideturtle()
            