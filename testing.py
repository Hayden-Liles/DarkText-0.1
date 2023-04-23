class PlayerAttributes:
    inventory = []
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory # LIST
class Item:
    def __init__(self, item_name, damage):
        self.item_name = item_name
        self.damage = damage

class Weapons(Item):
    weapon_1 = Item("Me Sword", 100)


Player_1 = PlayerAttributes("Bob", [])

def get_name():
    Player_1.name = input("Enter name here: ").capitalize()
    commands()

def stats():
    items = [item.item_name for item in Player_1.inventory]

    print(f"Name = {Player_1.name}")
    if not items:  # if empty list
        print("Inventory is empty.")
    else:
        for i in range(0, len(items), 4):
            if i == 0:
                print("Inventory: ", end='')
            else:
                print("           ", end='')  # for non-first lines
            print(', '.join(items[i:i + 4]))

def commands():
    prompt = None
    prompt_choices = {"stats", "quit", "give"}
    while prompt not in prompt_choices:
        prompt = input("Enter Command: ").lower()
    if prompt == "stats":
        stats()
        commands()
    elif prompt == "quit":
        quit()
    elif prompt == "give":
        Player_1.inventory.append(Weapons.weapon_1)
        commands()

get_name()