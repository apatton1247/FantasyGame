############### Monster Pokedex ###############

from Monster_Methods_Manuscript import *

########## Monster Superclass ##########
class Monster(object):
    def __init__(self):
        self.type = "monster"
        self.name = "monster name"
        self.level = 0
        self.description = "Generic description for characters to see."
        self.special_attributes = []
        self.speed = 0
        self.level_rewarded = 0
        self.treasure_rewarded = 0
        self.bad_stuff_description = "Description of bad stuff goes here."
        self.battle_strength = 0

    def prelim(self, battle_dict):
        pass

    def pursuit(self, battle_dict):
        pass
      
    def bad_stuff(self, character):
        pass

    def update_monster(self, battle_dict):
        self.battle_strength = self.level

    def fight(self, battle_dict):
        pass

    def chase(self, battle_dict):
        pass

    def good_stuff(self, battle_dict):
        pass

########## Level 1 ##########

class Maul_Rat(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Maul Rat"
        self.level = 1
        self.description = "A homely-looking rat wearing a wig and wielding a mallet. A creature from Hell. +3 against Clerics."
        self.spec_attr = []
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "She whacks you. Lose a level."
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_level(1, character)

    def update_monster(self, battle_dict):
        self.bias = monster_bias(clerics(battle_dict), 3)
        self.battle_strength = self.level + self.bias

class Crabs(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Crabs"
        self.level = 1
        self.description = "Not the sea creature. It cannot be Outrun."
        self.spec_attr = []
        self.speed = 15
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Discard armor and all items worn below the waist."
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_lower_items(character)

class Potted_Plant(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Potted Plant"
        self.level = 1
        self.description = "A potted plant... thats it. Elves gain an extra Treasure after defeating it."
        self.spec_attr = ["plant"]
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "None. Escape is automatic."
        self.fight = None
        self.chase = auto_escape()
        self.good_stuff = None
        self.battle_strength = 0

    def bad_stuff(self, character):
        no_bad_stuff(character)

    def chase(self, battle_dict):
        auto_escape()

class Lame_Goblin(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Lame Goblin"
        self.level = 1
        self.description = "A small goblin limping with a crutch. +1 to Run Away"
        self.spec_attr = []
        self.speed = -1
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "He whacks you with his crutch. Lose a level."
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_level(1, character)

class Drooling_Slime(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Drooling Slime"
        self.level = 1
        self.description = "Yucky slime! +4 against Elves."
        self.spec_attr = []
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Discard the Footgear you are wearing. Lose a level if you are not wearing any Footgear."
        self.battle_strength = 0

    def bad_stuff(self, character):
        if character.footgear_slots_used > 0:
            lose_footgear(character)
        else:
            lose_level(1, character)

    def update_monster(self, battle_dict):
        self.bias = monster_bias(elves(battle_dict), 4)
        self.battle_strength = self.level + self.bias

class Tequila_Mockingbird(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Tequila Mockingbird"
        self.level = 1
        self.description = "Horrible, drunken singing, very much like that of a Bard. +5 vs. Bards."
        self.spec_attr = []
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "You ate the worm! Discard two items (your choice) from your backpack."
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_backpack_item(2, character)

    def update_monster(self, battle_dict):
        self.bias = monster_bias(bards(battle_dict), 5)
        self.battle_strength = self.level + self.bias

########## Level 2 ##########

class Pit_Bull(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Pit Bull"
        self.level = 2
        self.description = "If you can't defeat it, you may distract it (automatic escape) by dropping any wand, pole, or staff. (Fetch, Fido!)"
        self.spec_attr = []
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Fang marks in your butt. Lose 2 levels."
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_level(2, character)

    def fight(self, battle_dict):
        #A player my say "drop " some pole/wand/staff, and if that item has "pole" or "wand"
        # or "staff" as a special attribute, then the player may auto-escape.
        pass

class Flying_Frogs(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Flying Frogs"
        self.level = 2
        self.description = "-1 to Run Away"
        self.spec_attr = []
        self.speed = 1
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "They bite!. Lose 2 levels."
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_level(2, character)

class Mr_Bones(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Mr. Bones"
        self.level = 2
        self.description = "A skeleton dancing in a top hat. If you must flee you lose a level even if you escape."
        self.spec_attr = ["undead"]
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "His bony touch costs you 2 levels."
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_level(2, character)

    def chase(self, character):
        lose_level(1, character)

class Large_Angry_Chicken(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Large Angry Chicken"
        self.level = 2
        self.description = "Fried Chicken is delicious. Gain an extra level if you defeat it with fire or flame."
        self.spec_attr = []
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Very painful pecking. Lose a level."
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_level(1, character)

    def fight(self, battle_dict):
        #If the character used fire in any way, they go up another level
        pass

class Gelatinous_Octahedron(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Gelatinous Octahedron"
        self.level = 2
        self.description = "+1 to Run Away"
        self.spec_attr = []
        self.speed = -1
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Drop all your Big items."
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_big_items(character)

########## Level 3 ##########

class The_Mighty_Germ(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "The Mighty Germ"
        self.level = 3
        self.description = "Really small spec. Halflings can just stomp it, killing it automatically."
        self.spec_attr = []
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Helpless sneezing causes items to fall out of your backpack. Discard 2 items (your choice) from your backpack."
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_backpack_item(2, character)

    def fight(self, battle_dict):
        #If a character whose race is "halfling" says "Stomp", they should auto-kill the Mighty Germ.  Also, maybe put in a custom victory message here.
        pass
    
class Were_Turtle(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Were-Turtle"
        self.level = 3
        self.description = "A nerdy-looking turtle with a spear. Pursues verrrry slowly. +2 to Run Away"
        self.spec_attr = []
        self.speed = -2
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "If you lose a race to the Were_Turtle, you lose your Race. If you were a Half-Breed, lose one non-human race. If you were human already, there's no effect."
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_race(1, character)

class Psycho_Squirrel(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Psycho Squirrel"
        self.level = 3
        self.description = "Will not attack females, or wearers of the Spiked Codpiece."
        self.spec_attr = []
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 1
        self.bad_stuff_description = "Lose a level. Speak in a high, squecky voice until your next turn."
        #self.fight = will_not_pursue(battle_dict, female, spiked_codpiece)
        self.chase = None
        self.good_stuff = None
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_level(1, character)
        font_italic(character)

    def pursuit(self, battle_dict):
        if len(battle_dict["monster"].keys()) == 1 and len(battle_dict["character"].keys()) == 1: # and the character is a female or wears the spiked codpiece
            will_not_pursue()

class Pinata(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Pinata"
        self.level = 3
        self.description = "Large paper mache creature. If the Pinata is defeated, each party memeber, in the order you choose, gains one Treasure. It doesn't matter who participated in the combat."
        self.spec_attr = []
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 0
        self.bad_stuff_description = "The player to your left picks one item that you are using or from your closet. Discard it."
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_field_item(1, character, character_to_left)

    def good_stuff(self, battle_dict):
        #Pinata loot method.  It's spelled out above, just need to figure out how to implement it.
        pass

########## Level 4 ##########

class Leperchaun(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Leperchaun"
        self.level = 4
        self.description = "A Leprechaun with limbs falling off. He's gross! +5 against Elves."
        self.spec_attr = []
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "He takes two items from you - one chosen by the player on either side of you."
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_field_item(1, character)#, (character_to_left))
        lose_field_item(1, character)#, (character_to_right))

    def update_monster(self, battle_dict):
        self.bias = monster_bias(elves(battle_dict), 5)
        self.battle_strength = self.level + self.bias

class Snails_on_Speed(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Snails on Speed"
        self.level = 4
        self.description = "-2 to Run Away"
        self.spec_attr = []
        self.speed = 2
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "They steal your treasure. Roll a die and lose that many items or cards in your hand - your choice."
        self.battle_strength = 0

    def bad_stuff(self, character):
        num_to_lose = roll_die(character)
        where = ""
        while where != "backpack" and where != "field":
            where = input("Will you lose items from your backpack, or items from the field? ").lower()
        if where == "backpack":
            lose_backpack_item(num_to_lose, character)
        else:
            lose_field_item(num_to_lose, character)

class Harpies(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Harpies"
        self.level = 4
        self.description = "Winged creatures playing a harp. They resist magic. +5 against Wizards."
        self.spec_attr = []
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "Their music is really, really bad. Lose 2 levels."
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_level(2, character)

    def update_monster(self, battle_dict):
        self.bias = monster_bias(wizards(battle_dict), 5)
        self.battle_strength = self.level + self.bias

class Undead_Horse(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Undead Horse"
        self.level = 4
        self.description = "+5 against Dwarves."
        self.spec_attr = ["undead"]
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "Kicks, bites, and smells awful. Lose 2 levels."
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_level(2, character)

    def update_monster(self, battle_dict):
        self.bias = monster_bias(dwarves(battle_dict), 5)
        self.battle_strength = self.level + self.bias

########## Level 5 ##########

class Fungus(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Fungus"
        self.level = 5
        self.description = "If the the Fungus becomes Humongous it gains, not the normal +10, but +25! Do not truffle with the Humongous Fungus."
        self.spec_attr = ["plant"]
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "Elves lose 2 levels. Anyone else loses 1. Double the penalty if the Fungus was Humongous."
        self.battle_strength = 0

    def bad_stuff(self, character):
        levels_to_lose = 1
        if character.char_race == "elf":
            lose_level((2*levels_to_lose), character)
        else:
            lose_level(1, character)

    def fight(self, battle_dict):
        #Provision for a player using Humongous on the Fungus to give an extra +15
        pass

class Plague_Rats(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Plague Rats"
        self.level = 5
        self.description = "Will flee from Orcs rather than attacking, leaving their treasure behind. Anyone else must fight, and is -1 to Run Away."
        self.spec_attr = []
        self.speed = 1
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "Lose 2 levels."
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_level(2, character)

    def pursuit(self, battle_dict):
        #will not allow pursuit by orcs, will just leave the treasure and circumvent the rest of the battle.  Maybe custom text here.
        pass

class Teddy_Bear(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Teddy Bear"
        self.level = 5
        self.description = "Digustingly cute. +5 against Orcs."
        self.spec_attr = []
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "Discard your whole backpack. If you discarded more than one item, you may pick up one Treasure while Teddy is cackling over his ill-gotten gains."
        self.battle_strength = 0

    def bad_stuff(self, character):
        backpack_size = len(character.backpack)
        empty_backpack(character)
        if backpack_size > 1:
            #Maybe have some text here explaining that this happened, maybe even name the treasure.
            character.backpack.append(treasure_deck[0])

    def update_monster(self, battle_dict):
        self.bias = monster_bias(orcs(battle_dict), 5)
        self.battle_strength = self.level + self.bias

class Crawling_Hand(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Crawling Hand"
        self.level = 4
        self.description = "A severed hand. If you give the Crawling Hand a Wishing Ring instead of fighting it, it will be your little friend. As a friend it now acts as a small item that gives +3 bonus in combat."
        self.spec_attr = ["undead"]
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "Undead wedgie! Lose 2 levels."
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_level(2, character)
        
########## Level 6 ##########

class Lawyers(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Lawyers"
        self.level = 6
        self.description = "Will not attack a Thief (professional courtesy). A Thief encountering a lawyer may instead discard two Treasures and pick up two new hidden ones."
        self.spec_attr = []
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "He hits you with an injunction. Let each other player take one item from your backpack starting with the player to your left. Discard the remainder."
        self.battle_strength = 0

    def bad_stuff(self, character):
        #Let other players choose items from your backpack, and after that call empty_backpack().
        pass

    def pursuit(self, battle_dict):
        #If the player's a thief they have the option to attack anyway or take the 2 for 2 treasure deal.
        pass

class Pukachu(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Pukachu"
        self.level = 6
        self.description = "Gain an extra level if you defeat it without using help or bonuses."
        self.spec_attr = []
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "Projectile vomiting attack! Discard your whole backpack."
        self.battle_strength = 0

    def bad_stuff(self, character):
        empty_backpack(character

    def update_monster(self, battle_dict):
        pass

    def good_stuff(self, battle_dict):
        #If you defeat it when len(battle_dict["character"].keys()) == 1 and the character's level > 6, self.level_rewarded = 2
        pass

class Shrieking_Geek(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Shrieking Geek"
        self.level = 6
        self.description = "+ 6 against Warriors."
        self.spec_attr = []
        self.speed = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 2
        self.bad_stuff_description = "You become a normal, boring Human. Lose both your Race and Class."
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_races(character)
        lose_classes(character)

    def update_monster(self, battle_dict):
        self.bias = monster_bias(warriors(battle_dict), 6)
        self.battle_strength = self.level + self.bias

########## Level 7 ##########

      

########## Level 8 ##########



########## Level 9 ##########

        

########## Level 10 ##########

class Shadow_Nose(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "The Shadow Nose"
        self.level = 10
        self.description = "Anything affecting the Floating nose works on its undead Shadow, too.  But the shadow won't take bribes."
        self.spec_attr = ["undead"]
        self.speed = 15
        self.level_rewarded = 1
        self.treasure_rewarded = 3
        self.bad_stuff_description = "You cannot flee. It automatically catches you. Lose 3 levels."
##      if "The Floating Nose" in battle_dict.keys():
##            self.enhancement += 10
##        if "Snot Elemental" in battle_dict.keys():
##            self.enhancement += 10
        self.battle_strength = 0

    def bad_stuff(self, character):
        lose_level(3, character)
