import Monster_Class

class Maul_Rat(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "Maul Rat"
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
    #def update_monster(self, battle_dict):
        #if character.char_class == "Cleric":
            #self.bias = 3

#An example of what could go in Monster Methods.
##        def clerics(number, battle_dict):
##            if character.char_class == "Cleric":
##                bias += 3
##            return bias

class Shadow_Nose(Monster):
    def __init__(self):
        self.type = "monster"
        self.name = "The Shadow Nose"
        self.description = "Anything affecting the Floating nose works on its undead Shadow, too.  But the shadow won't take bribes."
        self.bias = 0
        self.undead = True
        self.plant = False
        self.speed = 0
        self.enhancement = 0
        self.level_rewarded = 1
        self.treasure_rewarded = 3
        self.bad_stuff_description = "You cannot flee. It automatically catches you. Lose 3 levels."

    def update_monster(self, battle_dict):
        if "The Floating Nose" in battle_dict.keys():
            self.enhancement += 10
        if "Snot Elemental" in battle_dict.keys():
            self.enhancement += 10

    def chase(self, character):
        #No escape possible
        bad_stuff(character)
    
    def fight(self, character):
        pass

    def good_stuff(self, character):
        pass
    
    def bad_stuff(self, character):
        character.level -= 3
  
