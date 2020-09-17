import turtle
import time
import math




#chrome dinosaur by Doubtingeye352


#enemy come from right
#jumping player
#collusion detection
#graphics
# and a screen with the game




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



def Collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 20:
        return True
    else:
        return False


enemyspeed = 5
enemyspeed2 = 6





def jump():
    if player.state == "Ready":
        player.dy = 12
        player.state = "jumping"


Gravity = -0.8




wn.listen()
wn.onkeypress(jump, "space")




while True:
    wn.update()

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

    if Collision(player, enemy2):
        enemy2.hideturtle()
        enemy.hideturtle()
        player.hideturtle()
        pen.write("game over", font=("arial", 26, "normal"))






wn.mainloop()


