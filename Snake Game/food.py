import random
from turtle import Turtle
from random import Random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randomX = random.randint(-280, 280)
        randomY = random.randint(-280, 280)
        self.goto(randomX, randomY)

    def clearFood(self):
        self.hideturtle()


