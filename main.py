from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")
screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")

run = True
while run:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_wall()

    if ball.distance(r_paddle) < 55 and ball.xcor() > 320 and ball.x_move > 0:
        ball.bounce_paddle()

    if ball.distance(l_paddle) < 55 and ball.xcor() < -330 and ball.x_move < 0:
        ball.bounce_paddle()

    if ball.xcor() > 380:
        ball.home()
        ball.move_speed = 0.04
        scoreboard.l_score += 1
        ball.x_move *= -1
        scoreboard.update()

    if ball.xcor() < -380:
        ball.home()
        ball.move_speed = 0.04
        scoreboard.r_score += 1
        ball.x_move *= -1
        scoreboard.update()


screen.exitonclick()
