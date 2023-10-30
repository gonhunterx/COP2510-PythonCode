store_items = {"Sword": 250, "Axe": 225, "Hammer": 270}
print(store_items)
buy_item = input("Please select an item: ")
if buy_item.lower() == "sword":
    print(f"You buy a sword for {store_items['Sword']} gold")
else:
    print("you leave the shop")
