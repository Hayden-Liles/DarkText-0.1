import pickle
import random
import math as m

def stats_show():
    player_att_call()
    inventory_eq_call()
    Player.xp_req = ((.02 * ((Player.level + 1) * (Player.level + 1) * (Player.level + 1))) + (
            3.06 * ((Player.level + 1) * (Player.level + 1))) + (105 + Player.level + 1))
    print(
        "\033[0;33m\n=====================================================================\033[31;3m\033[31;1m",
        "\n   " + str(Player.player_name) + ": Lvl " + str(Player.level),
        " | Health: " + str(m.trunc(Player.cur_health)) + "/" + str(m.trunc(Player.max_health)),
        "| XP: " + str(m.trunc(Player.xp)) + "/" + str(m.trunc(Player.xp_req)),
        " | Weight: " +str(m.trunc(Player.cur_weight)) + "/" + str(m.trunc(Player.max_weight)),
        "\n\033[0;33m=====================================================================",
        "\n\033[0;1m\033[36;3mAttributes:",
        "\n\033[0;34m   Vitality     : \033[33;1m" + str(Player.vitality),
        "\n\033[0;34m   Resistance   : \033[33;1m" + str(Player.resistance),
        "\n\033[0;34m   Strength     : \033[33;1m" + str(Player.strength),
        "\n\033[0;34m   Intelligence : \033[33;1m" + str(Player.intelligence),
        "\n\n\033[36;3mStats:"
        "\n\033[0;34m   Health     : \033[33;1m" + str(m.trunc(Player.max_health)),
        "\n\033[0;34m   Damage     : \033[33;1m" + str(m.trunc(Player.damage)),
        "\n\033[0;34m   Defense    : \033[33;1m" + str(m.trunc(Player.defense)),
        "\n\033[0;34m   Max Weight : \033[33;1m" + str(m.trunc(Player.max_weight)),
        "\n\n\033[36;3mEquipped:",
        "\n\033[0;34;1m    Armor",
        "\n\033[0;34m       Head  : " + "\033[33;1m" + str(Player.inventory_eq[0].name) + " \033[31;1m--> \033[32;1mDefence: \033[37;1m" + str(Player.inventory_eq[0].armor_defense) + "\033[31;1m || \033[32;1mWeight: \033[37;1m" + str(Player.inventory_eq[0].weight),
        "\n\033[0;34m       Body  : " + "\033[33;1m" + str(Player.inventory_eq[1].name) + " \033[31;1m--> \033[32;1mDefence: \033[37;1m" + str(Player.inventory_eq[1].armor_defense) + "\033[31;1m || \033[32;1mWeight: \033[37;1m" + str(Player.inventory_eq[1].weight),
        "\n\033[0;34m       Hands : " + "\033[33;1m" + str(Player.inventory_eq[2].name) + " \033[31;1m--> \033[32;1mDefence: \033[37;1m" + str(Player.inventory_eq[2].armor_defense) + "\033[31;1m || \033[32;1mWeight: \033[37;1m" + str(Player.inventory_eq[2].weight),
        "\n\033[0;34m       Legs  : " + "\033[33;1m" + str(Player.inventory_eq[3].name) + " \033[31;1m--> \033[32;1mDefence: \033[37;1m" + str(Player.inventory_eq[3].armor_defense) + "\033[31;1m || \033[32;1mWeight: \033[37;1m" + str(Player.inventory_eq[3].weight),
        "\n    \033[34;1mWeapons"
        "\n\033[0;34m       Primary Weapon   : " + "\033[33;1m" + str(Player.inventory_eq[4].name) + " \033[31;1m--> \033[32;1mDamage: \033[37;1m" + str(Player.inventory_eq[4].attack) + "\033[31;1m || \033[32;1mBlock: \033[37;1m" + str(Player.inventory_eq[4].block) + "\033[31;1m || \033[32;1mWeight: \033[37;1m" + str(Player.inventory_eq[4].weight),
        "\n\033[0;34m       Secondary Weapon : " + "\033[33;1m" + str(Player.inventory_eq[5].name) + " \033[31;1m--> \033[32;1mDamage: \033[37;1m" + str(Player.inventory_eq[5].attack) + "\033[31;1m || \033[32;1mBlock: \033[37;1m" + str(Player.inventory_eq[5].block) + "\033[31;1m || \033[32;1mWeight: \033[37;1m" + str(Player.inventory_eq[5].weight),
        "\n\n\033[36;3m")
    items = [item.name for item in Player.inventory]
    item_num = 0
    if not items:
        print(" Inventory is empty.")
    else:
        for i in range(0, len(items), 4):
            if i == 0:
                print("Inventory: \033[0;34m", end='')
            else:
                item_num += 1
                print("           \033[0;34m", end='')
            print('\033[33;1m, \033[0;34m'.join(items[i:i + + 4]))
    print("\n\033[0;33m================================================================\n\033[0;0m")

def player_att_call():
    Player.damage = (((Player.strength * .26) * Player.eq_weapon1.attack) + (Player.eq_weapon2.attack * 0.5))

    Player.defense = ((Player.eq_head.armor_defense + Player.eq_body.armor_defense + Player.eq_hands.armor_defense +
                       Player.eq_legs.armor_defense) * (Player.resistance * 2.2)) + (Player.eq_weapon1.block + Player.eq_weapon2.block)

    Player.max_health = (100 + (Player.vitality * 13))

    Player.cur_health = Player.max_health

    Player.crit_damage = (Player.eq_weapon1.critical_damage + Player.eq_weapon1.critical_damage + Player.damage)

    Player.max_weight = (50 + (Player.strength * 1.2))

    Player.cur_weight = (Player.eq_weapon1.weight + Player.eq_weapon2.weight + Player.eq_head.weight +
                         Player.eq_body.weight + Player.eq_hands.weight + Player.eq_legs.weight)

    Player.weight_percentage = (1 - (Player.cur_weight / Player.max_weight))

    Player.total_attack = (Player.strength + Player.intelligence + Player.resistance)

def enemy_att_call():
    vitality_number_one = Player.vitality - 3
    vitality_number_two = Player.vitality + 2
    strength_number_one = Player.strength - 3
    strength_number_two = Player.strength + 2
    intelligence_number_one = Player.intelligence - 3
    intelligence_number_two = Player.intelligence + 2
    resistance_number_one = Player.intelligence - 3
    resistance_number_two = Player.intelligence + 2

    vitality_random_number = random.randint(vitality_number_one, vitality_number_two)
    strength_random_number = random.randint(strength_number_one, strength_number_two)
    intelligence_random_number = random.randint(intelligence_number_one, intelligence_number_two)
    resistance_random_number = random.randint(resistance_number_one, resistance_number_two)

    enemy_random_number = random.randint(6, 9)

    Enemy.vitality = vitality_random_number
    Enemy.strength = strength_random_number
    Enemy.intelligence = intelligence_random_number
    Enemy.resistance = resistance_random_number

    Enemy.level = ((Enemy.vitality + Enemy.strength + Enemy.intelligence) - 10)

    Enemy.eq_weapon1 = ClassAttributes.enemy_list[enemy_random_number].eq_weapon1
    Enemy.eq_weapon2 = ClassAttributes.enemy_list[enemy_random_number].eq_weapon2
    Enemy.eq_head = ClassAttributes.enemy_list[enemy_random_number].eq_head
    Enemy.eq_body = ClassAttributes.enemy_list[enemy_random_number].eq_body
    Enemy.eq_hands = ClassAttributes.enemy_list[enemy_random_number].eq_hands
    Enemy.eq_legs = ClassAttributes.enemy_list[enemy_random_number].eq_legs
    Enemy.mob_name = ClassAttributes.enemy_list[enemy_random_number].mob_name

    Enemy.damage = (((Enemy.strength * .26) * Enemy.eq_weapon1.attack) + (Enemy.eq_weapon2.attack * 0.5))

    Enemy.defense = ((Enemy.eq_head.armor_defense + Enemy.eq_body.armor_defense + Enemy.eq_hands.armor_defense +
                      Enemy.eq_legs.armor_defense) * (Enemy.resistance * 2.2)) + (Enemy.eq_weapon1.block + Enemy.eq_weapon2.block)

    Enemy.total_attack = (Enemy.strength + Enemy.intelligence + Enemy.resistance)

    Enemy.max_health = (100 + (Enemy.vitality * 1.4))
    Enemy.cur_health = Enemy.max_health

    if Player.total_attack > Enemy.total_attack:
        Player.attack_chance = (100 * (Enemy.total_attack / Player.total_attack))
    elif Player.total_attack < Enemy.total_attack:
        Player.attack_chance = (100 * (1-(Player.total_attack / Enemy.total_attack)))

    if Player.damage > Enemy.defense:
        Player.true_damage = Player.damage - Enemy.defense
    elif Player.damage <= Enemy.defense:
        Player.true_damage = (Player.damage * .1)

    if Enemy.damage > Player.defense:
        Enemy.true_damage = Enemy.damage - Player.defense
    elif Enemy.damage <= Player.defense:
        Enemy.true_damage = (Enemy.damage * .1)

    Enemy.xp = (Enemy.level * 12.5)


    fight()

