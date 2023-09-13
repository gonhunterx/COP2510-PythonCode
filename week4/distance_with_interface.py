from tkinter import *

ws = Tk()
ws.title("Distance Driven Calculator")
ws.geometry("500x300")
mytext = StringVar()
Label()

# Creating text widget for display
result_text = Text(ws, height=10, width=40, state="disabled")
result_text.pack()


def distanceTraveled():
    vehicle_speed = int(speed_entry.get())
    hours_traveled = int(hours_entry.get())

    result_text.config(state="normal")  # temporarily enable textbox

    result_text.delete(1.0, END)  # clearing text

    for inital_hour in range(1, hours_traveled + 1):
        distance = vehicle_speed / hours_traveled
        result_text.insert(
            END,
            f"Hour {inital_hour}: Traveling at {vehicle_speed} MPH - Distance: {distance} miles \n",
        )

    result_text.config(state="disabled"),  # setting back to disabled


# Labels for input
speed_label = Label(ws, text="What is the vehicle's speed (MPH)?: ")
speed_label.pack()
speed_entry = Entry(ws)
speed_entry.pack()

hours_label = Label(ws, text="How many hours did you travel?: ")
hours_label.pack()
hours_entry = Entry(ws)
hours_entry.pack()

calculate_button = Button(ws, text="Calculate", command=distanceTraveled)
calculate_button.pack()


ws.mainloop()
