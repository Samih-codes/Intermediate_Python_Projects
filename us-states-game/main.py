import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
	answer = screen.textinput(title= f"{len(guessed_states)}/50 States Correct ",
									prompt = "Can you name a State?").title()
	if answer == "Exit":
		missed_states = []
		for state in state_list:
			if state not in guessed_states:
				missed_states.append(state)
		new_data = pandas.DataFrame(missed_states)
		new_data.to_csv("states_to_practice.csv")
		break

	if answer in state_list:
		guessed_states.append(answer)
		t = turtle.Turtle()
		t.hideturtle()
		t.penup()
		state_data = data[data.state == answer]
		t.goto(int(state_data.x), int(state_data.y))
		t.write(answer)