def enemy_drops():
    print("WORK")
    drop_chance = 25
    drop = None
    chance_num = random.randint(0, 2)
    while drop is None:
        drop = random.randint(0, 5)
        if drop_chance >= chance_num:
            if drop == 0:
                if Enemy.eq_head.name != "none":
                    Player.ground_items.append(Enemy.eq_head)
                    print("Enemy dropped: " + str(Enemy.eq_head.name))
                else:
                    print("No Items")
            if drop == 1:
                if Enemy.eq_body.name != "none":
                    Player.ground_items.append(Enemy.eq_body)
                    print("Enemy dropped: " + str(Enemy.eq_body.name))
                else:
                    print("No Items")
            if drop == 2:
                if Enemy.eq_hands.name != "none":
                    Player.ground_items.append(Enemy.eq_hands)
                    print("Enemy dropped: " + str(Enemy.eq_hands.name))
                else:
                    print("No Items")
            if drop == 3:
                if Enemy.eq_legs.name != "none":
                    Player.ground_items.append(Enemy.eq_legs)
                    print("Enemy dropped: " + str(Enemy.eq_legs.name))
                else:
                    print("No Items")
            if drop == 4:
                if Enemy.eq_weapon1.name != "none":
                    Player.ground_items.append(Enemy.eq_weapon1)
                    print("Enemy dropped: " + str(Enemy.eq_weapon1.name))
                else:
                    print("No Items")
            if drop == 5:
                if Enemy.eq_weapon2.name != "none":
                    Player.ground_items.append(Enemy.eq_weapon2)
                    print("Enemy dropped: " + str(Enemy.eq_weapon2.name))
                else:
                    print("No Items")

def pick_up():
    if (len(Player.ground_items)) == 0:
        print("No items to pick up")
    else:
        print("Items")
        i = -1
        for x in Player.ground_items:
            i += 1
            print(str(i) + ". " + str(x.name))
        picked_item = 8705
        while picked_item == 8705 or picked_item > i or picked_item < i:
            try:
                picked_item = int(input("What would you like to pick up? "))
            except ValueError:
                print("That is not a number")
                continue
            try:
                if picked_item <= i:
                    Player.inventory.append(Player.ground_items[picked_item])
                    print("You picked up: " + str(Player.ground_items[picked_item].name))
                    del Player.ground_items[picked_item]
                    break
                else:
                    pick_up()
            except IndexError:
                print("That is not a valid number")
                pick_up()

def unequip():
    print("\033[33;1mthe number is expected\n")
    i = -1
    for x in Player.inventory_eq:
        i += 1
        if x.name != "none":
            print("\033[32;1m" + str(i) + ". " + str(x.name))
        elif x.type == "head":
            print("\033[31;1mNothing in Head slot")
        elif x.type == "body":
            print("\033[31;1mNothing in Body slot")
        elif x.type == "hands":
            print("\033[31;1mNothing in Hands slot")
        elif x.type == "legs":
            print("\033[31;1mNothing in Legs slot")
        elif x.type == "weapon" :
            print("\033[31;1mNothing in this Weapon slot")
    print()

    equip_item = 9091
    while equip_item == 9091:
        try:
            equip_item = int(input("\033[35;1mWhat would you like to unequip? \033[34;1m"))
        except ValueError:
            print("That is not a number")
            continue
        else:
            if equip_item > (len(Player.inventory_eq)) or equip_item < 0 or equip_item == False:
                unequip()
            else:
                if Player.inventory_eq[equip_item].type == "head":
                    if Player.eq_head.name != "none":
                        Player.inventory.append(Player.eq_head)
                        print("You unequipped: " + str(Player.eq_head.name))
                        Player.eq_head = Armor.none_armor_head
                        inventory_eq_call()
                    elif Player.eq_head == "none":
                        continue

                elif Player.inventory_eq[equip_item].type == "body":
                    if Player.eq_body.name != "none":
                        Player.inventory.append(Player.eq_body)
                        print("You unequipped: " + str(Player.eq_body.name))
                        Player.eq_body = Armor.none_armor_body
                        inventory_eq_call()
                    elif Player.eq_body.name == "none":
                        continue
                elif Player.inventory_eq[equip_item].type == "hands":
                    if Player.eq_hands.name != "none":
                        Player.inventory.append(Player.eq_hands)
                        print("You unequipped: " + str(Player.eq_hands.name))
                        Player.eq_hands = Armor.none_armor_hands
                        inventory_eq_call()
                    elif Player.eq_hands.name == "none":
                        continue
                elif Player.inventory_eq[equip_item].type == "legs":
                    if Player.eq_legs.name != "none":
                        Player.inventory.append(Player.eq_legs)
                        print("You unequipped: " + str(Player.eq_legs.name))
                        Player.eq_legs = Armor.none_armor_legs
                        inventory_eq_call()
                    elif Player.eq_legs.name == "none":
                        continue
                elif Player.inventory_eq[equip_item].type == "weapon":
                    if Player.inventory_eq[equip_item].name == "none":
                        continue
                    elif Player.inventory_eq[equip_item].name != "none":
                        if Player.inventory_eq[equip_item].name == Player.eq_weapon1.name:
                            Player.inventory.append(Player.eq_weapon1)
                            print("You unequipped: " + str(Player.eq_weapon1.name))
                            Player.eq_weapon1 = Weapons.none_weapon
                            inventory_eq_call()
                        elif Player.inventory_eq[equip_item].name == Player.eq_weapon2.name:
                            Player.inventory.append(Player.eq_weapon2)
                            print("You unequipped: " + str(Player.eq_weapon2.name))
                            Player.eq_weapon2 = Weapons.none_weapon
                            inventory_eq_call()
                        elif Player.inventory_eq[equip_item].name == Player.eq_weapon1.name and Player.inventory_eq[equip_item].name == Player.eq_weapon2.name:
                            choice = input("Would you like to unequip this to primary or secondary? ").lower()
                            if choice == "primary":
                                Player.inventory.append(Player.eq_weapon1)
                                print("You unequipped: " + str(Player.eq_weapon1.name))
                                Player.eq_weapon1 = Weapons.none_weapon
                                inventory_eq_call()
                            elif choice == "secondary":
                                    Player.inventory.append(Player.eq_weapon2)
                                    print("You unequipped: " + str(Player.eq_weapon2.name))
                                    Player.eq_weapon2 = Weapons.none_weapon
                                    inventory_eq_call()

def equip():
    if (len(Player.inventory)) == 0:
        print("No items in inventory")
    else:
        i = -1
        print("the number is expected")
        for x in Player.inventory:
            i += 1
            print(str(i) + ". " + str(x.name))
        equip_item = 9091
        while equip_item == 9091:
            try:
                equip_item = int(input("What would you like to equip? "))
            except ValueError:
                continue
            try:
                if Player.inventory[equip_item].type == "head":
                    if Player.eq_head.name != "none":
                        Player.inventory.append(Player.eq_head)
                        Player.eq_head = Player.inventory[equip_item]
                        Player.inventory.pop(equip_item)
                        inventory_eq_call()
                    elif Player.eq_head.name == "none":
                        Player.eq_head = Player.inventory[equip_item]
                        Player.inventory.pop(equip_item)
                        inventory_eq_call()
                    print("You equipped: " + str(Player.eq_head.name))
                elif Player.inventory[equip_item].type == "body":
                    if Player.eq_body.name != "none":
                        Player.inventory.append(Player.eq_body)
                        Player.eq_body = Player.inventory[equip_item]
                        Player.inventory.pop(equip_item)
                        inventory_eq_call()
                    elif Player.eq_body.name == "none":
                        Player.eq_body = Player.inventory[equip_item]
                        Player.inventory.pop(equip_item)
                        inventory_eq_call()
                    print("You equipped: " + str(Player.eq_body.name))
                elif Player.inventory[equip_item].type == "hands":
                    if Player.eq_hands.name != "none":
                        Player.inventory.append(Player.eq_hands)
                        Player.eq_hands = Player.inventory[equip_item]
                        Player.inventory.pop(equip_item)
                        inventory_eq_call()
                    elif Player.eq_hands.name == "none":
                        Player.eq_hands = Player.inventory[equip_item]
                        Player.inventory.pop(equip_item)
                        inventory_eq_call()
                    print("You equipped: " + str(Player.eq_hands.name))
                elif Player.inventory[equip_item].type == "legs":
                    if Player.eq_legs.name != "none":
                        Player.inventory.append(Player.eq_legs)
                        Player.eq_legs = Player.inventory[equip_item]
                        Player.inventory.pop(equip_item)
                        inventory_eq_call()
                    elif Player.eq_legs.name == "none":
                        Player.eq_legs = Player.inventory[equip_item]
                        Player.inventory.pop(equip_item)
                        inventory_eq_call()
                    print("You equipped: " + str(Player.eq_legs.name))
                elif Player.inventory[equip_item].type == "weapon":
                    if Player.inventory[equip_item].str_req <= Player.strength and Player.inventory[equip_item].int_req <= Player.intelligence:
                        if Player.inventory[equip_item].handed == "two-handed":
                            if Player.eq_weapon1.name != "none" and Player.eq_weapon2 != "none":
                                Player.inventory.append(Player.eq_weapon1)
                                Player.inventory.append(Player.eq_weapon2)
                                Player.eq_weapon1 = Player.inventory[equip_item]
                                Player.eq_weapon2 = Weapons.none_weapon
                                Player.inventory.pop(equip_item)
                                inventory_eq_call()
                            elif Player.eq_weapon1.name != "none" and Player.eq_weapon2.name == "none":
                                Player.inventory.append(Player.eq_weapon1)
                                Player.eq_weapon1 = Player.inventory[equip_item]
                                Player.inventory.pop(equip_item)
                                inventory_eq_call()
                            elif Player.eq_weapon1.name == "none" and Player.eq_weapon2.name != "none":
                                Player.inventory.append(Player.eq_weapon2)
                                Player.eq_weapon1 = Player.inventory[equip_item]
                                Player.eq_weapon2 = Weapons.none_weapon
                                Player.inventory.pop(equip_item)
                                inventory_eq_call()
                            print("You equipped: " + str(Player.eq_weapon1.name))
                        elif Player.inventory[equip_item].handed == "one-handed":
                            hand_choice = ("primary", "secondary")
                            choice = None
                            while choice not in hand_choice:
                                choice = input("Would you like to equip this to primary or secondary? ").lower()
                                if choice == "primary":
                                    if Player.eq_weapon1.name != "none":
                                        Player.inventory.append(Player.eq_weapon1)
                                        Player.eq_weapon1 = Player.inventory[equip_item]
                                        Player.inventory.pop(equip_item)
                                        inventory_eq_call()
                                    elif Player.eq_weapon1.name == "none":
                                        Player.eq_weapon1 = Player.inventory[equip_item]
                                        Player.inventory.pop(equip_item)
                                        inventory_eq_call()
                                    print("You equipped: " + str(Player.eq_weapon1.name))
                                elif choice == "secondary":
                                    if Player.eq_weapon2.name != "none":
                                        Player.inventory.append(Player.eq_weapon2)
                                        Player.eq_weapon2 = Player.inventory[equip_item]
                                        Player.inventory.pop(equip_item)
                                        inventory_eq_call()
                                    elif Player.eq_weapon2.name == "none":
                                        Player.eq_weapon2 = Player.inventory[equip_item]
                                        Player.inventory.pop(equip_item)
                                        inventory_eq_call()
                                    print("You equipped: " + str(Player.eq_weapon2.name))
                    else:
                        print("You are not good enough to use this")
                        print("Required Intelligence: " + str(Player.inventory[equip_item].int_req) + " | Your Intelligence: " + str(Player.intelligence),
                              "Required Strength: " + str(Player.inventory[equip_item].str_req) + " | Your Strength: " + str(Player.strength))
                else:
                    print("You can't equip that!")

            except IndexError:
                print("That is not a valid number")
                return

