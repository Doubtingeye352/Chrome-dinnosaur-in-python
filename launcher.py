import turtle



wn = turtle.Screen()
wn.title("chrome dinosaur launcher")
wn.setup(600,600)
wn.tracer(0)

pen = turtle.Turtle()
pen.penup()
pen.goto(-240,0)
pen.color("black")
pen.write("click r to start! or click h to go to how to play")
pen.hideturtle()

def howplay():
    pen.clear()
    import how

def gamestart():
    pen.clear()
    import main









wn.listen()
wn.onkeypress(gamestart, "r")
wn.onkeypress(howplay, "h")



while True:
    wn.update()


wn.mainloop()