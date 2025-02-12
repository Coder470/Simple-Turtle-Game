from turtle import*

def turtle_model():
    color("blue")
    shape("turtle")
    pensize(4)

def turtle_speed():
    speed(1)

def turtle_path():
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)

def background():
    Screen().bgcolor("turquoise")


#Game execution
turtle_model()
turtle_speed()
turtle_path()
background()

#Keeps the window open
done()