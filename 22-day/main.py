from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


# SCREEN SETUP
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

# PADDLE SETUP
l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))


screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


# BALL
ball = Ball()

# SCOREBOARD
scoreboard = ScoreBoard()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # BALL BOUNCE
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # PADDLE BALL BOUNCE
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.x_bounce()

    # DETECT R PADDLE MISSES
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # DETECT L PADDLE MISSES
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


#   EXIT
screen.exitonclick()
