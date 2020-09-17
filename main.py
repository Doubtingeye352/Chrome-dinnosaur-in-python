import turtle
import time
import math
import random




#chrome dinosaur by Doubtingeye352


#enemy come from right
#jumping player
#collusion detection
#graphics
# and a screen with the game


score = 0

wn = turtle.Screen()
wn.title("chrome dino")
wn.setup(1000,1000)
wn.tracer(0)


Gnd = -232

pen = turtle.Turtle()
pen.penup()
pen.goto(-220, 0)
pen.color("black")
pen.write("Loading....", font=("Roboto", 10, "normal"))
time.sleep(5)
pen.clear()
pen.hideturtle()

powerup = 0



pen2 = turtle.Turtle()
pen2.penup()
pen2.goto(250,300)
pen2.hideturtle()

player = turtle.Turtle()
player.shape("square")
player.color("black")
player.penup()
player.width = 20
player.height = 20
player.dy = 0
player.dx = 0
player.state = "ready"
player.goto(-340, Gnd + player.height / 2)

enemy = turtle.Turtle()
enemy.shape("circle")
enemy.color("red")
enemy.penup()
enemy.goto(340, -225)

enemy2 = turtle.Turtle()
enemy2.shape("circle")
enemy2.color("red")
enemy2.penup()
enemy2.goto(320, -225)

ground = turtle.Turtle()
ground.penup()
ground.goto(-340,-236)
ground.shape("square")
ground.setheading(90)
ground.shapesize(stretch_wid= 100, stretch_len=0.1)


food = turtle.Turtle()
food.shape("circle")
food.color("green")
food.penup()
x = random.randint(-200, 200)
food.goto(x,-225)

def Collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 20:
        return True
    else:
        return False





enemyspeed = 10
enemyspeed2 = 8





def jump():
    if player.state == "Ready":
        player.dy = 14
        player.state = "jumping"


Gravity = -0.8




wn.listen()
wn.onkeypress(jump, "space")
foodspeed = 10



while True:
    wn.update()



    pen2.clear()
    pen2.write(score, font=("arial",26,"normal"))







    # Gravity
    player.dy += Gravity

    # Move the jumper
    y = player.ycor()
    y += player.dy
    player.sety(y)

    # Deal with the ground
    if player.ycor() < Gnd + player.height / 2:
        player.sety(Gnd + player.height / 2)
        player.dy = 0
        player.state = "Ready"

    x = enemy.xcor()
    x = x - enemyspeed
    if x < -400:
        x = 345



    enemy.setx(x)

    x = enemy2.xcor()
    x = x - enemyspeed2
    if x < -400:
        x = 345



    enemy2.setx(x)


    if Collision(player, enemy):
        enemy.hideturtle()
        player.hideturtle()
        enemy2.hideturtle()
        pen.write("game over", font=("arial", 26, "normal"))
        pen2.goto(1000,1000)
        food.hideturtle()



    if Collision(player, enemy2):
        enemy2.hideturtle()
        enemy.hideturtle()
        player.hideturtle()
        pen.write("game over", font=("arial", 26, "normal"))
        pen2.goto(1000,1000)
        food.hideturtle()

    x = food.xcor()
    x = x - foodspeed
    if x < -400:
        x = random.randint(-200, 400)
        food.setposition(x,-225)

    food.setx(x)



    if Collision(player, food):
        food.hideturtle()
        score += 10
        x = random.randint(-200, 400)
        food.setposition(x, -225)
        food.showturtle()











wn.mainloop()

