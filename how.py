import turtle


wn = turtle.Screen()
wn.title("How to play?")
wn.setup(2000,1000)
wn.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.goto(-450,0)
pen.color("black")
pen.write("the objective is to dodge the enemy for as long as possible  you can change colors of your player click r for changing to red in the main game and b for blue g for green d for defaunt ", font=("arial",12,"normal"))
pen.hideturtle()


pen2 = turtle.Turtle()
pen2.penup()
pen2.goto(-350,-100)
pen2.write("click left arrow key to go back!", font=("arial",12,"normal"))



def back():
    pen2.clear()
    pen2.hideturtle()
    pen.clear()
    import launcher


wn.listen()

wn.onkeypress(back, "Left")

while True:
    wn.update()


wn.mainnloop()