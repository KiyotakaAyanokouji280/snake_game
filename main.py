from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from border import Border, Size

dimensions_a = Size()

scr = Screen()
# scr.screensize(dimensions_a.SCREEN_LENGTH, dimensions_a.SCREEN_WIDTH)
scr.setup(dimensions_a.SCREEN_LENGTH, dimensions_a.SCREEN_WIDTH)
scr.bgcolor('black')
scr.title("My Snake Game")
scr.bgpic("bg.gif")
scr.tracer(0)


my_snake = Snake()
food_piece = Food()
score = ScoreBoard()
game_border = Border()


game_on = True
while(game_on):
    scr.listen()
    scr.onkey(my_snake.up, "Up")
    scr.onkey(my_snake.down, "Down")
    scr.onkey(my_snake.left, "Left")
    scr.onkey(my_snake.right, "Right")

    my_snake.move()

    if my_snake.s[0].distance(food_piece) < 15:
        food_piece.food_position_change()
        score.increment_score()
        my_snake.extend_snake()
    

    if (my_snake.s[0].xcor() > game_border.SCREEN_LENGTH/2 or my_snake.s[0].xcor() < -game_border.SCREEN_LENGTH/2 or my_snake.s[0].ycor() > game_border.SCREEN_WIDTH/2 or my_snake.s[0].ycor() < -game_border.SCREEN_WIDTH/2):
        game_on = False
        score.gameover()

    for segment in my_snake.s[1:]:
            if my_snake.s[0].distance(segment) < 6:
                game_on = False
                score.gameover()

    scr.update()

    
    
    
    
   
    
    
        
        
        

        
        
    



scr.exitonclick()