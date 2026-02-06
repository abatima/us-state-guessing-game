import turtle

screen = turtle.Screen()
screen.title("US States Game")
background_image = "blank_states_img.gif"

screen.addshape(background_image)
turtle.shape(background_image)

guessed_state = screen.textinput(title="Guess the state", prompt="What's the name?")
print(guessed_state)
turtle.mainloop()