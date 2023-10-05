menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25,
}

cart = []
total = 0
print("----------- menu -----------")
for key, value in menu.items():
    print(f"{key:9}: ${value:.2f}")
print("----------------------------")

# if you use True you will have to break out of the loop one way or another.
while True:
    food = input("Select an item (q to quit): ")
    if food.lower() == "q":
        break
    # doing this will make it so if something is entered not in the dictionary it will not append it to cart
    elif menu.get(food) is not None:
        cart.append(food)


for food in cart:
    total += menu.get(food)
    print(food, end=" ")
