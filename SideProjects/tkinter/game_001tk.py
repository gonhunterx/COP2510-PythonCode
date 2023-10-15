import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.gold = 0


class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nagamitashima Game")
        self.style = Style("darkly")

        self.player = None
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_screen()
        frame = ttk.Frame(self.root)
        frame.grid(row=0, column=0, padx=10, pady=10)

        label = ttk.Label(frame, text="Welcome to Nagamitashima", style="bg.TLabel")
        label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        continue_btn = ttk.Button(frame, text="Continue", command=self.create_character)
        continue_btn.grid(row=1, column=0, padx=10, pady=10)

        exit_btn = ttk.Button(frame, text="Exit", command=self.root.quit)
        exit_btn.grid(row=1, column=1, padx=10, pady=10)

    def create_character(self):
        self.clear_screen()
        frame = ttk.Frame(self.root)
        frame.grid(row=0, column=0, padx=10, pady=10)

        label = ttk.Label(frame, text="Enter a username:")
        label.grid(row=0, column=0, padx=10, pady=10)

        username_entry = ttk.Entry(frame)
        username_entry.grid(row=0, column=1, padx=10, pady=10)

        start_btn = ttk.Button(
            frame,
            text="Start Game",
            command=lambda: self.start_game(username_entry.get()),
        )
        start_btn.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def start_game(self, username):
        self.player = Player(username)
        self.create_main_menu()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