def drop():
    if (len(Player.inventory)) == 0:
        print("No items to pick up")
        from Dark_Text import Player_Command
        Player_Command()


    i = -1
    print("the number is expected")
    for x in Player.inventory:
        i += 1
        print(str(i) + ". " + str(x.name))
    drop_item = 9091
    while drop_item == 9091:
        try:
            drop_item = int(input("What would you like to drop? "))
        except ValueError:
            print("That is not a number")
            continue
        try:
            double_check = None
            check_choices = ("yes", "no")
            while double_check not in check_choices:
                double_check = input("Are you sure? (yes/no): ")
                if double_check == "yes":
                    print("You dropped: " + str(Player.inventory[drop_item].name))
                    Player.ground_items.append(Player.inventory[drop_item])
                    Player.inventory.pop(drop_item)
                elif double_check == "no":
                    pass
        except IndexError:
            print("That is not a valid number")
            drop()

def show():
    if (len(Player.inventory)) != 0:
        i = -1
        for x in Player.inventory:
            i += 1
            print(str(i) + ". " + str(x.name))
        inv_num = 9918
        while inv_num == 9918:
            try:
                inv_num = int(input("What would you like to inspect? (number): "))
            except ValueError:
                print("That is not a number")
                continue
            try:
                item = Player.inventory[inv_num]
                if item.type == "weapon":
                    print("\n"+str(item.name) + " --> Damage: " + str(m.trunc(item.attack)) + " || Block: " + str(m.trunc(item.block)) + " || Weight: " + str(m.trunc(item.weight)),
                          "\n             Strength Required: " + str(item.str_req) + " || Intelligence Required: " + str(item.int_req))
                elif item.type =="blueprint":
                    print("That is a Blueprint! Try upgrading a Weapon with this.")
                elif item.armor == "armor":
                    print("\n"+str(item.name) + " --> Defense: " + str(m.trunc(item.armor_defense)) + " || Weight: " + str(m.trunc(item.weight)))
            except IndexError:
                print("That is not a valid number")
                show()
    else:
        print("There is nothing to inspect in your inventory")

def inventory_eq_call():
    Player.inventory_eq.clear()
    Player.inventory_eq.insert(0, Player.eq_head)
    Player.inventory_eq.insert(1, Player.eq_body)
    Player.inventory_eq.insert(2, Player.eq_hands)
    Player.inventory_eq.insert(3, Player.eq_legs)
    Player.inventory_eq.insert(4, Player.eq_weapon1)
    Player.inventory_eq.insert(5, Player.eq_weapon2)

def tier_plus():  # NEEDS TO BE ADDED and FIXED !!!!!!!!!!!!!!!!!!!!!!!!!!
    pass
    # if Player.eq_weapon1.name == Blueprints.equipment_name and Player.eq_weapon1.tier != 1:
    # Player.eq_weapon1.tier = Blueprints.bp_tier

def heal():
    if Player.cur_health == Player.max_health:
        print("\033[0;31mYou are already max health")
    elif Player.cur_health < Player.max_health and Player.flask.quanity != 0:
        print("\n\033[0;31m Health was " + str(m.trunc(Player.cur_health)) + "/" + str(m.trunc(Player.max_health)))
        Player.cur_health += Player.flask.health_buff
        Player.flask.quanity -= 1
        if Player.cur_health > Player.max_health:
            Player.cur_health = Player.max_health
        print("\033[0;34m Health is now: " + str(m.trunc(Player.cur_health)) + "/" + str(m.trunc(Player.max_health)) + "\n")
    elif Player.flask.quanity == 0:
        print("You are out of flasks!!!")



    pickle.dump(Player, open("Save.txt", "wb"))

def level_up_stats():
    print(
        "\033[0;34m" + str(Player.player_name) + "\nLevel: " + str(Player.level),
        "\n   Vitality     : " + str(Player.vitality),
        "\n   Resistance   : " + str(Player.resistance),
        "\n   Strength     : " + str(Player.strength),
        "\n   Intelligence : " + str(Player.intelligence) + "\n")

def level_up():
    print("\033[0;32m\nLEVEL UP!!!")
    level_up_stats()
    level_up_input = None
    level_up_choices = ("vitality", "resistance", "strength", "intelligence")
    yes_no_choices = ("yes", "no")
    yes_no = None

    strength_lvlup = (Player.strength + 1)
    max_weight_lvlup = (50 + ((Player.strength + 1) * 1.2))
    damage_lvlup = ((((Player.strength + 1) * .26) * Player.eq_weapon1.attack) + (Player.eq_weapon2.attack * 0.5))

    resistance_lvlup = ((Player.eq_head.armor_defense + Player.eq_body.armor_defense + Player.eq_hands.armor_defense +Player.eq_legs.armor_defense) * ((Player.resistance + 1) * 2.2)) + (Player.eq_weapon1.block + Player.eq_weapon2.block)
    health_lvlup = (100 + ((Player.vitality + 1) * 13))
    while level_up_input not in level_up_choices:
        level_up_input = input("\033[0;35mWhat would you like to level up?: ").lower()

    if level_up_input == "vitality":
        if Player.vitality <= 99:
            print("\033[0;34mVitality: " + str(Player.vitality) + " -> \033[0;32m" + str(Player.vitality + 1),
                  "\n\033[0;34mHealth: " + str(Player.max_health) + " -> \033[0;32m" + str(health_lvlup))
            while yes_no not in yes_no_choices:
                yes_no = input("\033[0;35mAre you sure?: ")
                if yes_no == "yes":
                    Player.vitality += 1
                    Player.level += 1
                    print()
                    break
                elif yes_no == "no":
                    break
                else:
                    continue
        else:
            print("Vitality is already MAX LEVEL")
            level_up()

    elif level_up_input == "resistance":
        if Player.resistance <= 99:
            print("\033[0;34mResistance: " + str(Player.resistance) + " -> \033[0;32m" + str((Player.resistance + 1)),
                "\n\033[0;34mDefence: " + str(m.trunc(Player.defense)) + " -> \033[0;32m" + str(m.trunc(resistance_lvlup)))
            while yes_no not in yes_no_choices:
                yes_no = input("\033[0;35mAre you sure?: ")
                if yes_no == "yes":
                    Player.resistance += 1
                    Player.level += 1
                    print()
                else:
                    level_up()
        else:
            print("Resistance is already MAX LEVEL")
            level_up()

    elif level_up_input == "strength":
        if Player.strength <= 99:
            print("\033[0;34mStrength: " + str(m.trunc(Player.strength)) + " -> \033[0;32m" + str(strength_lvlup),
                  "\n\033[0;34mDamage: " + str(m.trunc(Player.damage)) + " -> \033[0;32m" + str(m.trunc(damage_lvlup)),
                  "\n\033[0;34mMax Weight: " + str(m.trunc(Player.max_weight)) + " -> \033[0;32m" + str(m.trunc(max_weight_lvlup)))
            while yes_no not in yes_no_choices:
                yes_no = input("\033[0;35mAre you sure?: ")
                if yes_no == "yes":
                    Player.strength += 1
                    Player.level += 1
                    print()
                else:
                    level_up()
        else:
            print("Strength is already MAX LEVEL")
            level_up()

    elif level_up_input == "intelligence":
        if Player.intelligence <= 99:
            print("\033[0;34mIntelligence " + str(Player.intelligence) + " -> \033[0;32m" + str(Player.intelligence + 1))
            while yes_no not in yes_no_choices:
                yes_no = input("\033[0;35mAre you sure?: ")
                if yes_no == "yes":
                    Player.intelligence += 1
                    Player.level += 1
                    print()
                else:
                    level_up()
        else:
            print("Vitality is already MAX LEVEL")
            level_up()

    player_att_call()

