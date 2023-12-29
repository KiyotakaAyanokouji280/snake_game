from turtle import Turtle
from snake import Snake

class KeyBoard:

    def __init__(self):
        self.turn_down()
        self.turn_left()
        self.turn_right()
        self.turn_up()

    def turn_down(self,snake_instance):
        snake_instance.s[0].setheading(270)

    def turn_left(self,snake_instance):
        snake_instance.s[0].setheading(180)

    def turn_right(self,snake_instance):
        snake_instance.s[0].setheading(0)

    def turn_up(self,snake_instance):
        snake_instance.s[0].setheading(90)