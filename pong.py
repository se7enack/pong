#!/usr/bin/env python3

import turtle as t
from playsound import playsound
import time

endgame=5

class player():
    def __init__(self, name, score):
        self.name = name
        self.score = score

def gameon():
    t.resetscreen()

    screen = t.Screen()
    screen.title("Pong")
    screen.bgcolor('black')
    screen.setup(width=800,height=600)
    screen.tracer(0)

    p1name = t.textinput(prompt="Player1, Please enter your name: ",title="Player1")
    p2name = t.textinput(prompt="Player2, Please enter your name: ",title="Player2")

    p1 = player(p1name, 0)
    p2 = player(p2name, 0)

    time.sleep(1)

    player1 = t.Turtle()
    player1.speed(3)
    player1.shape('square')
    player1.color('orange')
    player1.shapesize(stretch_wid=5,stretch_len=1)
    player1.penup()
    player1.goto(-350,0)

    player2 = t.Turtle()
    player2.speed(3)
    player2.shape('square')
    player2.shapesize(stretch_wid=5,stretch_len=1)
    player2.color('blue')
    player2.penup()
    player2.goto(350,0)

    puck = t.Turtle()
    puck.speed(0)
    puck.shape('circle')
    puck.color('white')
    puck.penup()
    puck.goto(0,0)
    speed = .4
    puck_x = speed
    puck_y = speed

    scoreboard = t.Turtle()
    scoreboard.speed(0)
    scoreboard.color('white')
    scoreboard.penup()
    scoreboard.hideturtle()
    scoreboard.goto(0,260)
    scoreboard.write(p1.name + " {}   ".format(p1.score) + p2.name + " {}".format(p2.score),align="center",font=("Helvetica",26,"normal"))

    def player1_up():
        y = player1.ycor()
        y = y + 30
        player1.sety(y)

    def player1_down():
        y = player1.ycor()
        y = y - 30
        player1.sety(y)

    def player2_up():
        y = player2.ycor()
        y = y + 30
        player2.sety(y)

    def player2_down():
        y = player2.ycor()
        y = y - 30
        player2.sety(y)

    screen.listen()
    screen.onkeypress(player1_up,"w")
    screen.onkeypress(player1_down,"s")
    screen.onkeypress(player2_up,"Up")
    screen.onkeypress(player2_down,"Down")

    print("#####################################")

    while not p1.score >= endgame or p2.score >= endgame:
        screen.update()
        puck.setx(puck.xcor() + puck_x)
        puck.sety(puck.ycor() + puck_y)

        if puck.ycor() > 290:
            puck.sety(290)
            puck_y = puck_y * -1

        if puck.ycor() < -290:
            puck.sety(-290)
            puck_y = puck_y * -1

        if puck.xcor() > 390:
            puck.goto(0,0)
            puck_x = puck_x * -1
            p1.score = p1.score + 1
            scoreboard.clear()
            scoreboard.write(p1.name + " {}   ".format(p1.score) + p2.name + " {}".format(p2.score),align="center",font=('Helvetica',26,"normal"))
            print("# Player1:",p1.score,"| Player2:",p2.score,"| Goal:",endgame,"#")
            if p1.score >= endgame:
                break        
            
        if puck.xcor() < -390:
            puck.goto(0,0)
            puck_x = puck_x * -1
            p2.score = p2.score + 1
            scoreboard.clear()
            scoreboard.write(p1.name + " {}   ".format(p1.score) + p2.name + " {}".format(p2.score),align="center",font=('Helvetica',26,"normal"))
            print("# Player1:",p1.score,"| Player2:",p2.score,"| Goal:",endgame,"#")
            if p2.score >= endgame:
                break
        if (puck.xcor() > 340) and (puck.xcor() < 350) and (puck.ycor() < player2.ycor() + 40 and puck.ycor() > player2.ycor() - 40):
            puck.setx(340)
            puck_x = puck_x * -1

        if (puck.xcor() < -340) and (puck.xcor() > -350) and (puck.ycor() < player1.ycor() + 40 and puck.ycor() > player1.ycor() - 40):
            puck.setx(-340)
            puck_x = puck_x * -1
            
        if player1.ycor() > 250:
            player1.sety(250)
                
        if player1.ycor() < -250:
            player1.sety(-250)
            
        if player2.ycor() > 250:
            player2.sety(250)
            
        if player2.ycor() < -250:
            player2.sety(-250)

    print("#####################################")

    if p1.score > p2.score:
        print(p1.name, "wins!") 
    else:
        print(p2.name, "wins!")
                
    scoreboard.clear()
    scoreboard.write(p1.name + " {}   ".format(p1.score) + p2.name + " {}".format(p2.score),align="center",font=("Helvetica",26,"normal"))
    screen.title("GAME OVER")
    screen.bgcolor('red')
    playsound('end.wav')
    time.sleep(2)
    gameon()

gameon()
