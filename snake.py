from turtle import Turtle
import time

MOVE_DISTANCE = 20
POSITIONS = [(0,0), (-20,0), (-40,0), (-60,0), (-80,0)]

class Snake:
    def __init__(self):
        self.s = []
        self.create_snake()
    
    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)


    def add_segment(self,position):
        new_t = Turtle("square")
        new_t.color("white")
        new_t.penup()
        new_t.goto(position)
        self.s.append(new_t)

    def extend_snake(self):
        self.add_segment(self.s[-1].position())

    

    def move(self):
        for i in range(len(self.s)-1, 0, -1):
            self.s[i].goto(self.s[i-1].pos())   
        self.s[0].forward(MOVE_DISTANCE)
        time.sleep(0.1)



    def up(self):
        if(self.s[0].heading() != 270):
            self.s[0].setheading(90)

    def down(self):
        if(self.s[0].heading() != 90):
            self.s[0].setheading(270)

    def left(self):
        if(self.s[0].heading() != 0):
            self.s[0].setheading(180)

    def right(self):
        if(self.s[0].heading() != 180):
            self.s[0].setheading(0)

        
    

    
    
    
    

    