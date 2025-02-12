from turtle import*

def background():
    Screen().bgcolor("turquoise")

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




#Game execution
background()
turtle_model()
turtle_speed()
turtle_path()

#Keeps the window open
done()