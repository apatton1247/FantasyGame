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
        #Initializes equipment (equipped items), which is of the form:
        # equipment_type: [total_slots_of_this_type, [equipped_item_1, equipped_item_2 ...]]
        self.equipment = {
            "headgear": [1, []],
            "armor": [1, []],
            "weapons": [2, []],
            "footgear": [1, []],
            "slotless": [65536, []]
            }
        #This initializes backpack (carried, unequipped items), which is of
        # the same form as an equipment entry.
        self.backpack = [25, []]
        #This initializes shrine (stored items)
        self.shrine = []
        #This initializes gem pouch
        self.gems = {"ruby": 0, "citrine": 0, "topaz": 0, "emerald": 0,
                     "sapphire": 0, "amethyst": 0, "diamond": 0}

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

    def add_gems(self, gem_dict):
    #Adds gems to the player's gem pouch.
        for gem in gem_dict:
            self.gems[gem] += gem_dict[gem]

    def rem_gems(self, gem_dict):
    #Removes gems from the player's pouch.
#TODO: Does this need to do something special if they don't have the proper number
    # of gems they're asking to remove?
        for gem in gem_dict:
            gem_dict[gem] = -1*(gem_dict[gem])
        self.add_gems(gem_dict)

    def add_backpack(self, item):
    #Adds an item to the player's backpack.
        if len(self.backpack[1]) < self.backpack[0]:
            self.backpack[1].append(item)
        else:
            #TODO: This may be where we want to do checking to see if the player's backpack
            # can hold more items, or if they have to choose which items to leave behind.
            pass

    def rem_backpack(self, item):
    #Removes an item from the player's backpack.
        if item in self.backpack[1]:
            self.backpack.remove(item)

    def add_shrine(self, item):
    #Adds an item from the player's equipment or backpack to the shrine.
        if item in self.backpack[1]:
            self.backpack[1].remove(item)
            self.shrine.append(item)
        else:
            location = equipment_loc(item)
            if location:
                self.equipment[location][1].remove(item)
                self.shrine.append(item)

    def rem_shrine(self, item):
    #Removes an item from the player's shrine.  Is this the equivalent of a player throwing
    # the item away?
        if item in self.shrine:
            self.shrine.remove(item)
            
    def equipment_loc(self, item):
    #If a specified piece of equipment exists in the player's equipment, gives its location.
    #Else it returns an empty string.
        location = ""
        for equipment_type in self.equipment:
            for eq_item in self.equipment[equipment_type][1]:
                if item == eq_item:
                    location = equipment_type
        return location

    def chg_dimension(self, dim_name):
    #Sets the player's current dimension to the named dimension.  This will only
    # be called when it is allowed to be called.
        self.dimension = dim_name
