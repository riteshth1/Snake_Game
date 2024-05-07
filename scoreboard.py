from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("Game Over", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