def level_up_run():

    Player.xp_req = ((.02 * ((Player.level + 1) * (Player.level + 1) * (Player.level + 1))) + (
            3.06 * ((Player.level + 1) * (Player.level + 1))) + (105 + Player.level + 1))

    if Player.xp_req <= Player.xp:
        Player.xp -= Player.xp_req
        level_up()

    elif Player.xp_req >= Player.xp:

        print("\n\033[0;31mNot enough XP",
        "\n\033[0;34mPlayer XP: " + str(Player.xp),
        "\n\033[0;34mXP Required: " + str(Player.xp_req) + "\n")

def call_spawn_chance():
    spawn_chance = (100 - Player.player_spawn_chance)
    if spawn_chance < 100:
        random_spawn_chance = random.randint(1, spawn_chance)
        print(str(random_spawn_chance))
        if random_spawn_chance == 1:
            enemy_att_call()
        elif random_spawn_chance != 1:
            pass

def player_move():
    direction_choices = ("north", "west", "south", "east")
    direction = None

    while direction not in direction_choices:
        direction = input("\033[0;35mWhich way would you like to move? ").lower()

    if direction == "north":
        Player.player_spawn_chance += 11
        print("\033[0;34mYou went North")
        print(str(Player.player_spawn_chance) + "%")
        call_spawn_chance()

    elif direction == "west":
        Player.player_spawn_chance += 11
        print("\033[0;34mYou went West")
        call_spawn_chance()

    elif direction == "south":
        Player.player_spawn_chance += 11
        print("\033[0;34mYou went South")
        call_spawn_chance()

    elif direction == "east":
        Player.player_spawn_chance += 11
        print("\033[0;34mYou went East")
        call_spawn_chance()

def run_call():
    run_number = random.randint(1, 90)
    enemy_number = random.randint(10, 100)

    print("Your Number:: " + str(run_number))
    print("not Number:: " + str(enemy_number))
    print(str(Player.run_attempts))
    if run_number < enemy_number or Player.run_attempts > 2:
        print("\033[0;34mYou \033[0;31mfailed \033[0;34mto ran away!!!")
        attacked_call()
    elif run_number >= enemy_number:
        print("\033[0;34mYou \033[0;32msuccessfully \033[0;34mran away!!!")

def attack_call():
    Enemy.cur_health -= Player.true_damage
    print("\n\033[0;33m=========================================================================================="),
    print("\033[0;34mYou HIT " + str(Enemy.mob_name) + " for: " + str(m.trunc(Player.true_damage)) + " Damage!")
    if Enemy.cur_health <= 0:
        print(str(Enemy.mob_name) + " was killed")
        enemy_drops()
        print(str(m.trunc(Enemy.xp)) + " XP Gained\n")
        Player.xp += Enemy.xp
    else:
        attacked_call()
        fight()

def attacked_call():
    Player.cur_health -= Enemy.true_damage
    print("\033[0;31m" + str(Enemy.mob_name) + " HIT you for " + str(m.trunc(Enemy.true_damage)) + " Damage",
          "\n\033[0;33m==========================================================================================")
    if Player.cur_health <= 0:
        print("YOU DIED")
        from Dark_Text import load
        load()
    else:
        fight()

def parry_call():
    Enemy.cur_health -= Player.damage
    if Enemy.cur_health <= 0:
        print(str(Enemy.mob_name) + " was killed")
        enemy_drops()
        print(str(m.trunc(Enemy.xp)) + " XP Gained")
        Player.xp += Enemy.xp
        pickle.dump(Player, open("Save.txt", "wb"))
        from Dark_Text import load
        load()
    else:
        fight()

def fight():
    fight_prompt_choices = ("attack", "run", "parry")
    fight_prompt = None
    print("\n\033[0;37mCommands: " + str(fight_prompt_choices))
    print("\033[0;33m==========================================================================================",
        "\n\033[0;31m" + str(Enemy.mob_name) + " | Lvl: " + str(Enemy.level),
        ("\nHealth: " + str(m.trunc(Enemy.cur_health))),
        "\nDamage: " + str(m.trunc(Enemy.damage)) + " | Defense: " + str(m.trunc(Enemy.defense)),
        "\n\033[0;33m==========================================================================================",
        "\n\033[0;34m" + str(Player.player_name) + " | Lvl: " + str(m.trunc(Player.level)),
        "\n\033[0;34mHealth: " + str(m.trunc(Player.cur_health)),
        "\nDamage: " + str(m.trunc(Player.damage)) + " | Defense: " + str(m.trunc(Player.defense)),
        "\n\033[0;33m==========================================================================================\n")

    while fight_prompt not in fight_prompt_choices:


        fight_prompt = input("Enter Command: ").lower()

    if fight_prompt == "attack":
        attack_call()
    elif fight_prompt == "run":
        Player.run_attempts += 1
        run_call()
    elif fight_prompt == "parry":
        chance_test = random.randint(1, 2)
        if chance_test <= Player.attack_chance:
            print("\n\033[0;33m==========================================================================================")
            print("\033[0;34mYou waited for " + str(Enemy.mob_name) + " to attack to counter and \033[0;32msucceeded!")
            print("\033[0;34mYou HIT " + str(Enemy.mob_name) + " for: " + str(m.trunc(Player.damage)) + " Damage!")
            parry_call()
        elif chance_test > Player.attack_chance:
            print("\n\033[0;33m==========================================================================================")
            print("\033[0;34mYou waited for " + str(Enemy.mob_name) + " to attack to counter and \033[0;31mfailed!")
            attacked_call()

def rest():
    Player.cur_health = Player.max_health
    Player.flask.quanity = Player.flask.max_quanity
    pickle.dump(Player, open("Save.txt", "wb"))
    rest_options = ("leave", "level up", "upgrade")
    rest_prompt = None
    while rest_prompt not in rest_options:
        rest_prompt = input("\033[34;1mWhat would you like to do? ")
        if rest_prompt == "leave":
            print("\033[33;3mYou got up from the fire.")
            from Dark_Text import Player_Command
            Player_Command()
        elif rest_prompt == "level up":
            level_up_run()
            rest()
        elif rest_prompt == "upgrade":
            upgrade()
            rest()
        elif rest_prompt == "stats":
            stats_show()
            rest()
        elif rest_prompt == "unequip":
            unequip()
            rest()
        elif rest_prompt == "equip":
            equip()
            rest()
        elif rest_prompt == "inspect":
            show()
            rest()

