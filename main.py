from turtle import Turtle, Screen
from Paddle import Paddle
from Ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

rp = Paddle((350, 0))
lp = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.tracer(0)
screen.onkeypress(rp.go_up, 'Up')
screen.onkeypress(rp.go_down, 'Down')
screen.onkeypress(lp.go_up, 'w')
screen.onkeypress(lp.go_down, 's')



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#detection with the top wall layers
    if ball.ycor() > 280 or ball.ycor() < -280:
         ball.y_bounce() # only changes the y direction
    #check collision with right paddle
    if ball.distance(rp) < 50 and ball.xcor() > 320 or ball.distance(lp) < 50 and ball.xcor() < -320:
        ball.x_bounce()
        time.sleep(ball.move_speed)
    #Detect when a paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
