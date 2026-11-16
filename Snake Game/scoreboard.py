from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = 0
        with open('./snake/highscore.txt') as data:
            self.high_score = int(data.read())
        self.update()

    def update(self):
        self.goto(0,270)
        self.write(f'Score: {self.score}  High score: {self.high_score}', align = 'center', font = ('Courier',20, 'normal'))
        

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
    
    def game_over(self):
        if self.high_score < self.score:
            with open('./snake/highscore.txt', mode = 'w') as data:
                data.write(str(self.score))
        self.goto(0,0)
        self.write('Game Over!', align = 'center', font =('Courier',20, 'normal'))
