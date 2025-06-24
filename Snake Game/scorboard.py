from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.file = open("high_score.txt")
        self.highScore = self.file.read()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score} Highest score: {self.highScore}", align = "center", font = ("Arial", 15, "normal"))

    def updateScore(self):
        self.clear()
        self.write(f"Score: {self.score} Highest score: {self.highScore}", align = "center", font = ("Arial", 15, "normal"))

    def increaseScore(self):
        self.score += 1

    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over", align = "center", font = ("Arial", 30, "normal"))

    def reset(self):
        if self.score > int(self.highScore):
            self.highScore = self.score
            file = open("high_score.txt", mode = "w")
            file.write(str(self.highScore))
        self.score = 0
        self.updateScore()