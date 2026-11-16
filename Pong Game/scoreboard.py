from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.update()

    
    def update(self):
        self.clear()
        self.goto(0,270)
        self.write(f'{self.r_score} {self.l_score}', align = 'center', font = ('Courier', 20, 'normal'))
    
    def win_l(self):
        self.l_score += 1
        self.update()

    
    def win_r(self):
        self.r_score += 1
        self.update()

