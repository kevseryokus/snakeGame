import random
import turtle
import time
delay = 0.15

window = turtle.Screen()
window.title('Yılan Oyunu')
window.bgcolor('lightgreen')
window.setup(width=600, height=600)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"

eat = turtle.Turtle()
eat.speed(0)
eat.shape("circle")
eat.color("red")
eat.penup()
eat.shapesize(0.80, 0.80)
eat.goto(0, 0)

tails = []
point = 0

write = turtle.Turtle()
write.speed(0)
write.shape("square")
write.color("white")
write.penup()
write.hideturtle()
write.goto(0, 260)
write.write("Puan: {}".format(point), align="center", font=("Courier", 24, "normal"))

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"





def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"

window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_right, "Right")
window.onkey(go_left, "Left")

while True:
    window.update()

    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for tail in tails:
            tail.goto(1000, 1000)
        tails = []

        point = 0
        delay = 0.1

        write.clear()
        write.write("Puan: {}".format(point), align="center", font=("Courier", 24, "normal"))

    if head.distance(eat) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        eat.goto(x, y)

        new_tails = turtle.Turtle()
        new_tails.speed(0)
        new_tails.shape("square")
        new_tails.color("white")
        new_tails.penup()
        tails.append(new_tails)

        delay -= 0.001

        point = point + 10
        write.clear()
        write.write("Puan: {}".format(point), align="center", font=("Courier", 24, "normal"))

    for index in range(len(tails) - 1, 0, -1):
        x = tails[index - 1].xcor()
        y = tails[index - 1].ycor()
        tails[index].goto(x, y)

    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x, y)

    move()

    for segment in tails:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in tails:
                segment.goto(1000, 1000)
            tails = []
            point = 0
            write.clear()
            write.write('Puan: {}'.format(point), align='center', font=('Courier', 24, 'normal'))
            speed = 0.15

    time.sleep(delay)