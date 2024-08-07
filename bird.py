from turtle import Turtle

class Bird():

    def __init__(self):
        self.bird = Turtle(shape="circle")
        self.bird.color("yellow")
        self.bird.penup()
        self.bird.goto(-125,125)
        self.bird.right(90)

    def down(self):
        self.bird.forward(10)

    def up(self):
        self.bird.backward(100)












