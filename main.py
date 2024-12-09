import turtle
import pandas
# import tkinter as tk

screen = turtle.Screen()
screen.title("NIGERIAN STATE GAME")
image = "blank_nigerian_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data =  pandas.read_csv("37_states.csv")
all_states = data.state.to_list()
guessed_states = []
#
# def create_input_window(x=-150, y=100):
#     answer_state = " "
# #
#     def submit():
#         global answer_state
#         answer_state = entry.get()
#         root.destroy()
#
#
# #     # Create a tkinter window
#     root = tk.Tk()
#     root.title("Guess the State")
# #
# #     # Set the position of the tkinter window
#     root.geometry(f"+{x}+{y}")
# #
# #     # Make the window always stay on top
#     root.wm_attributes("-topmost", 1)
# #
# #     # Create an entry field and a submit button
#     label = tk.Label(root, text="Enter a U.S. state:")
#     entry = tk.Entry(root)
#     submit_button = tk.Button(root, text="Submit", command=submit)
# #
# #     # Place the widgets on the tkinter window
#     label.pack()
#     entry.pack()
#     submit_button.pack()
# #
# #     # Start the tkinter main loop
#     root.mainloop()
# #
#     return answer_state
# #
# #
# # # Example usage:
# # # Call the function to create the input window at a specific position
# x_pos = -150
# y_pos = 200
# result = create_input_window(x_pos, y_pos)
# # print(f"State entered: {result}")


while len(guessed_states) < 37:
    answer_state = screen.textinput(f"{len(guessed_states)} Out of 37 States",
                                    prompt= "Guess Another State Name?").title()


    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("State_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


screen.exitonclick()