def upgrade():
    Player.inventory.append(Player.flask)
    i = -1
    l = -1
    print()
    for x in Player.inventory:
        i += 1
        b = 0

        if x.type == "weapon" or x.type == "flask":
            print("\033[0m\033[33;1m" + str(i) + ". " + str(x.name))
        elif x.type == "blueprint":
            print("\033[0;31m" + str(i) + ". \033[31;9m" + str(x.name) + "\033[0;0m")
        else:
            print("\033[0;31m" + str(i) + ". \033[31;9m" + str(x.name) + "\033[0;0m")
    print()

    upg_item = 9091
    while upg_item == 9091:
        try:
            upg_item = int(input("\033[35;1mWhat item would you like to upgrade? "))
        except ValueError:
            print("\033[35;1mThat is not a number\033[0;0m")

        for z in Player.inventory:
            l += 1
            if hasattr(z, "equipment_name"):
                print("\033[33;1m" + str(l) + ". " + str(z.name) + "\033[0;0m")
            else:
                print("\033[0;0m" + str(l) + ". \033[0;9m" + str(z.name) + "\033[0;0m")
        try:
            bp = (int(input("\033[35;1mWhat Blueprint are you going to use? \033[0;0m")))
            try:

                if Player.inventory[upg_item].name == "Health Flask" and Player.inventory[bp].equipment_name == "Health Flask":
                    if Player.flask.tier != 7:
                        Player.flask.tier += 1
                        if Player.flask.tier == 1:
                            Player.flask.health_buff = 400
                        elif Player.flask.tier == 2:
                            Player.flask.health_buff = 500
                        elif Player.flask.tier == 3:
                            Player.flask.health_buff = 600
                        elif Player.flask.tier == 4:
                            Player.flask.health_buff = 650
                        elif Player.flask.tier == 5:
                            Player.flask.health_buff = 700
                        elif Player.flask.tier == 6:
                            Player.flask.health_buff = 750
                        elif Player.flask.tier == 7:
                            Player.flask.health_buff = 800
                    Player.inventory.pop(bp)
                elif Player.inventory[upg_item].name == "Health Flask" and Player.inventory[bp].equipment_name != "Health Flask":
                    print("You cannot upgrade your flask with " + str(Player.inventory[bp].name))




                elif Player.inventory[bp].equipment_name == Player.inventory[upg_item].name and Player.inventory[bp].tier_req == Player.inventory[upg_item].tier:
                    upgrade_prompt_choices = ("yes", "no")
                    upgrade_prompt = None

                    if hasattr(upg_item, "attack"):
                        while upgrade_prompt not in upgrade_prompt_choices:
                            print("\033[34;1mAttack : " + str(Player.inventory[upg_item].attack) + "\033[32;1m --> \033[33;1m" + str(m.trunc(Player.inventory[upg_item].attack * Player.inventory[bp].tier)) + "\n" +
                                  "\033[34;1mBlock  : " + str(Player.inventory[upg_item].block) + "\033[32;1m --> \033[33;1m" + str(m.trunc(Player.inventory[upg_item].block * Player.inventory[bp].tier)))
                            upgrade_prompt = input("\033[35;1mAre you sure? \033[0;0m")
                            if upgrade_prompt == "yes":
                                Player.inventory[upg_item].attack = (Player.inventory[upg_item].attack * Player.inventory[bp].tier)
                                Player.inventory[upg_item].block = (Player.inventory[upg_item].block * Player.inventory[bp].tier)
                                Player.inventory[upg_item].tier += 1
                                player_att_call()
                                Player.inventory.pop(bp)
                            else:
                                continue
                    else:
                        pass
                elif Player.inventory[bp].equipment_name == Player.inventory[upg_item].name and Player.inventory[bp].tier_req != Player.inventory[upg_item].tier:
                    print("\033[31;1m" + str(Player.inventory[upg_item].name) + "'s Tier is too great for this blueprint to do anything\033[0;0m")
                    rest()
            except ValueError:
                Player.inventory.pop(-1)
                print("\033[31;1mThat was not a blueprint; You put everything back to reassess\033[0;0m")
                rest()
        except ValueError:
            Player.inventory.pop(-1)
            print("\033[31;1mThat is not a number\033[0;0m")
            rest()
    Player.inventory.pop(-1)

class ClassAttributes:
    enemy_list = []
    inventory = []
    inventory_eq = []
    ground_items = []

    def __init__(self, character, vitality, resistance, strength, intelligence, crafting,
                 eq_weapon1, eq_weapon2, eq_head, eq_body, eq_hands, eq_legs, player_name, damage, defense,
                 level, xp, max_weight, cur_weight, weight_percentage, total_attack, attack_chance,
                 player_spawn_chance, mob_name, max_health, cur_health, crit_damage, crit_block, true_damage,
                 xp_req, run_attempts, inventory_eq, ground_items, inventory, flask):
        self.character = character
        self.vitality = vitality
        self.resistance = resistance
        self.strength = strength
        self.intelligence = intelligence
        self.crafting = crafting
        self.eq_weapon1 = eq_weapon1
        self.eq_weapon2 = eq_weapon2
        self.eq_head = eq_head
        self.eq_body = eq_body
        self.eq_hands = eq_hands
        self.eq_legs = eq_legs
        self.player_name = player_name
        self.damage = damage
        self.defense = defense
        self.level = level + 10
        self.xp = xp
        self.max_weight = max_weight
        self.cur_weight = cur_weight
        self.weight_percentage = weight_percentage
        self.total_attack = total_attack
        self.attack_chance = attack_chance
        self.player_spawn_chance = player_spawn_chance
        self.mob_name = mob_name
        self.max_health = max_health
        self.cur_health = cur_health
        self.crit_damage = crit_damage
        self.crit_block = crit_block
        self.true_damage = true_damage
        self.xp_req = xp_req
        self.run_attempts = run_attempts
        self.inventory = inventory
        self.inventory_eq = inventory_eq
        self.__class__.enemy_list.append(self)
        self.ground_items = ground_items
        self.flask = flask

class WeaponAttributes:
    def __init__(self, handed, name, attack, block, critical_damage,
                 critical_block, str_req, int_req, weight, tier, type):
        self.handed = handed
        self.name = name
        self.attack = attack
        self.block = block
        self.critical_damage = critical_damage
        self.critical_block = critical_block
        self.str_req = str_req
        self.int_req = int_req
        self.weight = weight
        self.tier = tier
        self.type = type #Identity

class ArmorAttributes:
    def __init__(self, type, name, armor_defense, weight, armor):
        self.name = name
        self.type = type
        self.armor_defense = armor_defense
        self.weight = weight
        self.armor = armor #Identity

class Objects:

    class HealthFlask:
        def __init__(self, health_buff, quanity, max_quanity, tier, name, type):
            self.health_buff = health_buff
            self.quanity = quanity
            self.max_quanity = max_quanity
            self.tier = tier
            self.name = name
            self.type = type
    health_flask = HealthFlask(300, 2, 2, 0, "Health Flask", "flask")

class Weapons(WeaponAttributes):
    none_weapon = WeaponAttributes("one-handed", "none", 0, 0, 0, 0, 0, 0, 0, 0, "weapon")
    # Daggers(one-handed)
    dagger = WeaponAttributes("one-handed", "Dagger", 74, 35, 1.3, 35, 5, 0, 1.5, 0, "weapon")
    misericorde = WeaponAttributes("one-handed", "Misericorde", 92, 36, 1.4, 15, 7, 0, 2, 0, "weapon")
    great_knife = WeaponAttributes("one-handed", "Great Knife", 75, 35, 1.1, 15, 6, 0, 1.5, 0, "weapon")
    blood_stained_knife = WeaponAttributes("one-handed", "Blood-Stained Dagger", 81, 36, 1.1, 15, 9, 0, 2, 0, "weapon")
    wakizashi = WeaponAttributes("one-handed", "Wakizashi", 94, 42, 1, 18, 9, 0, 3, 0, "weapon")
    # Swords(one-handed)
    short_sword = WeaponAttributes("one-handed", "Short Sword", 102, 45, 1, 28, 8, 0, 3, 0, "weapon")
    long_sword = WeaponAttributes("one-handed", "Long Sword", 110, 45, 1, 30, 10, 0, 3.5, 0, "weapon")
    broad_sword = WeaponAttributes("one-handed", "Broad Sword", 117, 47, 1, 31, 10, 0, 4, 0, "weapon")
    weathered_straight_sword = WeaponAttributes("one-handed", "Weathered Straight Sword", 103, 43, 1, 27, 7, 0, 3, 0, "weapon")
    straight_sword = WeaponAttributes("one-handed", "Straight Sword", 115, 45, 1.1, 30, 10, 0, 3.5, 0, "weapon")
    slender_sword = WeaponAttributes("one-handed", "Slender Sword", 101, 43, 1.1, 30, 8, 0, 3, 0, "weapon")
    crystal_sword = WeaponAttributes("one-handed", "Crystal Sword", 106, 44, 1, 33, 13, 15, 4.5, 0, "weapon")
    demon_sword = WeaponAttributes("one-handed", "Demon Sword", 120, 49, 1.2, 35, 17, 20, 4, 0, "weapon")
    # Great Swords (two-handed)
    bastard_sword = WeaponAttributes("two-handed", "Bastard Sword", 138, 65, 1, 42, 16, 0, 9, 0, "weapon")
    claymore = WeaponAttributes("two-handed", "Claymore", 138, 65, 1, 42, 16, 0, 9, 0, "weapon")
    iron_greatsword = WeaponAttributes("two-handed", "Iron Greatsword", 149, 73, 1, 47, 18, 0, 12, 0, "weapon")
    knights_greatsword = WeaponAttributes("two-handed", "Knights Greatsword", 141, 68, 1, 44, 16, 0, 10, 0, "weapon")
    banished_knights_greatsword = WeaponAttributes("two-handed", "Banished Knights Greatsword", 142, 68, 1, 44, 17, 0, 10, 0, "weapon")
    flamberge = WeaponAttributes("two-handed", "Flamberge", 129, 65, 1, 42, 15, 0, 12, 0, "weapon")
    demon_greatsword = WeaponAttributes("two-handed", "Demon Greatsword", 160, 80, 1, 52, 20, 15, 13, 0, "weapon")
    # Axes (one-handed)
    hand_axe = WeaponAttributes("one-handed", "Hand Axe", 113, 42, 1, 28, 9, 0, 3.5, 0, "weapon")
    battle_axe = WeaponAttributes("one-handed", "Battle Axe", 123, 47, 1, 28, 12, 0, 2.5, 0, "weapon")
    warped_axe = WeaponAttributes("one-handed", "Warped Axe", 118, 56, 1, 43, 24, 0, 5.5, 0, "weapon")
    stormhawk_axe = WeaponAttributes("one-handed", "Stormhawk Axe", 130, 49, 1, 28, 19, 0, 5.5, 0, "weapon")
    # Great Axes (two-handed)
    great_axe = WeaponAttributes("two-handed", "Great Axe", 151, 69, 1, 28, 30, 0, 13, 0, "weapon")
    executioners_great_axe = WeaponAttributes("two-handed", "Executioners Great Axe", 150, 74, 1.15, 48, 34, 0, 15, 0, "weapon")
    demon_great_axe = WeaponAttributes("two-handed", "Demon Great Axe", 152, 80, 1.3, 35, 38, 15, 13, 0, "weapon")
    # Bows (two-handed)
    longbow = WeaponAttributes("two-handed", "Longbow", 80, 30, 1, 0, 9, 0, 4, 0, "weapon")
    pulley_bow = WeaponAttributes("two-handed", "Pulley Bow", 77, 40, 1, 0, 11, 0, 3.5, 0, "weapon")
    # Great Bows (two-handed)
    greatbow = WeaponAttributes("two-handed", "Greatbow", 125, 60, 1, 0, 20, 0, 10, 0, "weapon")
    demon_greatbow = WeaponAttributes("two-handed", "Demon Greatbow", 135, 75, 1, 0, 25, 15, 12, 0, "weapon")
    # Crossbows (two-handed)
    crossbow = WeaponAttributes("two-handed", "Crossbow", 54, 35, 1, 0, 10, 0, 3.5, 0, "weapon")
    heavy_crossbow = WeaponAttributes("two-handed", "Heavy Crossbow", 64, 45, 1, 0, 14, 0, 5.5, 0, "weapon")

