from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)



snake = Snake()
food = Food()
score = Score() 

screen.listen()
screen.onkey(snake.goRight, 'Right')
screen.onkey(snake.goLeft, 'Left')
screen.onkey(snake.goDown, 'Down')
screen.onkey(snake.goUp, 'Up')


game_is_on = True
while game_is_on: 
    screen.update()
    time.sleep(0.09)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_new_segment()
        score.increaseScore()
        
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        score.gameOver()
    
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            game_is_on = False
            score.gameOver()
            
    if score.score > 5 :
        food.color('red')
    if score.score > 10 :
        food.color('green')


















screen.exitonclick()