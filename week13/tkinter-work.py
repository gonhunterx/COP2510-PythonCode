import tkinter


class MyGUI:
    def __init__(self):
        # create the main window widget.
        self.main_window = tkinter.Tk()
        self.main_window.geometry("400x300")
        # create a label widget
        self.label = tkinter.Label(self.main_window, text="hello world")

        self.label.pack()

        # enter the tkinter main loop
        tkinter.mainloop()


# create an instance of the my gui class so it runss
my_gui = MyGUI()
