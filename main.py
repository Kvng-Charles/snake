
from turtle import Screen,Turtle 
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Welcome to my snake game.")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1) 
    snake.move()

    if snake.head.distance(food) < 16:
        food.refresh()
        score.addscore()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.xcor() > 280:
        score.reset()
        snake.reset()

    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()







