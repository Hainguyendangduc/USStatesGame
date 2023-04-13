import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.tracer(0)

screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

write = turtle.Turtle()
write.hideturtle()
write.penup()

data = pd.read_csv("50_states.csv")
list = []
for i in range(50):
    screen.update()
    answer_states = screen.textinput(title=f"{len(list)}/50 States Correct", prompt="What's another state's name?").title()
    if (answer_states in list):
        i = i-1
    elif (answer_states in data.state.values):
        list.append(answer_states)
        state = data[data.state == answer_states]
        x = int(state.x.values)
        y = int(state.y.values)
        write.goto(x, y)
        write.write(answer_states, "center")
    else:
        i = i-1

screen.exitonclick()