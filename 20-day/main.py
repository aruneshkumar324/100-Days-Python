from turtle import Screen
import time

from snake import Snake


screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
