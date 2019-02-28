import turtle
import time
import random
import os

delay = 0.15 #snake speed
level = 1
record = 0

#create screen
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.penup()
head.goto(10,10)
head.shape("square")
head.direction = "stop"

#snake tail
tail = []

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(10,10)

txt = turtle.Turtle()


def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"
def go_stop():
    head.direction = "stop"

#key pad settings for directions
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_stop,"q")
wn.onkeypress(go_up,"W")
wn.onkeypress(go_down,"S")
wn.onkeypress(go_left,"A")
wn.onkeypress(go_right,"D")
wn.onkeypress(go_stop,"Q")
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")


def draw_border():
    brd = turtle.Turtle()
    brd.penup()
    brd.color("white")
    brd.goto(-285,265)
    #draw game border square
    brd.pendown()
    brd.forward(570)
    brd.right(90)
    brd.forward(530)
    brd.right(90)
    brd.forward(570)
    brd.right(90)
    brd.forward(560)
    #draw points square
    brd.right(90)
    brd.forward(570)
    brd.right(90)
    brd.forward(30)
    brd.hideturtle()

def move():

    for index in range(len(tail)-1, 0,-1):
        x = tail[index-1].xcor()
        y = tail[index-1].ycor()
        tail[index].goto(x,y)
    if len(tail) > 0:
        x = head.xcor()
        y = head.ycor()
        tail[0].goto(x,y)

    x = head.xcor()
    y = head.ycor()

    if head.direction == "up":
        head.sety(y + 20)
    if head.direction == "down":
        head.sety(y - 20)
    if head.direction == "left":
        head.setx(x - 20)
    if head.direction == "right":
        head.setx(x + 20)
        
def check_border():
    if head.xcor() >= 290:
        head.goto(-270,head.ycor())
    if head.xcor() <= -290:
        head.goto(270,head.ycor())
    if head.ycor() >= 270:
        head.goto(head.xcor(),-250)
    if head.ycor() <= -270:
        head.goto(head.xcor(),250)

def check_kill():
    global level, delay

    for body in tail:
        #snake eat his self
        if head.distance(body) < 20:
            for x in tail:
                x.hideturtle()

            tail.clear()
            head.goto(10,10)
            go_stop()
            level = 0
            update_text()
            delay = 0.15
            exit
        
def recreate_food():
    x = (random.randint(-14,14)*20)
    y = (random.randint(-13,13)*20)
    if x > 0:
        x -= 10
    else:
        x += 10
    
    if y > 0:
        y -= 10
    else:
        y += 10

    print(x)
    print(y)
    food.goto(x,y)

def grow_snake():
    global delay
    body = turtle.Turtle()
    body.speed(0)
    body.shape("square")
    body.color("gray")
    body.penup()
    tail.append(body)
    delay /= 1.01
    
def check_record():
    global record

    if record < level:
        record = level
        # Scrive un file.
        out_file = open("test.txt","w")
        out_file.write(str(record))
        out_file.close()

def get_record():
    global record
    # Legge un file.
    exists = os.path.isfile(os.path.dirname(os.path.abspath(__file__))+"/test.txt")
    if exists:
        # Store configuration file values
        in_file = open("test.txt","r")
        text = in_file.read()
        in_file.close()
        record = int(text)
    else:
        out_file = open("test.txt","w")
        out_file.write(str(record))
        out_file.close()

def update_text():
    global level,record
    txt.clear()
    txt.penup()
    txt.goto(-270,267)
    txt.pendown()
    txt.color("white")
    txt.write('Snakee!!', font = ('Times', 20, 'bold'))
    txt.penup()
    txt.goto(0,267)
    txt.pendown()
    txt.color("white")
    txt.write('Record '+str(record), font = ('Times', 20, 'bold'))
    txt.hideturtle()
    txt.penup()
    txt.goto(200,267)
    txt.pendown()
    txt.color("white")
    txt.write('Liv '+str(level), font = ('Times', 20, 'bold'))
    txt.hideturtle()

    if level == 0:
        wn.bgcolor("green")
        food.color("red")
    elif level == 20:
        wn.bgcolor("blue")
        food.color("yellow")
    elif level == 40:
        wn.bgcolor("orange")
        food.color("blue")
    elif level == 60:
        wn.bgcolor("red")
        food.color("white")
    elif level == 80:
        wn.bgcolor("azure")
        food.color("pink")
    elif level == 100:
        wn.bgcolor("pink")
        food.color("yellow")


get_record()
draw_border()
recreate_food()
update_text()

#MAIN
while True:
    wn.update()

    if head.distance(food) < 20:
        #food eaten
        check_record()
        level += 1
        recreate_food()
        grow_snake()
        grow_snake()
        update_text()

    move()
    check_kill()
    check_border()
    time.sleep(delay)

wn.mainloop()
