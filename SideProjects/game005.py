import random

game_map = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#"],
]

# players starting pos
player_x, player_y = 1, 1


while True:
    # display the game map
    for row in game_map:
        print(" ".join(row))

    # get player input
    move = input("enter a direction (w/a/s/d): ")
    # move player
    if move == "w" and game_map[player_y - 1][player_x] == ".":
        game_map[player_y][player_x] = "."
        player_y -= 1
    elif move == "a" and game_map[player_y][player_x - 1] == ".":
        game_map[player_y][player_x] = "."
        player_x -= 1
    elif move == "s" and game_map[player_y + 1][player_x] == ".":
        game_map[player_y][player_x] = "."
        player_y += 1
    elif move == "d" and game_map[player_y][player_x + 1] == ".":
        game_map[player_y][player_x] = "."
        player_x += 1

    # check for game over
    if game_map[player_y][player_x] == "#":
        print("game over!")
        break

    game_map[player_y][player_x] = "@"


main()
