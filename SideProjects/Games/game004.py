import sys
import tkinter as tk
from tkinter import messagebox


# Classes
class Player:
    def __init__(self, name):
        self.name = name
        self.coins = 0
        self.inventory = []

    def display_stats(self):
        stats_text = f"🙂‍↔️ User: {self.name}\n💰 Coins: {self.coins}\n🎒 Inventory:\n"
        for item in self.inventory:
            stats_text += f"{item.name}: {item.value} coins\n"
        return stats_text


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


# Items for inventory
wood_log = Item("Wood Log", 4)
wheat = Item("Wheat", 2)


# Functions
def intro_menu():
    welcome_label.config(text="Welcome to Nomata")
    start_button.config(state=tk.NORMAL)
    quit_button.config(state=tk.NORMAL)


def start_game():
    player_name = name_entry.get()
    if player_name.strip() == "":
        messagebox.showerror("Error", "Please enter your name.")
    else:
        player.name = player_name
        intro_frame.pack_forget()
        main_menu_frame.pack()


def quit_game():
    sys.exit()


def main_menu():
    main_menu_label.config(text="Main Menu")
    farm_button.config(state=tk.NORMAL)
    woods_button.config(state=tk.NORMAL)
    market_button.config(state=tk.NORMAL)
    stats_button.config(state=tk.NORMAL)
    quit_button2.config(state=tk.NORMAL)


def go_to_farm():
    farm_frame.pack()


def farm():
    farm_label.config(text="You walk to the farm...")
    farm_button.config(state=tk.NORMAL)
    leave_button.config(state=tk.NORMAL)


def chop():
    farm_label.config(text="You farm some wheat. +1 wheat")
    player.inventory.append(wheat)
    farm_button.config(state=tk.NORMAL)
    leave_button.config(state=tk.NORMAL)


def leave_farm():
    farm_frame.pack_forget()
    main_menu_frame.pack()


def go_to_woods():
    woods_frame.pack()


def woods():
    woods_label.config(text="You walk into the woods...")
    chop_button.config(state=tk.NORMAL)
    leave_button2.config(state=tk.NORMAL)


def chop_wood():
    woods_label.config(text="You chop some wood. +1 wood log")
    player.inventory.append(wood_log)
    chop_button.config(state=tk.NORMAL)
    leave_button2.config(state=tk.NORMAL)


def leave_woods():
    woods_frame.pack_forget()
    main_menu_frame.pack()


def go_to_market():
    market_frame.pack()


def market():
    market_label.config(text="You enter the market...")
    sell_button.config(state=tk.NORMAL)
    leave_button3.config(state=tk.NORMAL)


def sell():
    # You can add logic here to sell items and update player's coins
    pass


def leave_market():
    market_frame.pack_forget()
    main_menu_frame.pack()


def display_stats():
    stats_label.config(text=player.display_stats())
    main_menu_frame.pack_forget()
    stats_frame.pack()


def back_to_main_menu():
    stats_frame.pack_forget()
    main_menu_frame.pack()


# Initialize Tkinter
root = tk.Tk()
root.title("Nomata Game")
root.geometry("500x350")

# Create player instance
player = Player("")

# Intro Menu
intro_frame = tk.Frame(root)
intro_frame.pack(pady=50)

welcome_label = tk.Label(intro_frame, text="Welcome to Nomata", font=("Roboto", 16))
welcome_label.pack()

name_label = tk.Label(intro_frame, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(intro_frame)
name_entry.pack()

start_button = tk.Button(intro_frame, text="Start", command=start_game)
start_button.pack()

quit_button = tk.Button(intro_frame, text="Quit", command=quit_game)
quit_button.pack()

# Main Menu
main_menu_frame = tk.Frame(root)

main_menu_label = tk.Label(main_menu_frame, text="Main Menu", font=("Roboto", 16))
main_menu_label.pack(pady=10)

farm_button = tk.Button(main_menu_frame, text="Go to Farm", command=go_to_farm)
farm_button.pack()

woods_button = tk.Button(main_menu_frame, text="Go to Woods", command=go_to_woods)
woods_button.pack()

market_button = tk.Button(main_menu_frame, text="Go to Market", command=go_to_market)
market_button.pack()

stats_button = tk.Button(
    main_menu_frame, text="Display Stats/Inventory", command=display_stats
)
stats_button.pack()

quit_button2 = tk.Button(main_menu_frame, text="Quit", command=quit_game)
quit_button2.pack()

# Farm
farm_frame = tk.Frame(root)

farm_label = tk.Label(farm_frame, text="You walk to the farm...", font=("Roboto", 14))
farm_label.pack(pady=20)

farm_button = tk.Button(farm_frame, text="Farm", command=chop)
farm_button.pack()

leave_button = tk.Button(farm_frame, text="Leave", command=leave_farm)
leave_button.pack()

# Woods
woods_frame = tk.Frame(root)

woods_label = tk.Label(
    woods_frame, text="You walk into the woods...", font=("Roboto", 14)
)
woods_label.pack(pady=20)

chop_button = tk.Button(woods_frame, text="Chop", command=chop_wood)
chop_button.pack()

leave_button2 = tk.Button(woods_frame, text="Leave", command=leave_woods)
leave_button2.pack()

# Market
market_frame = tk.Frame(root)

market_label = tk.Label(
    market_frame, text="You enter the market...", font=("Roboto", 14)
)
market_label.pack(pady=20)

sell_button = tk.Button(market_frame, text="Sell", command=sell)
sell_button.pack()

leave_button3 = tk.Button(market_frame, text="Leave", command=leave_market)
leave_button3.pack()

# Stats/Inventory
stats_frame = tk.Frame(root)

stats_label = tk.Label(stats_frame, text="", font=("Roboto", 14))
stats_label.pack(pady=20)

back_button = tk.Button(
    stats_frame, text="Back to Main Menu", command=back_to_main_menu
)
back_button.pack()

root.mainloop()
