import random
import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.setup(800, 700)
screen.bgcolor("black")
screen.title("Fractal Fern Generator - by codebyimran")
screen.tracer(0)

# Create turtle for drawing
t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()

# Color palette for the fern
colors = ["#00FF00", "#33FF33", "#66FF66", "#99FF99", "#CCFFCC"]
current_color_index = 0

# Create turtle for titles and information
text_turtle = turtle.Turtle()
text_turtle.speed(0)
text_turtle.penup()
text_turtle.hideturtle()
text_turtle.color("white")

# Display program information
def display_info():
    text_turtle.goto(0, 280)
    text_turtle.write("Fractal Fern Generator", align="center", font=("Courier", 20, "bold"))
    
    text_turtle.goto(0, 250)
    text_turtle.write("by codebyimran", align="center", font=("Courier", 14, "italic"))
    
    text_turtle.goto(0, -280)
    text_turtle.write("Click anywhere to exit", align="center", font=("Arial", 12, "normal"))
    
    text_turtle.goto(-350, 220)
    text_turtle.write("Algorithm: Barnsley Fern", align="left", font=("Arial", 10, "normal"))
    
    text_turtle.goto(-350, 200)
    text_turtle.write("Points: 10,000 iterations", align="left", font=("Arial", 10, "normal"))

# Starting point for fern
x, y = 0, 0

# Display initial information
display_info()

# Draw the enhanced Barnsley Fern
for i in range(10000):
    # Change color gradually
    if i % 2000 == 0 and i > 0:
        current_color_index = (current_color_index + 1) % len(colors)
        t.color(colors[current_color_index])
    
    t.goto(x * 60, y * 60 - 250)  # Scale and position
    t.dot(3)
    
    # Barnsley Fern transformation rules
    r = random.random()
    if r < 0.01:
        x = 0
        y = 0.16 * y
    elif r < 0.86:
        x = 0.85 * x + 0.04 * y
        y = -0.04 * x + 0.85 * y + 1.6
    elif r < 0.93:
        x = 0.2 * x - 0.26 * y
        y = 0.23 * x + 0.22 * y + 1.6
    else:
        x = -0.15 * x + 0.28 * y
        y = 0.26 * x + 0.24 * y + 0.44
    
    # Update progress
    if i % 1000 == 0:
        text_turtle.goto(300, -300)
        text_turtle.write(f"Progress: {i//100}/100%", align="right", font=("Arial", 10, "normal"))
        screen.update()

# Final update and completion message
screen.update()
text_turtle.goto(300, -300)
text_turtle.write("Progress: 100% - COMPLETE!", align="right", font=("Arial", 10, "bold"))

# Add a decorative border
border = turtle.Turtle()
border.speed(0)
border.penup()
border.hideturtle()
border.color("#444444")
border.pensize(2)
border.goto(-350, -320)
border.pendown()
for _ in range(2):
    border.forward(700)
    border.left(90)
    border.forward(600)
    border.left(90)

screen.exitonclick()