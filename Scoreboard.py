from turtle import Turtle
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.write(f"Score ={self.score}", False, align=ALIGNMENT, )
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score ={self.score}", False, align=ALIGNMENT, )
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT)