import tkinter


class MyGUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("400x300")
        self.label = tkinter.Label(self.root, text="Hello")
        self.label.pack()

        self.root.mainloop()


my_gui = MyGUI()


def main():
        
