from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def draw_dashed_line():
    line_drawer = Turtle()
    line_drawer.color("white")
    line_drawer.penup()
    line_drawer.goto(0, -300)
    line_drawer.setheading(90)

    for _ in range(15):  # Adjust the range and dash size as needed
        line_drawer.pendown()
        line_drawer.forward(20)  # Length of each dash
        line_drawer.penup()
        line_drawer.forward(20)  # Length of each gap
    line_drawer.hideturtle()


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

draw_dashed_line()

game_is_on = True
while game_is_on:
    # time.sleep(0.1)
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with ball up&down walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect if r_paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect if l_paddle misses ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
