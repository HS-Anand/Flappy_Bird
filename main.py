from turtle import Screen
from score import Scoreboard
from bird import Bird
from pole import Pole
import time

screen = Screen()
screen.bgcolor("cyan")
screen.setup(500, 500)
screen.title("Flappy Bird")
screen.tracer(0)
screen.listen()


pole = Pole()
flappy = Bird()
scoreboard = Scoreboard()
head = flappy.bird

screen.onkey(flappy.up,"space")

game = True
flag1 = 1
flag2 = 1
flag3 = 1
f = 0

while game:
    screen.update()
    time.sleep(0.06)
    flappy.down()
    pole.forw()

    if head.ycor() > 240 or head.ycor() < -240:
        f = 1

    pole.pole_end()

    for segment in pole.segments1:
        if head.distance(segment) < 20:
            f = 1
    for segment in pole.segments2:
        if head.distance(segment) < 20:
            f = 1
    for segment in pole.segments3:
        if head.distance(segment) < 20:
            f = 1
    if f == 1:
        game = False
        scoreboard.game_over()
        for segment in pole.segments1:
            segment.hideturtle()
        for segment in pole.segments2:
            segment.hideturtle()
        for segment in pole.segments3:
            segment.hideturtle()
        flappy.bird.hideturtle()
        screen.update()
        break;

    if head.xcor() > (pole.segments1[0].xcor() + 50) and flag1 == 1:
        scoreboard.increase_score()
        flag1 = 0
        flag2 = 1
    if head.xcor() > (pole.segments2[0].xcor() + 50) and flag2 == 1:
        scoreboard.increase_score()
        flag2 = 0
        flag3 = 1
    if head.xcor() > (pole.segments3[0].xcor() + 50) and flag3 == 1:
        scoreboard.increase_score()
        flag3 = 0
        flag1 = 1

screen.exitonclick()
