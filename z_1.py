# TO_DO

# Color Code Text ✅

# Starting Characters show some hidden features ✅
# Stats shows some hidden features ✅
#       Damage, Defence, Health, ect? ✅

# Add resistance attribute ✅

# make Run work ✅

# Level up shows what it would change ✅

# Clear function ✅
#       Clears all text from prompt ✅

# Make Enemies drop items ✅
#   list of items on ground ✅
#   chance for the enemy to drop items✅
#       25% ✅

#   if enemy drops an item it's added to the list ✅
#   Make it, so you can SEE items on ground ✅

#   Make it so that you can pick up items from ground ✅
#   Add pick up Action ✅
#       If player command == pick up item_name & Item_name is on ground ✅
#           Item is added to inventory ✅
#   If player moves list clears ✅


# Player Inventory (BAG) ✅
#       Open Inventory Action ✅

# Play can equip armor and weapons ✅

# Armor_Types can only be assigned to the proper thing ✅

#
# Player Equipped ✅
# INDEX'S ✅
#   Head = 0  |  Body = 1  |  Hands = 2  |  Legs = 3  |  Weapon1 = 4  |  Weapon2  = 5

# Make it so that weapon requirements work ✅

#                                                    PLAYER SELECTION ✅

#   1. Warrior
#       Vitality = 10
#       Endurance = 9
#       Strength = 12
#       Intelligence = 4
#       Dexterity = 12
#       Starting Weapon =
#       Starting Armor =
#       damage =117.6


#   2. Outcast
#       Vitality = 8
#       Endurance = 8
#       Strength = 8
#       Intelligence = 8
#       Dexterity = 8
#       Starting Weapon =
#       Starting Armor =
#       damage = 84.4

#   3. Rogue
#       Vitality = 8
#       Endurance = 12
#       Strength = 8
#       Intelligence = 10
#       Dexterity = 12
#       Starting Weapon =
#       Starting Armor =
#       damage = 121.4

#   4. Hunter
#       Vitality = 8
#       Endurance = 9
#       Strength = 8
#       Intelligence = 12
#       Dexterity = 10
#       Starting Weapon =
#       Starting Armor =
#       damage = 90.4

# ******************************************************************************************************************

#                                                      ATTRIBUTES
#                                                   ________________
#
# Attributes LAWS
#   1. Max level = 100
#   2. Default Attributes = Player Selection Attributes ✅


#   1. Vitality - Health = Vitality * 1.3(Strength) * 1.1(Endurance) ✅
#       HEALTH |
#   2. Endurance - Stamina ✅
#       RUNNING |
#   3. Strength - Power ✅

#   4. Intelligence - Smarts ✅

#   5. Dexterity - ***( Dexterity * 1.2(Strength) )*** ✅

#   6. Crafting (Player Only) - Makes things
#       5.1: If you have found the blueprint and researched it you can make it
#      NEEDS TO EDIT 5.2: If you are smart enough you can figure out how to make a better version of it with more materials
#       5.3: ...

#   7. Max_Weight - ***(Default_Weight * 1.2 (Strength) (MAX = 220lbs)*** ✅
#
#       6.1: Current Weight - Weight in your inventory
#       6.2: Weight_Percentage = 1 - (Current Weight / Max Weight)
#       6.2 EX: if your max weight is 237lbs and the items you have is 57lbs
#               you are carrying 24% of your current max and have 76% Remaining

#   8. Attack_Chance - *** ( Total_Attack = (Strength + Dex + Intelligence) ✅
#           if Total_Attack > MOB_Total_Attack:
#               (MOB_Total_Attack / Total_Attack) = Attack_Chance
#                       Attack_Chance = 88%

#           elif Total_Attack < MOB_Total_Attack:
#               1-(Total_attack / MOB_Total_Attack) = Attack_Chance

#           ( MOB_Total_Attack / Total_Attack) )
#   8 EXAMPLE: Strength:25, Dexterity:25, Intelligence:25 | Total_Attack = 75
#   *-- Enemy: Strength:30, Dexterity:17, Intelligence:19 | MOB_Total_Attack = 66