class Armor(ArmorAttributes):
    none_armor_head = ArmorAttributes("head", "none", 0, 0, "none")
    none_armor_body = ArmorAttributes("body", "none", 0, 0, "none")
    none_armor_hands = ArmorAttributes("hands", "none", 0, 0, "none")
    none_armor_legs = ArmorAttributes("legs", "none", 0, 0, "none")
    # All-Knowing Set
    all_knowing_helmet = ArmorAttributes("head", "All-Knowing Helmet", 4.6, 4.6, "armor")
    all_knowing_armor = ArmorAttributes("body", "All-Knowing Armor", 12.9, 10.7, "armor")
    all_knowing_gauntlets = ArmorAttributes("hands", "All-Knowing Gauntlets", 3.2, 3.5, "armor")
    all_knowing_greaves = ArmorAttributes("legs", "All-Knowing Greaves", 7.4, 6.6, "armor")
    # Aristocrat set
    aristocrat_headband = ArmorAttributes("head", "Aristocrat Headband", 1.9, 1.2, "armor")
    aristocrat_garb = ArmorAttributes("body", "Aristocrat Garb", 7.8, 4.9, "armor")
    aristocrat_boots = ArmorAttributes("legs", "Aristocrat Boots", 4.3, 2.9, "armor")
    # Banished Knight set
    banished_knight_helmet = ArmorAttributes("head", "Banished Knight Helmet", 6.8, 7.5, "armor")
    banished_knight_armor = ArmorAttributes("body", "Banished Knight Armor", 18.7, 17.6, "armor")
    banished_knight_gauntlets = ArmorAttributes("hands", "Banished Knight Gauntlets", 4.7, 5.8, "armor")
    banished_knight_greaves = ArmorAttributes("legs", "Banished Knight Greaves", 10.8, 10.8, "armor")
    # Bandit set
    bandit_mask = ArmorAttributes("head", "Bandit Mask", 2.8, 3.0, "armor")
    bandit_garb = ArmorAttributes("body", "Bandit Garb", 8.0, 7.7, "armor")
    bandit_manchettes = ArmorAttributes("hands", "Bandit Manchettes", 1.5, 4.4, "armor")
    bandit_boots = ArmorAttributes("legs", "Bandit Boots", 4.0, 4.6, "armor")
    # Bloodhound knight set
    bloodhound_knight_helm = ArmorAttributes("helmet", "Bloodhound Knight Helm", 4.4, 4.6, "armor")
    bloodhound_knight_armor = ArmorAttributes("body", "Bloodhound Knight Armor", 12.4, 10.6, "armor")
    bloodhound_knight_gauntlets = ArmorAttributes("hands", "Bloodhound Knight Gauntlets", 3.1, 3.5, "armor")
    bloodhound_knight_greaves = ArmorAttributes("legs", "Bloodhound Knight Greaves", 7.1, 6.6, "armor")
    # Chain set
    chain_coif = ArmorAttributes("head", "Chain Coif", 4.2, 3.8, "armor")
    chain_armor = ArmorAttributes("body", "Chain Armor", 11.9, 8.8, "armor")
    chain_gauntlets = ArmorAttributes("hands", "Chain Gauntlets", 2.9, 2.9, "armor")
    chain_leggings = ArmorAttributes("legs", "Chain Leggings", 6.8, 5.5, "armor")
    # Commoners set
    commoners_headband = ArmorAttributes("head", "Commoner's Headband", 0.9, 1.4, "armor")
    commoners_garb = ArmorAttributes("body", "Commoner's Garb", 5.3, 5.1, "armor")
    commoners_shoes = ArmorAttributes("legs", "Commoner's Shoes", 1.5, 2.0, "armor")
    # Fingerprint set
    fingerprint_helm = ArmorAttributes("head", "Fingerprint Helmet", 4.8, 4.6, "armor")
    fingerprint_armor = ArmorAttributes("body", "Fingerprint Armor", 13.5, 10.6, "armor")
    fingerprint_gauntlets = ArmorAttributes("hands", "Fingerprint Gauntlets", 3.3, 3.5, "armor")
    fingerprint_greaves = ArmorAttributes("legs", "Fingerprint Greaves", 7.7, 6.6, "armor")
    # Leather set
    leather_hood = ArmorAttributes("head", "Leather Hood", 2.8, 3, "armor")
    leather_armor = ArmorAttributes("body", "Leather Armor", 8.0, 7.1, "armor")
    leather_gloves = ArmorAttributes("hands", "Leather Gloves", 1.9, 4.4, "armor")
    leather_boots = ArmorAttributes("legs", "Leather Boots", 4.5, 4.4, "armor")
    # Knight set
    knight_helmet = ArmorAttributes("head", "Knight Helmet", 4.4, 4.6, "armor")
    knight_armor = ArmorAttributes("body", "Knight Armor", 12.4, 10.6, "armor")
    knight_gauntlets = ArmorAttributes("hands", "Knight Gauntlets", 3.1, 3.5, "armor")
    knight_greaves = ArmorAttributes("legs", "Knight Greaves", 7.1, 6.6, "armor")
    # Noble set
    noble_hood = ArmorAttributes("head", "Noble Hood", 1.8, 1.4, "armor")
    noble_garb = ArmorAttributes("body", "Noble Garb", 6.7, 5.1, "armor")
    noble_trousers = ArmorAttributes("legs", "Noble Trousers", 3.4, 2.5, "armor")
    # Prisoner set
    prisoner_shirt = ArmorAttributes("body", "Prisoner Shirt", 4.2, 3.2, "armor")
    prisoner_trousers = ArmorAttributes("legs", "Prisoner Trousers", 2.3, 2.0, "armor")

