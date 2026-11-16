import turtle as t
import time
from player import Player
from ball import Ball
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width = 800, height= 600)
screen.title('Pong Game')
screen.bgcolor('black')
screen.tracer(0)


r_player = Player((350,0))
l_player = Player((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_player.up, 'Up')
screen.onkey(r_player.down, 'Down')

screen.onkey(l_player.up, 'w')
screen.onkey(l_player.down, 's')
screen.onkey(ball.pause, 'p')


flag = True
while flag:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #the wall
    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.bounce_y()

    #touch to player
    if (ball.distance(r_player) < 50 and ball.xcor() > 320 ) or (ball.distance(l_player) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    
    #score for the left side
    if ball.xcor() > 350:
        scoreboard.win_l()
        ball.reset()
        
    #score for the right side
    if ball.xcor() < -350:
        scoreboard.win_r()
        ball.reset()

screen.update()
screen.exitonclick()