#   9. Parrying_Chance (HIDDEN) (Player Only) = ((Dexterity * Weight_Percentage) / 100 ) * Attack_Chance ✅

#   11 DAMAGE Function done need to be called ✅


#   14 XP ✅

#   # attack ✅
#     critical damage = attack chancce -
#     damage = damage - (block + defence)

#
# ******************************************************************************************************************

#                                                          WEAPONS ✅

#   Daggers (one-handed)
#       Dagger:
#           Attack: 74
#           Block: 35
#           Critical Hit: 130%
#           Critical Block: 35
#           Str: 5
#           Dex: 9
#           Int: 0
#           Weight: 1.5

#       Misericorde:
#           Attack: 92
#           Block: 36
#           Critical Hit: 140%
#           Critical Block: 15
#           Str: 7
#           Dex: 12
#           Int: 0
#           Weight: 2
#
#       Great Knife:
#           Attack: 75
#           Block: 35
#           Critical Hit: 110%
#           Critical Block: 15
#           Str: 6
#           Dex: 12
#           Int: 0
#           Weight: 1.5
#
#       Blood-Stained Dagger:
#           Attack: 81
#           Block: 36
#           Critical Hit: 110%
#           Critical Block: 15
#           Str: 9
#           Dex: 12
#           Int: 0
#           Weight: 2

