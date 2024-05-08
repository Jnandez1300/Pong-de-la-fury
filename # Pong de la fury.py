# Pong de la fury
# By Julian Hernandez

import turtle
import time
import tkinter as tk
from tkinter import simpledialog

# Function to create explosion effect
def explode(x, y):
    explosion = turtle.Turtle()
    explosion.shape("circle")
    explosion.color("orange")
    explosion.shapesize(3)
    explosion.penup()
    explosion.goto(x, y)
    for _ in range(5):
        explosion.stamp()
        time.sleep(0.1)
        explosion.hideturtle()

# Function to show user system pop-up with game instructions
def show_user_popup():
    root = tk.Tk()
    root.withdraw()
    
    instructions = """Controls:
    - Player A (Left Side):
      - Move Up: Press the "W" key
      - Move Down: Press the "S" key
    - Player B (Right Side):
      - Move Up: Press the up arrow key
      - Move Down: Press the down arrow key
    
    Gameplay:
    - The game starts automatically once you run the code.
    - Each player controls a paddle, with Player A on the left and Player B on the right.
    - Use your paddle to hit the ball back and forth.
    - If the ball passes your opponent's paddle and goes off-screen behind them, you score a point.
    - The first player to reach the set number of points wins.
    
    Scoring:
    - The score is displayed at the top center of the screen.
    - Player A's score is on the left, and Player B's score is on the right.
    
    Game Over:
    - The game continues until you exit the program.
    - You can exit the game window to end the program.
    
    Tips:
    - Try to anticipate the ball's movement to position your paddle for the best chance of hitting it.
    - Keep an eye on your opponent's paddle to react quickly and defend against their shots.
    - Practice timing and precision to control the ball and outmaneuver your opponent.
    
    Enjoy the game!"""
    
    simpledialog.messagebox.showinfo("Instructions", instructions)

# Set up the screen
wn = turtle.Screen()
wn.title("Pong de la Fury")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Call the function to show the user system pop-up with game instructions
show_user_popup()

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function to move paddle A up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# Function to move paddle A down
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# Function to move paddle B up
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# Function to move paddle B down
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        explode(0, 0)  # Create explosion effect

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        explode(0, 0)  # Create explosion effect

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        explode(340, ball.ycor())  # Create explosion effect at paddle position

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        explode(-340, ball.ycor())  # Create explosion effect at paddle position

