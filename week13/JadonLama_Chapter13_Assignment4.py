import tkinter as tk

# I utilized both the grid and pack function. It works well because the button frame only
# has two options, but placing the other objects in specific rows and columns works well.


class MyGUI:
    def __init__(self):
        # create main window
        self.window = tk.Tk()
        self.window.geometry("400x300")
        self.window.title("Fahrenheit Calculator")

        # creating the variables to set for the calulations
        self.cel_num = tk.StringVar()
        self.fah_num = tk.StringVar()

        # creating two frames
        self.info_frame = tk.Frame(self.window)
        self.button_frame = tk.Frame(self.window)

        # Labels ---------------------------------------
        tk.Label(self.info_frame, text="Enter the Celsius temperature: ").grid(
            row=0, column=0
        )
        tk.Label(self.info_frame, text="Fahrenheit temperature: ").grid(row=1, column=0)
        # label for the results section that is within the info_frame.
        self.result_label = tk.Label(self.info_frame, textvariable=self.fah_num).grid(
            row=1, column=1
        )

        # Entry box ------------------------------------
        tk.Entry(self.info_frame, textvariable=self.cel_num).grid(row=0, column=1)

        # create the button widgets --------------------
        self.show_info_button = tk.Button(
            self.button_frame, text="Calculate", command=self.display_info
        )
        self.quit_button = tk.Button(
            self.button_frame, text="Quit", command=self.window.destroy
        )
        # pack buttons ---------------------------------
        self.show_info_button.pack(side="left")
        self.quit_button.pack(side="right")

        # pack the button frames to create two of them
        self.info_frame.pack()
        self.button_frame.pack()

        # main loop for the program --------------------
        tk.mainloop()

    # function to get the value entered and convert it into fahrenheit
    def display_info(self):
        # try except for invalid inputs
        try:
            # creating variables to preform calculations on and set as the fah
            cel_value = float(self.cel_num.get())
            # preforming the calculation on the cel_value to get the fahrenheit's value
            fah_value = (cel_value * 9 / 5) + 32
            # setting the value for fah_num and formatting the input to display 2 decimal places
            self.fah_num.set(f"{fah_value:.2f}")
        except ValueError:
            # handle invalid inputs
            self.fah_num.set("Invalid Input.")


my_gui = MyGUI()
