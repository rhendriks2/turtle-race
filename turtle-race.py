from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
race_is_on = False
user_guess = screen.textinput(title="Make your guess", prompt="Which turtle will win the race? Choose between colors:\n"
                                                              "red, orange, yellow, green, blue and purple ")
# print(user_guess)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)
    # each own instance with own characteristics

if user_guess:
    race_is_on = True

while race_is_on:

    for turtle in all_turtles:

        if turtle.xcor() > 220:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)


screen.exitonclick()
