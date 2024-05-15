from turtle import Turtle, Screen

screen = Screen()


class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(cor)


    def up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)


    def down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)



