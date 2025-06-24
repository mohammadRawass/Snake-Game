from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
class Snake:
    def __init__(self):
        self.snake_segments = []
        self.createSnake()
        self.head = self.snake_segments[0]

    def createSnake(self):
        for position in STARTING_POSITION:
            self.addSegment(position)

    def moveSnake(self):
         for segNum in range(len(self.snake_segments) - 1, 0, -1):
                    new_x = self.snake_segments[segNum - 1].xcor()
                    new_y = self.snake_segments[segNum - 1].ycor()
                    self.snake_segments[segNum].goto(new_x, new_y)
         self.head.forward(DISTANCE)

    def reset(self):
        for segment in self.snake_segments:
            segment.goto(1000,1000)
        self.snake_segments.clear()
        self.createSnake()
        self.head = self.snake_segments[0]

    def addSegment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.setposition(position)
        self.snake_segments.append(snake)

    def extend(self):
        self.addSegment(self.snake_segments[-1].position())

    def snakeUp(self):
        if self.head.heading() == 270:
            self.head.setheading(270)
        else:
            self.head.setheading(90)

    def snakeDown(self):
        if self.head.heading() == 90:
            self.head.setheading(90)
        else:
            self.head.setheading(270)

    def snakeRight(self):
        if self.head.heading() == 180:
            self.head.setheading(180)
        else:
            self.head.setheading(0)

    def snakeLeft(self):
        if self.head.heading() == 0:
            self.head.setheading(0)
        else:
            self.head.setheading(180)
