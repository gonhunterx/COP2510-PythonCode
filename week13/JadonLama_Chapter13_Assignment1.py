import tkinter as tk


class MyGUI:
    def __init__(self):
        # create main window
        self.window = tk.Tk()
        # self.window.geometry("400x300")

        # string var values
        self.name_value = tk.StringVar()
        self.street_value = tk.StringVar()
        # city state zip
        self.csz_value = tk.StringVar()

        # creating two frames
        self.info_frame = tk.Frame(self.window)
        self.button_frame = tk.Frame(self.window)

        # button widget
        # self.my_button = tk.Button(
        #     self.window, text="Click me", command=self.do_something
        # )

        # label widgets associated with strvars
        self.name_label = tk.Label(self.info_frame, textvariable=self.name_value)
        self.street_label = tk.Label(self.info_frame, textvariable=self.street_value)
        self.csz_label = tk.Label(self.info_frame, textvariable=self.csz_value)

        # packing labels
        self.name_label.pack()
        self.street_label.pack()
        self.csz_label.pack()
        # self.my_button.pack()

        # create the button widgets
        self.show_info_button = tk.Button(
            self.button_frame, text="Show info", command=self.display_info
        )
        self.quit_button = tk.Button(
            self.button_frame, text="Quit", command=self.window.destroy
        )
        # pack buttons
        self.show_info_button.pack(side="left")
        self.quit_button.pack(side="right")

        self.info_frame.pack()
        self.button_frame.pack()

        tk.mainloop()

    def display_info(self):
        self.name_value.set("Jadon Lama")
        self.street_value.set("43 west main rd")
        self.csz_value.set("Cortez, FL 14850")


my_gui = MyGUI()
