from turtle import Turtle
ALIGN = "center"
FONT =("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.setx(0)
        self.sety(200)
        self.score_aquired = 0
        self.write(f"Score: {self.score_aquired}", False, align = ALIGN, font = FONT)
        
    def increment_score(self):
        self.clear()
        self.write(f"Score: {self.score_aquired}", False, align = ALIGN, font = FONT)
        self.score_aquired+=1

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER!", False, align = ALIGN, font = FONT)

        