import Classesimport osimport pickleimport timec = ClassesPlayer_exists = os.path.isfile("Save.txt")def load():    if Player_exists:        c.Player = pickle.load(open("Save.txt", "rb"))        os.system("cls")        Player_Command()    else:        Area001()def Area001():    print("\033[0;35mPICK A CLASS\n" "\033[37;1m===============================================================================================",          "\n\033[33;1m " + c.PlayerClass.warrior.character + ":" + "                                    \033[37;1m||\033[33;1m " + c.PlayerClass.outcast.character + ":" + "                                     \033[37;1m||\033[31;1m",          "\n                                             \033[37;1m||\033[34;1m                                              \033[37;1m||\033[31;1m"          "\n   Attributes:                               \033[37;1m||\033[31;1m" + "    Attributes:" + "                               \033[37;1m||\033[36;1m"                                                                                            "\n      Vitality     : \033[33;1m" + str(c.PlayerClass.warrior.vitality) + "                       \033[37;1m||\033[36;1m    " + "   Vitality     : \033[33;1m" + str(c.PlayerClass.outcast.vitality) + "                       \033[37;1m||\033[36;1m",          "\n      Resistance   : \033[33;1m" + str(c.PlayerClass.warrior.resistance) + "                      \033[37;1m||\033[36;1m    " + "   Resistance   : \033[33;1m" + str(c.PlayerClass.outcast.resistance) + "                       \033[37;1m||\033[36;1m",          "\n      Strength     : \033[33;1m" + str(c.PlayerClass.warrior.strength) + "                      \033[37;1m||\033[36;1m    " + "   Strength     : \033[33;1m" + str(c.PlayerClass.outcast.strength) + "                       \033[37;1m||\033[36;1m",          "\n      Intelligence : \033[33;1m" + str(c.PlayerClass.warrior.intelligence) + "                       \033[37;1m||\033[36;1m    " + "   Intelligence : \033[33;1m" + str(c.PlayerClass.outcast.intelligence) + "                       \033[37;1m||\033[36;1m",          "\n                                             \033[37;1m||\033[34;1m                                              \033[37;1m||\033[31;1m"          "\n   Weapons:                                  \033[37;1m||\033[31;1m    " + "Weapons:" + "                                  \033[37;1m||\033[36;1m"                                                                                             "\n      Primary Weapon : \033[33;1m" + str(c.PlayerClass.warrior.eq_weapon1.name) + "           \033[37;1m||\033[34;1m    " + "   \033[36;1mPrimary Weapon : \033[33;1m" + str(c.PlayerClass.outcast.eq_weapon1.name) + "                \033[37;1m||\033[34;1m",          "\n         Damage: \033[32;1m" + str(c.PlayerClass.warrior.eq_weapon1.attack) + "\033[34;1m | Block: \033[32;1m" + str(c.PlayerClass.warrior.eq_weapon1.block) + "             \033[37;1m||\033[34;1m          Damage: \033[32;1m" + str(c.PlayerClass.outcast.eq_weapon1.attack) + "\033[34;1m | Block: \033[32;1m" + str(c.PlayerClass.outcast.eq_weapon1.block) + "              \033[37;1m||\033[34;1m"          "\n      \033[36;1mSecondary Weapon : \033[33;1m" + str(c.PlayerClass.warrior.eq_weapon2.name) + "                \033[37;1m||\033[34;1m    " + "   \033[36;1mSecondary Weapon : \033[33;1m" + str(c.PlayerClass.outcast.eq_weapon2.name) + "                \033[37;1m||\033[34;1m",          "\n         \033[32;1mN/A                                 \033[37;1m||\033[34;1m          \033[32;1mN/A                                 \033[37;1m||\033[34;1m"          "\n                                             \033[37;1m||\033[34;1m                                              \033[37;1m||\033[31;1m"          "\n   Armor:                                    \033[37;1m||\033[31;1m    " + "Armor:" + "                                    \033[37;1m||\033[34;1m"                                                                                           "\n      \033[36;1mHead  : \033[33;1m" + str(c.PlayerClass.warrior.eq_head.name) + "            \033[37;1m||\033[34;1m    " + "   \033[36;1mHead  : \033[33;1m" + str(c.PlayerClass.outcast.eq_head.name) + "                           \033[37;1m||\033[34;1m",          "\n         Defense: \033[32;1m" + str(c.PlayerClass.outcast.eq_head.armor_defense) + "                          \033[37;1m||\033[34;1m    " + "      Defense: \033[32;1m" + str(c.PlayerClass.outcast.eq_head.armor_defense) + "                          \033[37;1m||\033[34;1m",          "\n      \033[36;1mBody  : \033[33;1m" + str(c.PlayerClass.warrior.eq_body.name) + "                \033[37;1m||\033[34;1m    " + "   \033[36;1mBody  : \033[33;1m" + str(c.PlayerClass.outcast.eq_body.name) + "                 \033[37;1m||\033[34;1m",          "\n         Defense: \033[32;1m" + str(c.PlayerClass.outcast.eq_body.armor_defense) + "                        \033[37;1m||\033[34;1m    " + "      Defense: \033[32;1m" + str(c.PlayerClass.outcast.eq_body.armor_defense) + "                        \033[37;1m||\033[34;1m",          "\n      \033[36;1mHands : \033[33;1m" + str(c.PlayerClass.warrior.eq_hands.name) + "                           \033[37;1m||\033[34;1m    " + "   \033[36;1mHands : \033[33;1m" + str(c.PlayerClass.outcast.eq_hands.name) + "                           \033[37;1m||\033[34;1m",          "\n         Defense: \033[32;1m" + str(c.PlayerClass.outcast.eq_hands.armor_defense) + "                          \033[37;1m||\033[34;1m    " + "      Defense: \033[32;1m" + str(c.PlayerClass.outcast.eq_hands.armor_defense) + "                          \033[37;1m||\033[34;1m",          "\n      \033[36;1mLegs  : \033[33;1m" + str(c.PlayerClass.warrior.eq_legs.name) + "               \033[37;1m||\033[34;1m    " + "   \033[36;1mLegs  : \033[33;1m" + str(c.PlayerClass.outcast.eq_legs.name + "              \033[37;1m||\033[34;1m") +          "\n         Defense: \033[32;1m" + str(c.PlayerClass.outcast.eq_legs.armor_defense) + "                        \033[37;1m||\033[34;1m    " + "      Defense: \033[32;1m" + str(c.PlayerClass.outcast.eq_legs.armor_defense) + "                        \033[37;1m||\033[34;1m",          "\n                                             \033[37;1m||\033[34;1m                                              \033[37;1m||\033[31;1m"          "\n   Stats:                                    \033[37;1m||\033[31;1m    " + "Stats:" + "                                    \033[37;1m||\033[34;1m"          "\n      \033[36;1mHealth     : \033[33;1m" + "204" + "                       \033[37;1m||\033[34;1m    " + "   \033[36;1mHealth     : \033[33;1m" + "204" + "                       \033[37;1m||\033[34;1m    "          "\n      \033[36;1mDamage     : \033[33;1m" + "318" + "                       \033[37;1m||\033[34;1m    " + "   \033[36;1mDamage     : \033[33;1m" + "153" + "                       \033[37;1m||\033[34;1m    "          "\n      \033[36;1mDefense    : \033[33;1m" + "248" + "                       \033[37;1m||\033[34;1m    " + "   \033[36;1mDefense    : \033[33;1m" + "149" + "                       \033[37;1m||\033[34;1m    "             "\n      \033[36;1mMax Weight : \033[33;1m" + "64" + "                        \033[37;1m||\033[34;1m    " + "   \033[36;1mMax Weight : \033[33;1m" + "60" + "                        \033[37;1m||\033[34;1m    "                                                                                                                                                                                            "\n                                             \033[37;1m||\033[34;1m                                              \033[37;1m||\033[34;1m"          "\n\033[37;1m===============================================================================================\033[33;1m\n "          + c.PlayerClass.rogue.character + ":" + "                                      \033[37;1m||\033[33;1m " + c.PlayerClass.hunter.character + ":" + "                                      \033[37;1m||\033[34;1m",          "\n                                             \033[37;1m||\033[34;1m                                              \033[37;1m||\033[31;1m"          "\n   Attributes:                               \033[37;1m||\033[31;1m" + "    Attributes:" + "                               \033[37;1m||\033[34;1m",          "\n      \033[36;1mVitality     : \033[33;1m" + str(c.PlayerClass.rogue.vitality) + "                       \033[37;1m||\033[34;1m    " + "   \033[36;1mVitality     : \033[33;1m" + str(c.PlayerClass.hunter.vitality) + "                       \033[37;1m||\033[34;1m",          "\n      \033[36;1mResistance   : \033[33;1m" + str(c.PlayerClass.rogue.resistance) + "                      \033[37;1m||\033[34;1m    " + "   \033[36;1mResistance   : \033[33;1m" + str(c.PlayerClass.hunter.resistance) + "                       \033[37;1m||\033[34;1m",          "\n      \033[36;1mStrength     : \033[33;1m" + str(c.PlayerClass.rogue.strength) + "                      \033[37;1m||\033[34;1m    " + "   \033[36;1mStrength     : \033[33;1m" + str(c.PlayerClass.hunter.strength) + "                       \033[37;1m||\033[34;1m",          "\n      \033[36;1mIntelligence : \033[33;1m" + str( c.PlayerClass.rogue.intelligence) + "                      \033[37;1m||\033[34;1m    " + "   \033[36;1mIntelligence : \033[33;1m" + str(c.PlayerClass.hunter.intelligence) + "                      \033[37;1m||\033[34;1m",          "\n                                             \033[37;1m||\033[34;1m                                              \033[37;1m||\033[31;1m"          "\n   Weapons                                   \033[37;1m||\033[31;1m    " + "Weapons" + "                                   \033[37;1m||\033[34;1m"                                                                                             "\n      \033[36;1mPrimary Weapon : \033[33;1m" + str(c.PlayerClass.rogue.eq_weapon1.name) + "                \033[37;1m||\033[34;1m    " + "   \033[36;1mPrimary Weapon : \033[33;1m" + str(c.PlayerClass.hunter.eq_weapon1.name) + "               \033[37;1m||\033[34;1m",          "\n         Damage: \033[32;1m" + str(c.PlayerClass.rogue.eq_weapon1.attack) + "\033[34;1m | Block: \033[32;1m" + str(c.PlayerClass.rogue.eq_weapon1.block) + "              \033[37;1m||\033[34;1m          Damage: \033[32;1m" + str(c.PlayerClass.hunter.eq_weapon1.attack) + "\033[34;1m | Block: \033[32;1m" + str(c.PlayerClass.hunter.eq_weapon1.block) + "              \033[37;1m||\033[34;1m"          "\n      \033[36;1mSecondary Weapon : \033[33;1m" + str(c.PlayerClass.rogue.eq_weapon2.name) + "              \033[37;1m||\033[34;1m    " + "   \033[36;1mSecondary Weapon : \033[33;1m" + str(c.PlayerClass.hunter.eq_weapon2.name) + "                \033[37;1m||\033[34;1m",          "\n         Damage: \033[32;1m" + str(c.PlayerClass.rogue.eq_weapon2.attack) + "\033[34;1m | Block: \033[32;1m" + str(c.PlayerClass.rogue.eq_weapon2.block) + "              \033[37;1m||\033[34;1m          \033[32;1mN/A                                 \033[37;1m||\033[34;1m"          "\n                                             \033[37;1m||\033[34;1m                                              \033[37;1m||\033[31;1m"          "\n   Armor                                     \033[37;1m||\033[31;1m    " + "Armor" + "                                     \033[37;1m||\033[34;1m"                                                                                           "\n      \033[36;1mHead  : \033[33;1m" + str(c.PlayerClass.rogue.eq_head.name) + "                           \033[37;1m||\033[34;1m    " + "   \033[36;1mHead  : \033[33;1m" + str(c.PlayerClass.hunter.eq_head.name) + "                   \033[37;1m||\033[34;1m",          "\n         Defense: \033[32;1m" + str(c.PlayerClass.rogue.eq_head.armor_defense) + "                          \033[37;1m||\033[34;1m    " + "      Defense: \033[32;1m" + str(c.PlayerClass.hunter.eq_head.armor_defense) + "                        \033[37;1m||\033[34;1m",          "\n      \033[36;1mBody  : \033[33;1m" + str(c.PlayerClass.rogue.eq_body.name) + "                 \033[37;1m||\033[34;1m    " + "   \033[36;1mBody  : \033[33;1m" + str(c.PlayerClass.hunter.eq_body.name) + "                  \033[37;1m||\033[34;1m",          "\n         Defense: \033[32;1m" + str(c.PlayerClass.rogue.eq_body.armor_defense) + "                        \033[37;1m||\033[34;1m    " + "      Defense: \033[32;1m" + str(c.PlayerClass.hunter.eq_body.armor_defense) + "                        \033[37;1m||\033[34;1m",          "\n      \033[36;1mHands : \033[33;1m" + str(c.PlayerClass.rogue.eq_hands.name) + "              \033[37;1m||\033[34;1m    " + "   \033[36;1mHands : \033[33;1m" + str(c.PlayerClass.hunter.eq_hands.name) + "                 \033[37;1m||\033[34;1m",          "\n         Defense: \033[32;1m" + str(c.PlayerClass.rogue.eq_hands.armor_defense) + "                        \033[37;1m||\033[34;1m    " + "      Defense: \033[32;1m" + str(c.PlayerClass.hunter.eq_hands.armor_defense) + "                        \033[37;1m||\033[34;1m",          "\n      \033[36;1mLegs  : \033[33;1m" + str(c.PlayerClass.rogue.eq_legs.name) + "                           \033[37;1m||\033[34;1m    " + "   \033[36;1mLegs  : \033[33;1m" + str(c.PlayerClass.hunter.eq_legs.name) + "                  \033[37;1m||\033[34;1m" +          "\n         Defense: \033[32;1m" + str(c.PlayerClass.rogue.eq_legs.armor_defense) + "                          \033[37;1m||\033[34;1m    " + "      Defense: \033[32;1m" + str(c.PlayerClass.hunter.eq_legs.armor_defense) + "                        \033[37;1m||\033[34;1m",          "\n                                             \033[37;1m||\033[34;1m                                              \033[37;1m||\033[31;1m"          "\n   Stats:                                    \033[37;1m||\033[31;1m    " + "Stats:" + "                                    \033[37;1m||\033[34;1m"          "\n      \033[36;1mHealth     : " + "\033[33;1m204" + "                       \033[37;1m||\033[34;1m    " + "   \033[36;1mHealth     : " + "\033[33;1m204" + "                       \033[37;1m||\033[34;1m    "          "\n      \033[36;1mDamage     : " + "\033[33;1m229" + "                       \033[37;1m||\033[34;1m    " + "   \033[36;1mDamage     : " + "\033[33;1m166" + "                       \033[37;1m||\033[34;1m    "          "\n      \033[36;1mDefense    : " + "\033[33;1m178" + "                       \033[37;1m||\033[34;1m    " + "   \033[36;1mDefense    : " + "\033[33;1m341" + "                       \033[37;1m||\033[34;1m    "          "\n      \033[36;1mMax Weight : " + "\033[33;1m62" + "                        \033[37;1m||\033[34;1m    " + "   \033[36;1mMax Weight : " + "\033[33;1m59" + "                        \033[37;1m||\033[34;1m    "          "\n                                             \033[37;1m||\033[34;1m                                              \033[37;1m||\033[34;1m"                    "\n\033[37;1m===============================================================================================\033[0;0m\n")    picked_options = ["warrior", "outcast", "rogue", "hunter"]    picked = None    while picked not in picked_options:        picked = input("\n\033[0;35mWhat class will you be?: ").lower()    if picked == "warrior":        c.Player = c.PlayerClass.warrior        c.Player.player_name = input("\033[0;35mWhat is your name?: \033[0;0m").capitalize().removesuffix(" ")    elif picked == "outcast":        c.Player = c.PlayerClass.outcast        c.Player.player_name = input("\033[0;35mWhat is your name?: \033[0;0m").capitalize().removesuffix(" ")    elif picked == "rogue":        c.Player = c.PlayerClass.rogue        c.Player.player_name = input("\033[0;35mWhat is your name?: \033[0;0m").capitalize().removesuffix(" ")    elif picked == "hunter":        c.Player = c.PlayerClass.hunter        c.Player.player_name = input("\033[0;35mWhat is your name?: \033[0;0m").capitalize().removesuffix(" ")    c.player_att_call()    c.inventory_eq_call()    c.stats_show()    Player_Command()def Player_Command():    pickle.dump(c.Player, open("Save.txt", "wb"))    player_prompt = None    player_prompt_choices = ("quit", "move", "heal", "stats", "clear", "see",                             "pick up", "equip", "drop", "inspect", "unequip",                             "test", "rest", "upgrade", "give")    while player_prompt not in player_prompt_choices:        player_prompt = input("\033[0;35mEnter Command: \033[0;0m").lower()    if player_prompt == "quit":        print("\033[31;1mDisconnecting...")        time.sleep(1.5)        pickle.dump(c.Player, open("Save.txt", "wb"))        quit()    elif player_prompt == "move":        c.Player.ground_items.clear()        c.player_move()        Player_Command()    elif player_prompt == "heal":        c.heal()        Player_Command()    elif player_prompt == "stats":        c.stats_show()        print(str(c.Player.flask.health_buff))        Player_Command()    elif player_prompt == "clear":        os.system("cls")        Player_Command()    elif player_prompt == "see":        if (len(c.Player.ground_items)) == 0:            print("You can't see anything")        else:            print("Items")            for x in c.Player.ground_items:                print("" + x.name)        Player_Command()    elif player_prompt == "pick up":        c.pick_up()        Player_Command()    elif player_prompt == "equip":        c.equip()        Player_Command()    elif player_prompt == "drop":        c.drop()        Player_Command()    elif player_prompt == "inspect":        c.show()        Player_Command()    elif player_prompt == "unequip":        c.unequip()        Player_Command()    elif player_prompt == "test":        c.enemy_att_call()        Player_Command()    elif player_prompt == "give":        c.Player.inventory.append(c.Blueprints.health_flask_upgrade)        c.Player.inventory.append(c.Blueprints.health_flask_upgrade)        c.Player.inventory.append(c.Blueprints.health_flask_upgrade)        Player_Command()    elif player_prompt == "rest":        print("\033[33;3mYou sat down at the fire.")        c.rest()    else:        Player_Command()load()