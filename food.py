from turtle import Turtle
from random import randint
from border import Size

dimensions = Size()

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.xcor = randint(-dimensions.SCREEN_LENGTH/2,dimensions.SCREEN_LENGTH/2)
        self.ycor = randint(-dimensions.SCREEN_WIDTH/2,dimensions.SCREEN_WIDTH/2)

        
        
    def food_position_change(self):
        rand_x = randint(-dimensions.SCREEN_LENGTH/2,dimensions.SCREEN_LENGTH/2)
        rand_y = randint(-dimensions.SCREEN_WIDTH/2,dimensions.SCREEN_WIDTH/2)
        self.goto(rand_x, rand_y)

    
        


