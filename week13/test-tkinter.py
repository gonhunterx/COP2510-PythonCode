import tkinter


class Inital_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LFPW Storage App")
        self.root.geometry("400x300")

        self.label = tkinter.Label(self.root, text="Welcome to LFPW Manager")
        # pack label
        self.label.pack()

        self.entry = tkinter.Entry(self.root)
        self.entry.pack()
        self.entry_input = self.entry.get()

        tkinter.mainloop()


def main():
    root = tkinter.Tk()
    app = Inital_GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
