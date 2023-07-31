
from turtle import Turtle
# from snake

ALIGNMENT = "center"
FONT = ("Arial", 15,"normal")

class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        # self.highscore = 0
        with open(".\snake\data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        

    def addscore(self):
        self.score += 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} Highscore : {self.highscore}", align = ALIGNMENT, font= FONT)


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align = ALIGNMENT, font= FONT)

    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(".\snake\data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