#       Wakizashi:
#           Attack: 94
#           Block: 42
#           Critical Hit: 100%
#           Critical Block: 18
#           Str: 9
#           Dex: 13
#           Int: 0
#           Weight: 3
#
#   Swords(one-handed)
#       Short Sword:
#           Attack: 102
#           Block: 45
#           Critical Hit: 100%
#           Critical Block: 28
#           Str: 8
#           Dex: 10
#           Int: 0
#           Weight: 3
#
#       Long Sword:
#           Attack: 110
#           Block: 45
#           Critical Hit: 100%
#           Critical Block: 30
#           Str: 10
#           Dex: 10
#           Int: 0
#           Weight: 3.5
#
#       Broad Sword:
#           Attack: 117
#           Block: 47
#           Critical Hit: 100%
#           Critical Block: 31
#           Str: 10
#           Dex: 10
#           Int: 0
#           Weight: 4
#
#       Weathered Straight Sword:
#           Attack: 103
#           Block: 43
#           Critical Hit: 100%
#           Critical Block: 27
#           Str: 7
#           Dex: 10
#           Int: 0
#           Weight: 3
#
#       Straight Sword:
#           Attack: 115
#           Block: 45
#           Critical Hit: 110%
#           Critical Block: 30
#           Str: 10
#           Dex: 10
#           Int: 0
#           Weight: 3.5
#
#       Slender Sword:
#           Attack: 101
#           Block: 43
#           Critical Hit: 110%
#           Critical Block: 30
#           Str: 8
#           Dex: 11
#           Int: 0
#           Weight: 3
#
#       Crystal Sword:
#           Attack: 106
#           Block: 44
#           Critical Hit: 100%
#           Critical Block: 33
#           Str: 13
#           Dex: 10
#           Int: 15
#           Weight: 4.5
#
#       Demon Sword:
#           Attack: 107
#           Block: 43
#           Critical Hit: 110%
#           Critical Block: 28
#           Str: 15
#           Dex: 12
#           Int: 20
#           Weight: 4
#
#   Great Swords (Two-handed)
#       Bastard Sword:
#           Attack: 138
#           Block: 65
#           Critical Hit: 100%
#           Critical Block: 42
#           Str: 16
#           Dex: 10
#           Int: 0
#           Weight: 9
#
#       Claymore:
#           Attack: 138
#           Block: 65
#           Critical Hit: 100%
#           Critical Block: 42
#           Str: 16
#           Dex: 13
#           Int: 0
#           Weight: 9
#
#       Iron Greatsword:
#           Attack: 149
#           Block: 73
#           Critical Hit: 100%
#           Critical Block: 47
#           Str: 18
#           Dex: 10
#           Int: 0
#           Weight: 12
#
#       Knights Greatsword:
#           Attack: 141
#           Block: 68
#           Critical Hit: 100%
#           Critical Block: 44
#           Str: 16
#           Dex: 12
#           Int: 0
#           Weight: 10
#
#       Banished Knights Greatsword:
#           Attack: 142
#           Block: 68
#           Critical Hit: 100%
#           Critical Block: 44
#           Str: 17
#           Dex: 9
#           Int: 0
#           Weight: 10
#
#       Flamberge:
#           Attack: 129
#           Block: 65
#           Critical Hit: 100%
#           Critical Block: 42
#           Str: 15
#           Dex: 14
#           Int: 0
#           Weight: 12
#
#       Demon Greatsword:
#           Attack: 160
#           Block: 80
#           Critical Hit: 100%
#           Critical Block: 52
#           Str: 20
#           Dex: 15
#           Int: 15
#           Weight: 13
#
#   Axes(one-handed)
#       Hand Axe:
#           Attack: 113
#           Block: 42
#           Critical Hit: 100%
#           Critical Block: 28
#           Str: 9
#           Dex: 8
#           Int: 0
#           Weight: 3.5
#
#       Battle Axe:
#           Attack: 123
#           Block: 47
#           Critical Hit: 100%
#           Critical Block: 28
#           Str: 12
#           Dex: 8
#           Int: 0
#           Weight: 2.5
#
#       Warped Axe:
#           Attack: 118
#           Block: 56
#           Critical Hit: 100%
#           Critical Block: 43
#           Str: 24
#           Dex: 8
#           Int: 0
#           Weight: 5.5
#
#       Stormhawk Axe:
#           Attack: 130
#           Block: 49
#           Critical Hit: 100%
#           Critical Block: 28
#           Str: 19
#           Dex: 15
#           Int: 0
#           Weight: 5.5
#
#   Great Axes(two-handed)
#       Great Axe:
#           Attack: 151
#           Block: 69
#           Critical Hit: 100%
#           Critical Block: 28
#           Str: 30
#           Dex: 8
#           Int: 0
#           Weight: 13
#
#       Executioners Great Axe:
#           Attack: 150
#           Block: 74
#           Critical Hit: 115%
#           Critical Block: 48
#           Str: 34
#           Dex: 8
#           Int: 0
#           Weight: 15
#
#       Demon Great Axe:
#           Attack: 152
#           Block: 42
#           Critical Hit: 100%
#           Critical Block: 28
#           Str: 37
#           Dex: 13
#           Int: 15
#           Weight: 13
#
# Bows(two-handed)
#       Longbow:
#           Attack: 80
#           Critical Hit: 100%
#           Str: 9
#           Dex: 14
#           Int: 0
#           Weight: 4
#
#       Pulley Bow:
#           Attack: 77
#           Critical Hit: 100%
#           Str: 11
#           Dex: 11
#           Int: 0
#           Weight: 3.5
#
#       Pulley Bow:
#           Attack: 77
#           Critical Hit: 100%
#           Str: 11
#           Dex: 11
#           Int: 0
#           Weight: 3.5
#
#   Great Bows(two-handed)
#       GreatBow:
#           Attack: 125
#           Critical Hit: 100%
#           Str: 20
#           Dex: 20
#           Int: 0
#           Weight: 10
#
#       Demon GreatBow:
#           Attack: 135
#           Critical Hit: 100%
#           Str: 25
#           Dex: 20
#           Int: 0
#           Weight: 10
#
#       Crossbow:
#           Attack: 54
#           Critical Hit: 100%
#           Str: 10
#           Dex: 8
#           Int: 0
#           Weight: 3.5
#
#       Heavy Crossbow:
#           Attack: 64
#           Critical Hit: 100%
#           Str: 14
#           Dex: 10
#           Int: 0
#           Weight: 5.5
#
# ******************************************************************************************************************

#                                                           ARMOR ✅

#   All-Knowing Set
#       All-Knowing Helmet
#           Defence: 4.6
#           Weight: 4.6
#       All-Knowing Armor
#           Defence: 12.9
#           Weight: 10.7
#       All-Knowing Gauntlets
#           Defence: 3.2
#           Weight: 3.5
#       All-Knowing Greaves
#           Defence: 7.4
#           Weight: 6.6

