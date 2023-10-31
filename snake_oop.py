import turtle
import time
import random

delay = 0.1
level = 1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
class SnakeHead(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("black")
        self.penup()
        self.goto(0, 0)
        self.direction = "stop"

    def move(self):
        if self.direction == "up":
            y = self.ycor()
            self.sety(y + 20)
        if self.direction == "down":
            y = self.ycor()
            self.sety(y - 20)
        if self.direction == "left":
            x = self.xcor()
            self.setx(x - 20)
        if self.direction == "right":
            x = self.xcor()
            self.setx(x + 20)

head = SnakeHead()  # Create an instance of SnakeHead

# Create a list to store snake segments
segments = []

# Snake food
class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(0, 100)

food = Food()  # Create an instance of Food

# Pen
class ScorePen(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)

    def update_score(self):
        self.clear()
        self.write("Score: {}  High Score: {}  Level: {}".format(
            score, high_score, level),
            align="center",
            font=("Courier", 16, "normal"))

pen = ScorePen()  # Create an instance of ScorePen

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Create a function to add a new snake segment
def add_segment():
    segment = turtle.Turtle()
    segment.speed(0)
    segment.shape("circle")
    segment.color("green")
    segment.penup()
    segments.append(segment)

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide and clear the segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Reset the score, delay, and level
        score = 0
        delay = 0.1
        level = 1

        pen.update_score()

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        add_segment()

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.update_score()

    # Move the segments
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    head.move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide and clear the segments
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # Reset the score, delay, and level
            score = 0
            delay = 0.1
            level = 1

            pen.update_score()

    # Levels
    if level == 1 and score == 50:
        level += 1
        delay *= 0.9
    if level == 2 and score == 100:
        level += 1
        delay *= 0.9
    if level == 3 and score == 150:
        level += 1
        delay *= 0.9

    time.sleep(delay)

wn.mainloop()
