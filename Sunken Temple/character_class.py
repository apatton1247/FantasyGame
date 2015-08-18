from dimensions import Shrine
from races import Human, Dwarf, Elf, Golem, Reptilian, Phantasm, Alien, Cyborg
from classes import Classless, Sorceror, Necromancer, Shaman, Druid, Telepath, Assassin, Warrior

class Character():
    def __init__(self, name, color, level=1, strength=5, spirit=5, intellect=5):
        #This initializes basic Character traits
        self.name = name
        self.level = level
        self.bonus = 0
        self.char_class = Classless()
        self.char_race = Human()
        self.status = "Normal"
        self.color = color
        self.xp = 0
        self.xp_for_level = (100 + 50*level)
        #Initializes equipment (equipped items)
        self.equipment = Equipment()
        #This initializes backpack (carried, unequipped items), which is of
        # the same form as an equipment entry.
        self.backpack = Backpack()
        #This initializes shrine (stored items)
        self.shrine = Shrine(self.name + " Shrine")
        #This initializes gem pouch
        self.gems = {"ruby": 0, "citrine": 0, "topaz": 0, "emerald": 0,
                     "sapphire": 0, "amethyst": 0, "diamond": 0}

        #Your location determines your available actions, including which
        # items you can use.
        self.dimension = None
    
        #This initializes your Attributes
        self.strength = strength
        self.spirit = spirit
        self.intellect = intellect
    
    def battle_strength_calc(self):
        bs = (self.level
             + self.char_class.battle_calc(self.strength, self.spirit, self.intellect)
             #+ self.dimension(self.strength + self.spirit + self.intellect)
             )
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

    def recalc_attr(self):
        #base attributes values
        self.strength = 5
        self.spirit = 5
        self.intellect = 5
        #TODO: add attributes that come from items
#        self.strength, self.spirit, self.intellect = self.equip_calc()
        #add attributes that come from race bonus
        self.strength, self.spirit, self.intellect = self.char_race.race_bonus_calc(self)

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
        self.recalc_attr()

    def change_race(self, new_race):
        self.char_race = new_race()
        self.recalc_attr()

    def change_class(self, new_class):
        self.char_class = new_class()
    
    def xp_up(self, amount):
        while (self.xp + amount) >= self.xp_for_level:
            amount -= self.xp_for_level
            self.level_up(1)
        else:
            self.xp += amount
    
    def add_gems(self, gem_dict):
    #Adds gems to the player's gem pouch.
        for gem in gem_dict:
            self.gems[gem] += gem_dict[gem]

    def rem_gems(self, gem_dict):
    #Removes gems from the player's pouch.
#TODO: Does this need to do something special if they don't have the proper number
    # of gems they're asking to remove?
        for gem in gem_dict:
            self.gems[gem] -= gem_dict[gem]

    def move_item(self, found_item_loc, new_item_loc):
    #Adds an item from the player's equipment or backpack to the shrine.
        item = found_item_loc.last_item
        found_item_loc.remove(item)
        new_item_loc.add(item)

    def drop_item(self, item):
    #Removes an item from the player's backpack; the equivalent of a player throwing
    # the item away.
        if item in self.backpack:
            self.backpack.remove(item)

    def chg_dimension(self, dim):
    #Sets the player's current dimension to the named dimension.  This will only
    # be called when it is allowed to be called.
        self.dimension = dim


class Backpack():
    """A backpack stores the player's unequipped items."""
    def __init__(self):
        self.size = 25
        self.contents = {}
    def __contains__(self, item_name):
        for item in self.contents:
            if item.name == item_name:
                self.last_item = item
                return True
        else:
            return False
    def __iter__(self):
        return iter(self.contents.items())
    def add(self, item):
        existing_item = self.get_item(item.name)
        if existing_item:
            #If item already exists in backpack, just increment quantity.
            self.contents[existing_item] += 1
        elif len(self.contents) >= self.size:
            #TODO: This is where we want to check to see if the player's backpack can
            # hold more items, or if they have to choose which items to leave behind.
            #What should happen at this point?  Some error message?
            pass
        else:
            #If it doesn't already exist but there's room, add item as a qty 1.
            self.contents[item] = 1
    def remove(self, item):
        #This method will only be called when it is possible to be called; checking
        # to see if the item is already in the backpack will be left up to the caller.
        #Decrements the quantity of a certain item, and if qty hits 0, deletes the item.
        existing_item = self.get_item(item.name)
        self.contents[existing_item] -= 1
        if self.contents[existing_item] < 1:
            del(self.contents[existing_item])
    def get_item(self, item_name):
        if item_name in self:
            return self.last_item
        else:
            return None
        
class Equipment():
    """The player's equipped items."""
    def __init__(self):
        self.headgear_slots = 1
        self.armor_slots = 1
        self.weapons_slots = 2
        self.footgear_slots = 1
        self.slotless = 65535
        self.headgear = []
        self.armor = []
        self.weapons = []
        self.footgear = []
        self.slotless = []
    def __contains__(self, item_name):
        for loc in (self.headgear, self.armor, self.weapons, self.footgear, self.slotless):
            for item in loc:
                if item.name == item_name:
                    #Sets these attributes as a sort of short-term equipment-memory for the last-found item.
                    self.last_item = item
                    self.last_loc = loc
                    return True
        else:
            return False
    def __iter__(self):
        pass
    def __next__(self):
        pass
    def add(self, item):
        #If item.type == "headgear", and len(self.headgear) < self.headgear_slots: self.headgear.append(item)
        pass
    def remove(self, item):
        #If item.type == "headgear", self.headgear.remove(item)
        pass
    def get_item(self, item_name):
        #TODO: If an object exists somewhere in the player's equipment, searching its name with this method
        # should return the object, and/or its location in equipment? Whichever would be more helpful.
        pass
