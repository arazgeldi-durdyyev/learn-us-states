import turtle
import pandas
import csv
FONT = ("Adobe Gothic", 19, "normal")


def get_mouse_click_coor(x, y):
    print(x, y)


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=500)
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    guess = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                             prompt="What is another state name?").title()

    if guess == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states_for_learning.csv")
        break

    if guess in states and guess not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess]
        t.color("black")
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(guess)
    else:
        pass
    # turtle.onscreenclick(get_mouse_click_coor)

# screen.exitonclick()
# turtle.mainloop()