#   Aristocrat Set
#       Aristocrat Headband
#           Defence: 1.9
#           Weight: 1.2
#       Aristocrat Garb
#           Defence: 7.8
#           Weight: 4.9
#       Aristocrat Boots
#           Defence: 4.3
#           Weight: 2.9

#   Banished Knight Set
#       Banished Knight Helmet
#           Defence: 6.8
#           Weight: 7.5
#       Banished Knight Armor
#           Defence: 18.7
#           Weight: 17.5
#       Banished Knight Gauntlets
#           Defence: 4.7
#           Weight: 5.8
#       Banished Knight Greaves
#           Defence: 10.8
#           Weight: 10.8

#   Bandit Set
#       Bandit Mask
#           Defence: 2.8
#           Weight: 3.0
#       Bandit Garb
#           Defence: 8.0
#           Weight: 7.7
#       Bandit Manchettes
#           Defence: 1.5
#           Weight: 1.7
#       Bandit Boots
#           Defence: 4.0
#           Weight: 4.4

#   Bloodhound Knight Set
#       Bloodhound Knight Helm
#           Defence: 4.4
#           Weight: 4.6
#       Bloodhound Knight Armor
#           Defence: 12.4
#           Weight: 10.6
#       Bloodhound Knight Gauntlets
#           Defence: 3.1
#           Weight: 3.5
#       Bloodhound Knight Greaves
#           Defence: 7.1
#           Weight: 6.6

#   Chain Set
#       Chain Coif
#           Defence: 4.2
#           Weight: 3.8
#       Chain Armor
#           Defence: 11.9
#           Weight: 8.8
#       Chain Gauntlets
#           Defence: 2.9
#           Weight: 2.9
#       Chain Leggings
#           Defence: 6.8
#           Weight: 5.5

#   Commoner's Set
#       Commoner's Headband
#           Defence: 0.9
#           Weight: 1.4
#       Commoner's Garb
#           Defence: 5.3
#           Weight: 5.1
#       Commoner's Shoes
#           Defence: 1.5
#           Weight: 2.0

#   Fingerprint Set
#       Fingerprint Helm
#           Defence: 4.8
#           Weight: 4.6
#       Fingerprint Armor
#           Defence: 13.5
#           Weight: 10.6
#       Fingerprint Gauntlets
#           Defence: 3.3
#           Weight: 3.5
#       Fingerprint Greaves
#           Defence: 7.7
#           Weight: 6.6

#   Leather set
#       Leather Hood
#           Defence: 2.8
#           Weight: 3
#       Leather Armor
#           Defence: 8.0
#           Weight: 7.1
#       Leather Gloves
#           Defence: 1.9
#           Weight: 2.4
#       Leather Boots
#           Defence: 4.5
#           Weight: 4.4

#   Knight Set
#       Knight Helm
#           Defence: 4.4
#           Weight: 4.6
#       Knight Armor
#           Defence: 12.4
#           Weight: 10.6
#       Knight Gauntlets
#           Defence: 3.1
#           Weight: 3.5
#       Knight Greaves
#           Defence: 7.1
#           Weight: 6.6

#   Noble Set
#       Noble Hood
#           Defence: 1.8
#           Weight: 1.4
#       Noble Garb
#           Defence: 6.7
#           Weight: 5.1
#       Noble Trousers
#           Defence: 3.4
#           Weight: 2.5

#   Prisoner Set
#       Prisoner Shirt
#           Defence: 4.2
#           Weight: 3.2
#       Prisoner Trousers
#           Defence: 2.3
#           Weight: 2.0


# Chance to spawn a mob ✅
# if you move you have a percentage to encounter a monster
# percentage is determined by how many times you have moved
#player.spawn_chance = 100
# 1 move player.spawn_chance -= 2



# if player.spawn_chance > 0: ✅
#   random_spawn_chance = random.randint(1, int(player.spawn_chance))
#   if random_spawn_chance = 1:
#       call_fight()
#   else:
#       Player_Command():

# vitality ✅
# number_one = player_vitality - 3
# number_two = player_vitality + 3
# mob_vitality = random.randint(number_one, number_two)






