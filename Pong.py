from turtle import *
import turtle
import threading
import time

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2
static = True

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0 Player_2: 0", align="center", font=("Fixedsys", 24, "bold"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0,145)
pen2.write("Press enter to start", align="center", font=("Fixedsys", 24, "bold"))

def update_score(sa, sb):
    pen.clear()
    pen.write("Player 1: {} Player_2: {}".format(sa, sb), align="center", font=("Fixedsys", 24, "bold"))

def paddle_a_up():
    y = paddle_a.ycor()
    if y<=240:
        y+=20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y>=-220:
        y-=20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y<=240:
        y+=20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y>=-220:
        y-=20
        paddle_b.sety(y)

def play_sound():
    playsound(".mp3")

def init_play_sound():
    t = threading.Thread(target=play_sound)
    t.start()

def init_game():
    global static
    static = False
    pen2.clear()

def reset_screen():
    ball.goto(0, 0)
    ball.dx *=-1
    pen2.write("Press enter to start", align="center", font=("Fixedsys", 24, "bold"))
    paddle_a.goto(-350, 0)
    paddle_b.goto(350, 0)


wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(init_game, "Return")

while True:
    try:
        wn.update()
        #moveball
        if static==False:
            ball.setx(ball.xcor()+ball.dx)
            ball.sety(ball.ycor()+ball.dy)
            
        if ball.ycor()>290:
            ball.sety(290)
            ball.dy *= -1
            init_play_sound()
            
        if ball.ycor()<-290:
            ball.sety(-290)
            ball.dy *= -1
            init_play_sound()

        if ball.xcor()>390:
            score_a += 1
            update_score(score_a, score_b)
            static = True
            time.sleep(1)
            reset_screen()
        
        if ball.xcor()<-390:
            score_a += 1
            update_score(score_a, score_b)
            static = True
            time.sleep(1)
            reset_screen()

        if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50):
            ball.setx(340)
            ball.dx *= -1
            init_play_sound()
        
        if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50):
            ball.setx(-340)
            ball.dx *= -1
            init_play_sound()

    except:
        break