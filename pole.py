from turtle import Turtle
import random

class Pole():

    def __init__(self):
        self.segments1 = []
        self.segments2 = []
        self.segments3 = []
        self.add_segment1()
        self.add_segment2()
        self.add_segment3()


    def add_segment1(self):
        n = random.randint(5, 15)
        pos1 = 150
        pos2 = 240
        for j in range(3):
            for i in range(n):
                new_segment = Turtle(shape="square")
                new_segment.right(180)
                new_segment.color("green")
                new_segment.penup()
                new_segment.goto(pos1, pos2)
                self.segments1.append(new_segment)
                pos2 -= 20
            pos2 = 240
            pos1 += 20
        pos1 = 150
        pos2 = -240
        for j in range(3):
            for i in range(25-n-7):
                new_segment = Turtle(shape="square")
                new_segment.right(180)
                new_segment.color("green")
                new_segment.penup()
                new_segment.goto(pos1, pos2)
                self.segments1.append(new_segment)
                pos2 += 20
            pos2 = -240
            pos1 += 20

    def add_segment2(self):
        n = random.randint(5, 15)
        pos1 = 320
        pos2 = 240
        for j in range(3):
            for i in range(n):
                new_segment = Turtle(shape="square")
                new_segment.right(180)
                new_segment.color("green")
                new_segment.penup()
                new_segment.goto(pos1, pos2)
                self.segments2.append(new_segment)
                pos2 -= 20
            pos2 = 240
            pos1 += 20
        pos1 = 320
        pos2 = -240
        for j in range(3):
            for i in range(25 - n - 7):
                new_segment = Turtle(shape="square")
                new_segment.right(180)
                new_segment.color("green")
                new_segment.penup()
                new_segment.goto(pos1, pos2)
                self.segments2.append(new_segment)
                pos2 += 20
            pos2 = -240
            pos1 += 20

    def add_segment3(self):
        n = random.randint(5, 15)
        pos1 = 490
        pos2 = 240
        for j in range(3):
            for i in range(n):
                new_segment = Turtle(shape="square")
                new_segment.right(180)
                new_segment.color("green")
                new_segment.penup()
                new_segment.goto(pos1, pos2)
                self.segments3.append(new_segment)
                pos2 -= 20
            pos2 = 240
            pos1 += 20
        pos1 = 490
        pos2 = -240
        for j in range(3):
            for i in range(25 - n - 7):
                new_segment = Turtle(shape="square")
                new_segment.right(180)
                new_segment.color("green")
                new_segment.penup()
                new_segment.goto(pos1, pos2)
                self.segments3.append(new_segment)
                pos2 += 20
            pos2 = -240
            pos1 += 20

    def forw(self):
            for segment in self.segments1:
                segment.forward(4)
            for segment in self.segments2:
                segment.forward(4)
            for segment in self.segments3:
                segment.forward(4)

    def pole_end(self):
        if self.segments1[0].xcor() < -290:
            for segment in self.segments1:

                segment.backward(500)
            for segment in self.segments1:
                segment.isvisible()

        if self.segments2[0].xcor() < -290:
            for segment in self.segments2:

                segment.backward(500)
            for segment in self.segments2:
                segment.isvisible()

        if self.segments3[0].xcor() < -290:
            for segment in self.segments3:

                segment.backward(500)
            for segment in self.segments3:
                segment.isvisible()
