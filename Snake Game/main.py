from turtle import Screen
import time
from snake import Snake
from food import Food
from scorboard import ScoreBoard

def screenSetup():
    screen.setup(width = 600, height = 600)
    screen.bgcolor("black")
    screen.title("Snake Game")

screen = Screen()
screen.tracer(0)

def moveSnake():
    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.moveSnake()
        eatFood()
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
           scoreboard.reset()
           snake.reset()
        for segment in snake.snake_segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()


def eatFood():
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increaseScore()
        scoreboard.updateScore()
        snake.extend()

screenSetup()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(key = "Up", fun = snake.snakeUp)
screen.onkey(key = "Down", fun = snake.snakeDown)
screen.onkey(key = "Left", fun = snake.snakeLeft)
screen.onkey(key = "Right", fun = snake.snakeRight)
screen.update()
moveSnake()
screen.exitonclick()