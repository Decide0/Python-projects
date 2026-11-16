import turtle as t
from mysnake import Snake
import time
from food import Food
from scoreboard import Scoreboard
def game():
    myscreen = t.Screen()
    myscreen.setup(width=800, height=600)
    myscreen.title('Snake game')
    myscreen.bgcolor('black')
    myscreen.tracer(0)

    snake = Snake()
    food = Food()
    score = Scoreboard()

    myscreen.listen()
    myscreen.onkey(snake.up, 'Up')
    myscreen.onkey(snake.down, 'Down')
    myscreen.onkey(snake.right, 'Right')
    myscreen.onkey(snake.left, 'Left')

    flag = True
    while flag:
        time.sleep(0.1)
        myscreen.update()
        snake.move()
        if food.distance(snake.head) < 15:
            food.refresh()
            score.increase_score()
            snake.extend()
        
        if snake.head.xcor() > 380 or snake.head.xcor() <-380 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            score.game_over()
            flag = False
        
        for part in snake.snake_parts[1:]:
            if snake.head.distance(part) < 10:
                score.game_over()
                flag = False
        
        if len(snake.snake_parts) == 266:
            print('You win')
            flag = False
        
        if flag == False:
            answer = myscreen.textinput(title = 'Snake Game', prompt = 'Wanna play again?')
            if answer == 'yes':
                myscreen.clear()
                game()
game()