import tkinter


class MyGUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("400x300")
        self.label = tkinter.Label(self.root, text="Hello")
        self.label.pack()

        self.menu = tkinter.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Option 1", command=self.option1)
        self.menu.add_command(label="Option 2", command=self.option2)

        self.menu_button = tkinter.Menubutton(self.root, text="Options", menu=self.menu)
        self.menu_button.pack()

        self.root.mainloop()

    def option1(self):
        print("option 1 selected")

    def option2(self):
        print("option 2 selected")

    def start(self):
        self.root.mainloop()


my_gui = MyGUI()
my_gui.start()

# def main():


# I just need to create the GUI with a few extra tabs
# this will allow me to now show a tab unless the user logs in
# or i can use django and a web auth program.
