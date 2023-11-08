import tkinter


class ListBox:
    def __init__(self):
        self.window = tkinter.Tk()

        self.listbox = tkinter.Listbox(self.window)
        self.listbox.pack(padx=10, pady=10)

        # populate list
        self.listbox.insert(0, "Monday")
        self.listbox.insert(1, "Tuesday")
        self.listbox.insert(2, "Wednesday")
        self.listbox.insert(3, "Thursday")
        self.listbox.insert(4, "Friday")
        self.listbox.insert(5, "Saturday")
        self.listbox.insert(6, "Sunday")

        tkinter.mainloop()


if __name__ == "__main__":
    listbox = ListBox()
