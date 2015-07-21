class Character(object):
    def __init__(self, name, color, level=1, strength=5, spirit=5, intellect=5):
        #This initializes basic Character traits
        self.name = name
        self.level = level
        self.bonus = 0
        self.char_class = "Classless"
        self.char_race = "Human"
        self.status = "Normal"
        self.color = color
        self.xp = 0
        self.xp_for_level = (100 + 50*level)
        #This initializes equipment (equipped items)
        self.equipment = {
            "headgear": [],
            "armor": [],
            "weapons": [],
            "footgear": [],
            "slotless": []
            }
        #This initializes equipment slots
        self.hand_slots = 2
        self.hand_slots_used = 0
        self.footgear_slots = 1
        self.footgear_slots_used = 0
        self.headgear_slots = 1
        self.headgear_slots_used = 0
        self.armor_slots = 1
        self.armor_slots_used = 0
        #This initializes backpack
        self.backpack_size = 25#revise later
        self.backpack = []
        #This initializes shrine (stored items)
        self.shrine = []

        #Your location determines your available actions, including which
        # items you can use.
        self.dimension = "temple"
    
        #This initializes your Attributes
        self.strength = strength
        self.spirit = spirit
        self.intellect = intellect
    
    def battle_strength_calc(self):
        bs = self.level + self.strength + self.spirit + self.intellect
        return bs
    
    def attr_up(self, attribute, amount):
        if attribute == "strength":
            self.strength += amount
            if self.strength < 0:
                self.strength = 0
        elif attribute == "spirit":
            self.spirit += amount
            if self.spirit < 0:
                self.spirit = 0
        elif attribute == "intellect":
            self.intellect += amount
            if self.intellect < 0:
                self.intellect = 0

    def level_up(self, amount):
        self.level += amount
        if self.level < 0:
            self.level = 0
        #TODO: is this where there should be a check to see if this can be the
        # game-winning level? Like maybe have it be def level_up(self, amount, win_ok = False),
        # and if it's an acceptable way to win, like with the xp-level-up below, it'd just
        # say self.level_up(1, win_ok = True) ?
        #TODO: Should the xp scaling per level work differently from this?
        self.xp = 0
        self.xp_for_level = (100 + 50*self.level)
    
    
    def xp_up(self, amount):
        while (self.xp + amount) >= self.xp_for_level:
            amount -= self.xp_for_level
            self.level_up(1)
        else:
            self.xp += amount
    
    def equip(self, equipment):
        #Should be able to check what type of object (e.g. footgear, slotless) the
        # equipment is, and if it's slotted check the self.(type)_slots vs the
        # self.(type)_slots_used to see if there's room to equip it.  If so, does.
        pass
      
    def unequip(self, equipment):
        #Checks to see if the equipment is equipped, and if so unequips it (it goes
        # in the backpack? or the closet?
        pass

    def chg_dimension(self, dim_name):
        #Sets the player's current dimension to the named dimension.  This will only
        # be called when it is allowed to be called.
        self.dimension = dim_name
