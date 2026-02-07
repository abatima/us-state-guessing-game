import turtle
import pandas

screen = turtle.Screen()
written_state = turtle.Turtle()
screen.title("US States Game")
background_image = "blank_states_img.gif"
correct_counter = 0
guessed_states = []
game_is_on = True
screen.addshape(background_image)
turtle.shape(background_image)

data = pandas.read_csv("50_states.csv")

while game_is_on:
    answer_state = screen.textinput(title=f"{correct_counter}/50 Guess the state", prompt="What's the name?").title()

    for state in data.state:
        if state == answer_state and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            correct_counter += 1

            #drawing

            state_row = data[data.state == answer_state]
            written_state.teleport(state_row.x.item(), state_row.y.item())
            written_state.hideturtle()
            written_state.write(answer_state)



    print(answer_state)
turtle.mainloop()