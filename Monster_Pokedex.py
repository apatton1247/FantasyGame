############### Monster Pokedex ###############

import Monster_Class

########## Level 1 ##########

class Maul_Rat(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Maul Rat"
        self.level = 1
        self.description = "A homely-looking rat wearing a wig and wielding a mallet. A creature from Hell. +3 against Clerics."
        self.undead = False
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "She whacks you. Lose a level."
        self.bad_stuff = lose_level(1, battle_dict)
        self.fight = pass
        self.chase = pass
        self.enhancement = pass
        self.bias = clerics(3, battle_dict)
        self.good_stuff = pass

#An example of what could go in Monster Methods.
##        def clerics(number, battle_dict):
##            if character.char_class == "Cleric":
##                bias += 3
##            return bias

class Crabs(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Crabs"
        self.level = 1
        self.description = "Not the sea creature. It cannot be Outrun"
        self.undead = False
        self.plant = False
        self.speed = 15
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Discard armor and all items worn below the waist."
        self.bad_stuff = lose_lower_items()
        self.fight = pass
        self.chase = pass
        self.enhancement = pass
        self.bias = pass
        self.good_stuff = pass

class Potted_Plant(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Potted Plant"
        self.level = 1
        self.description = "A potted plant... thats it. Elves gain an extra Treasure after defeating it."
        self.undead = False
        self.plant = True
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "None. Escape is automatic."
        self.bad_stuff = no_bad_stuff()
        self.fight = pass
        self.chase = auto_escape()
        self.enhancement = pass
        self.bias = pass
        self.good_stuff = pass

class Lame_Goblin(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Lame Goblin"
        self.level = 1
        self.description = "A small goblin limping with a crutch. +1 to Run Away"
        self.undead = False
        self.plant = False
        self.speed = -1
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "He whacks you with his crutch. Lose a level."
        self.bad_stuff = lose_level(1)
        self.fight = pass
        self.chase = pass
        self.enhancement = pass
        self.bias = pass
        self.good_stuff = pass

class Drooling_Slime(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Drooling Slime"
        self.level = 1
        self.description = "Yucky slime! +4 against Elves."
        self.undead = False
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Discard the Footgear you are wearing. Lose a level if you are not wearing any Footgear."
        self.bad_stuff = lose_level(1)
        self.fight = pass
        self.chase = pass
        self.enhancement = pass
        self.bias = elves(4, battle_dict)
        self.good_stuff = pass

########## Level 2 ##########

class Pit_Bull(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Pit Bull"
        self.level = 2
        self.description = "If you can't defeat it, you may distract it (automatic escape) by dropping any wand, pole, or staff. (Fetch, Fido!)"
        self.undead = False
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Fang marks in your butt. Lose 2 levels."
        self.bad_stuff = lose_level(2)
        self.fight = bribe(wand, pole, staff)#we will have to add a boelean attribute to items classes for this
        self.chase = pass
        self.enhancement = pass
        self.bias = pass
        self.good_stuff = pass

class Flying_Frogs(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Flying Frogs"
        self.level = 2
        self.description = "-1 to Run Away"
        self.undead = False
        self.plant = False
        self.speed = 1
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "They bite!. Lose 2 levels."
        self.bad_stuff = lose_level(2)
        self.fight = pass
        self.chase = pass
        self.enhancement = pass
        self.bias = pass
        self.good_stuff = pass

class Mr_Bones(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Mr. Bones
        self.level = 2
        self.description = "A skeleton dancing in a top hat. If you must flee you lose a level even if you escape."
        self.undead = True
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "His bony touch costs you 2 levels."
        self.bad_stuff = lose_level(2)
        self.fight = pass
        self.chase = lose_level(1)
        self.enhancement = pass
        self.bias = pass
        self.good_stuff = pass

class Large_Angry_Chicken(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Large Angry Chicken"
        self.level = 2
        self.description = "Fried Chicken is delicious. Gain an exrtra level if you defeat it with fire or flame."
        self.undead = False
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Very painful pecking. Lose a level."
        self.bad_stuff = lose_level(1)
        self.fight = used_fire(#checks if item or one shot in battle dictionary has fire attribute)
        self.chase = pass
        self.enhancement = pass
        self.bias = pass
        self.good_stuff = pass

class Gelatinous_Octahedron(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Gelatinous Octahedron"
        self.level = 2
        self.description = "+1 to Run Away"
        self.undead = False
        self.plant = False
        self.speed = -1
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Drop all your Big items."
        self.bad_stuff = lose_big_items()
        self.fight = pass
        self.chase = pass
        self.enhancement = pass
        self.bias = pass
        self.good_stuff = pass

















########## Level 10 ##########

class Shadow_Nose(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "The Shadow Nose"
        self.description = "Anything affecting the Floating nose works on its undead Shadow, too.  But the shadow won't take bribes."
        self.undead = True
        self.plant = False
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 3
        self.bad_stuff_description = "You cannot flee. It automatically catches you. Lose 3 levels."
        self.bad_stuff = lose_level(1, battle_dict)
        self.fight = pass
        self.chase = pass
        self.enhancement = pass
        self.bias = pass
        self.good_stuff = pass
##      if "The Floating Nose" in battle_dict.keys():
##            self.enhancement += 10
##        if "Snot Elemental" in battle_dict.keys():
##            self.enhancement += 10

        

   
  