class PlayerClass(ClassAttributes, Weapons, Armor):
    warrior = ClassAttributes("WARRIOR", 8, 12, 12, 4, 0, Weapons.short_sword, Weapons.none_weapon, Armor.commoners_headband,
                              Armor.commoners_garb, Armor.none_armor_hands, Armor.commoners_shoes,
                              "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 0, 0, 0, 0, 0, 0, 0, [], [], [], Objects.health_flask)

    outcast = ClassAttributes("OUTCAST", 8, 8, 8, 8, 0, Weapons.dagger, Weapons.none_weapon, Armor.none_armor_head,
                              Armor.prisoner_shirt, Armor.none_armor_hands, Armor.prisoner_trousers,
                              "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 0, 0, 0, 0, 0, 0, 0, [], [], [], Objects.health_flask)

    rogue = ClassAttributes("ROGUE", 8, 10, 10, 10, 0, Weapons.dagger, Weapons.dagger, Armor.none_armor_head, Armor.prisoner_shirt,
                            Armor.prisoner_trousers, Armor.none_armor_legs,
                            "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 0, 0, 0, 0, 0, 0, 0, [], [], [], Objects.health_flask)

    hunter = ClassAttributes("HUNTER", 8, 9, 8, 12, 0, Weapons.longbow, Weapons.none_weapon, Armor.leather_hood,
                             Armor.leather_armor, Armor.leather_gloves, Armor.leather_boots,
                             "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 0, 0, 0, 0, 0, 0, 0, [], [], [], Objects.health_flask)

class BlueprintAttributes:
    def __init__(self, name, equipment_name, tier, int_req, tier_req, type):
        self.name = name
        self.equipment_name = equipment_name
        self.tier = tier
        self.int_req = int_req
        self.tier_req = tier_req
        self.type = type

class Blueprints(BlueprintAttributes):
    dagger_t1 = BlueprintAttributes("Dagger Tier 1 Blueprint", "Dagger", 1.1, 15, 0, "blueprint")
    dagger_t2 = BlueprintAttributes("Dagger Tier 2 Blueprint", "Dagger", 1.15, 20, 1, "blueprint")
    dagger_t3 = BlueprintAttributes("Dagger Tier 3 Blueprint", "Dagger", 1.25, 35, 2, "blueprint")
    misericorde_t1 = BlueprintAttributes("Misericorde Tier 1 Blueprint", "Misericorde", 1.1, 15, 0, "blueprint")
    misericorde_t2 = BlueprintAttributes("Misericorde Tier 2 Blueprint", "Misericorde", 1.15, 20, 1, "blueprint")
    misericorde_t3 = BlueprintAttributes("Misericorde Tier 3 Blueprint", "Misericorde", 1.25, 35, 2, "blueprint")
    great_knife_t1 = BlueprintAttributes("Great Knife Tier 1 Blueprint", "Great Knife", 1.1, 15, 0, "blueprint")
    great_knife_t2 = BlueprintAttributes("Great Knife Tier 2 Blueprint", "Great Knife", 1.15, 20, 1, "blueprint")
    great_knife_t3 = BlueprintAttributes("Great Knife Tier 3 Blueprint", "Great Knife", 1.25, 35, 2, "blueprint")
    blood_stained_knife_t1 = BlueprintAttributes("Blood Stained Knife Tier 1 Blueprint", "Blood Stained Knife", 1.1, 15, 0, "blueprint")
    blood_stained_knife_t2 = BlueprintAttributes("Blood Stained Knife Tier 2 Blueprint", "Blood Stained Knife", 1.15, 20, 1, "blueprint")
    blood_stained_knife_t3 = BlueprintAttributes("Blood Stained Knife Tier 3 Blueprint", "Blood Stained Knife", 1.25, 35, 2, "blueprint")
    wakizashi_t1 = BlueprintAttributes("Wakizashi Tier 1 Blueprint", "Wakizashi", 1.1, 15, 0, "blueprint")
    wakizashi_t2 = BlueprintAttributes("Wakizashi Tier 2 Blueprint", "Wakizashi", 1.15, 20, 1, "blueprint")
    wakizashi_t3 = BlueprintAttributes("Wakizashi Tier 3 Blueprint", "Wakizashi", 1.25, 35, 2, "blueprint")
    short_sword_t1 = BlueprintAttributes("Short Sword Tier 1 Blueprint", "Short Sword", 1.1, 15, 0, "blueprint")
    short_sword_t2 = BlueprintAttributes("Short Sword Tier 2 Blueprint", "Short Sword", 1.15, 20, 1, "blueprint")
    short_sword_t3 = BlueprintAttributes("Short Sword Tier 3 Blueprint", "Short Sword", 1.25, 35, 2, "blueprint")
    long_sword_t1 = BlueprintAttributes("Long Sword Tier 1 Blueprint", "Long Sword", 1.1, 15, 0, "blueprint")
    long_sword_t2 = BlueprintAttributes("Long Sword Tier 2 Blueprint", "Long Sword", 1.15, 20, 1, "blueprint")
    long_sword_t3 = BlueprintAttributes("Long Sword Tier 3 Blueprint", "Long Sword", 1.25, 35, 2, "blueprint")
    broad_sword_t1 = BlueprintAttributes("Broad Sword Tier 1 Blueprint", "Broad Sword", 1.1, 15, 0, "blueprint")
    broad_sword_t2 = BlueprintAttributes("Broad Sword Tier 2 Blueprint", "Broad Sword", 1.15, 20, 1, "blueprint")
    broad_sword_t3 = BlueprintAttributes("Broad Sword Tier 3 Blueprint", "Broad Sword", 1.25, 35, 2, "blueprint")
    weathered_straight_sword_t1 = BlueprintAttributes("Weathered Straight Sword Tier 1 Blueprint", "Weathered Straight Sword", 1.1, 15, 0, "blueprint")
    weathered_straight_sword_t2 = BlueprintAttributes("Weathered Straight Sword Tier 2 Blueprint", "Weathered Straight Sword", 1.15, 20, 1, "blueprint")
    weathered_straight_sword_t3 = BlueprintAttributes("Weathered Straight Sword Tier 3 Blueprint", "Weathered Straight Sword", 1.25, 35, 2, "blueprint")
    straight_sword_t1 = BlueprintAttributes("Straight Sword Tier 1 Blueprint", "Straight Sword", 1.1, 15, 0, "blueprint")
    straight_sword_t2 = BlueprintAttributes("Straight Sword Tier 2 Blueprint", "Straight Sword", 1.15, 20, 1, "blueprint")
    straight_sword_t3 = BlueprintAttributes("Straight Sword Tier 3 Blueprint", "Straight Sword", 1.25, 35, 2, "blueprint")
    slender_sword_t1 = BlueprintAttributes("Slender Sword Tier 1 Blueprint", "Slender Sword", 1.1, 15, 0, "blueprint")
    slender_sword_t2 = BlueprintAttributes("Slender Sword Tier 2 Blueprint", "Slender Sword", 1.15, 20, 1, "blueprint")
    slender_sword_t3 = BlueprintAttributes("Slender Sword Tier 3 Blueprint", "Slender Sword", 1.25, 35, 2, "blueprint")
    crystal_sword_t1 = BlueprintAttributes("Crystal Sword Tier 1 Blueprint", "Crystal Sword", 1.1, 15, 0, "blueprint")
    crystal_sword_t2 = BlueprintAttributes("Crystal Sword Tier 2 Blueprint", "Crystal Sword", 1.15, 20, 1, "blueprint")
    crystal_sword_t3 = BlueprintAttributes("Crystal Sword Tier 3 Blueprint", "Crystal Sword", 1.25, 35, 2, "blueprint")
    demon_sword_t1 = BlueprintAttributes("Demon Sword Tier 1 Blueprint", "Demon Sword", 1.1, 15, 0, "blueprint")
    demon_sword_t2 = BlueprintAttributes("Demon Sword Tier 2 Blueprint", "Demon Sword", 1.15, 20, 1, "blueprint")
    demon_sword_t3 = BlueprintAttributes("Demon Sword Tier 3 Blueprint", "Demon Sword", 1.25, 35, 2, "blueprint")
    bastard_sword_t1 = BlueprintAttributes("Bastard Sword Tier 1 Blueprint", "Bastard Sword", 1.1, 15, 0, "blueprint")
    bastard_sword_t2 = BlueprintAttributes("Bastard Sword Tier 2 Blueprint", "Bastard Sword", 1.15, 20, 1, "blueprint")
    bastard_sword_t3 = BlueprintAttributes("Bastard Sword Tier 3 Blueprint", "Bastard Sword", 1.25, 35, 2, "blueprint")
    claymore_t1 = BlueprintAttributes("Claymore Tier 1 Blueprint", "Claymore", 1.1, 15, 0, "blueprint")
    claymore_t2 = BlueprintAttributes("Claymore Tier 2 Blueprint", "Claymore", 1.15, 20, 1, "blueprint")
    claymore_t3 = BlueprintAttributes("Claymore Tier 3 Blueprint", "Claymore", 1.25, 35, 2, "blueprint")
    iron_greatsword_t1 = BlueprintAttributes("Iron Greatsword Tier 1 Blueprint", "Iron Greatsword", 1.1, 15, 0, "blueprint")
    iron_greatsword_t2 = BlueprintAttributes("Iron Greatsword Tier 2 Blueprint", "Iron Greatsword", 1.15, 20, 1, "blueprint")
    iron_greatsword_t3 = BlueprintAttributes("Iron Greatsword Tier 3 Blueprint", "Iron Greatsword", 1.25, 35, 2, "blueprint")
    knights_greatsword_t1 = BlueprintAttributes("Knights Greatsword Tier 1 Blueprint", "Knights Greatsword", 1.1, 15, 0, "blueprint")
    knights_greatsword_t2 = BlueprintAttributes("Knights Greatsword Tier 2 Blueprint", "Knights Greatsword", 1.15, 20, 1, "blueprint")
    knights_greatsword_t3 = BlueprintAttributes("Knights Greatsword Tier 3 Blueprint", "Knights Greatsword", 1.25, 35, 2, "blueprint")
    banished_knights_greatsword_t1 = BlueprintAttributes("Banished Knights Greatsword Tier 1 Blueprint", "Banished Knights Greatsword", 1.1, 15, 0, "blueprint")
    banished_knights_greatsword_t2 = BlueprintAttributes("Banished Knights Greatsword Tier 2 Blueprint", "Banished Knights Greatsword", 1.15, 20, 1, "blueprint")
    banished_knights_greatsword_t3 = BlueprintAttributes("Banished Knights Greatsword Tier 3 Blueprint", "Banished Knights Greatsword", 1.25, 35, 2, "blueprint")
    flamberge_t1 = BlueprintAttributes("Flamberge Tier 1 Blueprint", "Flamberge", 1.1, 15, 0, "blueprint")
    flamberge_t2 = BlueprintAttributes("Flamberge Tier 2 Blueprint", "Flamberge", 1.15, 20, 1, "blueprint")
    flamberge_t3 = BlueprintAttributes("Flamberge Tier 3 Blueprint", "Flamberge", 1.25, 35, 2, "blueprint")
    demon_greatsword_t1 = BlueprintAttributes("Demon Greatsword Tier 1 Blueprint", "Demon Greatsword", 1.1, 15, 0, "blueprint")
    demon_greatsword_t2 = BlueprintAttributes("Demon Greatsword Tier 2 Blueprint", "Demon Greatsword", 1.15, 20, 1, "blueprint")
    demon_greatsword_t3 = BlueprintAttributes("Demon Greatsword Tier 3 Blueprint", "Demon Greatsword", 1.25, 35, 2, "blueprint")
    hand_axe_t1 = BlueprintAttributes("Hand Axe Tier 1 Blueprint", "Hand Axe", 1.1, 15, 0, "blueprint")
    hand_axe_t2 = BlueprintAttributes("Hand Axe Tier 2 Blueprint", "Hand Axe", 1.15, 20, 1, "blueprint")
    hand_axe_t3 = BlueprintAttributes("Hand Axe Tier 3 Blueprint", "Hand Axe", 1.25, 35, 2, "blueprint")
    battle_axe_t1 = BlueprintAttributes("Battle Axe Tier 1 Blueprint", "Battle Axe", 1.1, 15, 0, "blueprint")
    battle_axe_t2 = BlueprintAttributes("Battle Axe Tier 2 Blueprint", "Battle Axe", 1.15, 20, 1, "blueprint")
    battle_axe_t3 = BlueprintAttributes("Battle Axe Tier 3 Blueprint", "Battle Axe", 1.25, 35, 2, "blueprint")
    warped_axe_t1 = BlueprintAttributes("Warped Axe Tier 1 Blueprint", "Warped Axe", 1.1, 15, 0, "blueprint")
    warped_axe_t2 = BlueprintAttributes("Warped Axe Tier 2 Blueprint", "Warped Axe", 1.15, 20, 1, "blueprint")
    warped_axe_t3 = BlueprintAttributes("Warped Axe Tier 3 Blueprint", "Warped Axe", 1.25, 35, 2, "blueprint")
    stormhawk_axe_t1 = BlueprintAttributes("Stormhawk Axe Tier 1 Blueprint", "Stormhawk Axe", 1.1, 15, 0, "blueprint")
    stormhawk_axe_t2 = BlueprintAttributes("Stormhawk Axe Tier 2 Blueprint", "Stormhawk Axe", 1.15, 20, 1, "blueprint")
    stormhawk_axe_t3 = BlueprintAttributes("Stormhawk Axe Tier 3 Blueprint", "Stormhawk Axe", 1.25, 35, 2, "blueprint")
    great_axe_t1 = BlueprintAttributes("Great Axe Tier 1 Blueprint", "Great Axe", 1.1, 15, 0, "blueprint")
    great_axe_t2 = BlueprintAttributes("Great Axe Tier 2 Blueprint", "Great Axe", 1.15, 20, 1, "blueprint")
    great_axe_t3 = BlueprintAttributes("Great Axe Tier 3 Blueprint", "Great Axe", 1.25, 35, 2, "blueprint")
    executioners_great_axe_t1 = BlueprintAttributes("Executioner's Great Axe Tier 1 Blueprint", "Executioner's Great Axe", 1.1, 15, 0, "blueprint")
    executioners_great_axe_t2 = BlueprintAttributes("Executioner's Great Axe Tier 2 Blueprint", "Executioner's Great Axe", 1.15, 20, 1, "blueprint")
    executioners_great_axe_t3 = BlueprintAttributes("Executioner's Great Axe Tier 3 Blueprint", "Executioner's Great Axe", 1.25, 35, 2, "blueprint")
    demon_great_axe_t1 = BlueprintAttributes("Demon Great Axe Tier 1 Blueprint", "Demon Great Axe", 1.1, 15, 0, "blueprint")
    demon_great_axe_t2 = BlueprintAttributes("Demon Great Axe Tier 2 Blueprint", "Demon Great Axe", 1.15, 20, 1, "blueprint")
    demon_great_axe_t3 = BlueprintAttributes("Demon Great Axe Tier 3 Blueprint", "Demon Great Axe", 1.25, 35, 2, "blueprint")
    longbow_t1 = BlueprintAttributes("Longbow Tier 1 Blueprint", "Longbow", 1.1, 15, 0, "blueprint")
    longbow_t2 = BlueprintAttributes("Longbow Tier 2 Blueprint", "Longbow", 1.15, 20, 1, "blueprint")
    longbow_t3 = BlueprintAttributes("Longbow Tier 3 Blueprint", "Longbow", 1.25, 35, 2, "blueprint")
    pulley_bow_t1 = BlueprintAttributes("Pulley Bow Tier 1 Blueprint", "Pulley Bow", 1.1, 15, 0, "blueprint")
    pulley_bow_t2 = BlueprintAttributes("Pulley Bow Tier 2 Blueprint", "Pulley Bow", 1.15, 20, 1, "blueprint")
    pulley_bow_t3 = BlueprintAttributes("Pulley Bow Tier 3 Blueprint", "Pulley Bow", 1.25, 35, 2, "blueprint")
    greatbow_t1 = BlueprintAttributes("Greatbow Tier 1 Blueprint", "Greatbow", 1.1, 15, 0, "blueprint")
    greatbow_t2 = BlueprintAttributes("Greatbow Tier 2 Blueprint", "Greatbow", 1.15, 20, 1, "blueprint")
    greatbow_t3 = BlueprintAttributes("Greatbow Tier 3 Blueprint", "Greatbow", 1.25, 35, 2, "blueprint")
    demon_greatbow_t1 = BlueprintAttributes("Demon Greatbow Tier 1 Blueprint", "Demon Greatbow", 1.1, 15, 0, "blueprint")
    demon_greatbow_t2 = BlueprintAttributes("Demon Greatbow Tier 2 Blueprint", "Demon Greatbow", 1.15, 20, 1, "blueprint")
    demon_greatbow_t3 = BlueprintAttributes("Demon Greatbow Tier 3 Blueprint", "Demon Greatbow", 1.25, 35, 2, "blueprint")
    crossbow_t1 = BlueprintAttributes("Crossbow Tier 1 Blueprint", "Crossbow", 1.1, 15, 0, "blueprint")
    crossbow_t2 = BlueprintAttributes("Crossbow Tier 2 Blueprint", "Crossbow", 1.15, 20, 1, "blueprint")
    crossbow_t3 = BlueprintAttributes("Crossbow Tier 3 Blueprint", "Crossbow", 1.25, 35, 2, "blueprint")
    heavy_crossbow_t1 = BlueprintAttributes("Heavy Crossbow Tier 1 Blueprint", "Heavy Crossbow", 1.1, 15, 0, "blueprint")
    heavy_crossbow_t2 = BlueprintAttributes("Heavy Crossbow Tier 2 Blueprint", "Heavy Crossbow", 1.15, 20, 1, "blueprint")
    heavy_crossbow_t3 = BlueprintAttributes("Heavy Crossbow Tier 3 Blueprint", "Heavy Crossbow", 1.25, 35, 2, "blueprint")
    health_flask_upgrade = BlueprintAttributes("Health Flask Upgrade", "Health Flask", 0, 0, 0, "blueprint")



    # 1

Player = ClassAttributes("", 0, 0, 0, 0, 0, Weapons.none_weapon, Weapons.none_weapon, Armor.none_armor_head,
                         Armor.none_armor_body, Armor.none_armor_hands, Armor.none_armor_legs,
                         "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 0, 0, 0, 0, 0, 0, 0, [], [], [], Objects.health_flask)

Enemy = ClassAttributes("", 0, 0, 0, 0, 0, Weapons.none_weapon, Weapons.none_weapon, Armor.none_armor_head,
                        Armor.none_armor_body, Armor.none_armor_hands, Armor.none_armor_legs,
                        "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", 0, 0, 0, 0, 0, 0, 0, [], [], [], Objects.health_flask)
    # 1
ClassAttributes("", 0, 0, 0, 0, 0, Weapons.great_knife, Weapons.none_weapon, Armor.none_armor_head,
                Armor.all_knowing_armor, Armor.none_armor_hands, Armor.all_knowing_greaves, "",
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "All Knowing Minion", 0, 0, 0, 0, 0, 0, 0, [], [], [], Objects.health_flask)

    # 2
ClassAttributes("", 0, 0, 0, 0, 0, Weapons.short_sword, Weapons.none_weapon, Armor.all_knowing_helmet,
                 Armor.all_knowing_armor, Armor.all_knowing_gauntlets, Armor.all_knowing_greaves, "",
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "All Knowing Soldier", 0, 0, 0, 0, 0, 0, 0, [], [], [], Objects.health_flask)
     # 3
ClassAttributes("", 0, 0, 0, 0, 0, Weapons.crossbow, Weapons.none_weapon, Armor.all_knowing_helmet,
                 Armor.all_knowing_armor, Armor.all_knowing_gauntlets, Armor.all_knowing_greaves, "",
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "All Knowing Ranger", 0, 0, 0, 0, 0, 0, 0, [], [], [], Objects.health_flask)
     # 4
ClassAttributes("", 0, 0, 0, 0, 0, Weapons.great_knife, Weapons.great_knife, Armor.all_knowing_helmet,
                 Armor.all_knowing_armor, Armor.all_knowing_gauntlets, Armor.all_knowing_greaves, "",
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "All Knowing Rogue", 0, 0, 0, 0, 0, 0, 0, [], [], [], Objects.health_flask)

