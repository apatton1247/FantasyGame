class Character(object):
  def __init__(self, name, gender):
    #This initializes basic Character traits
    self.name = name
    self.level = 0
    self.char_class = "normal"
    self.char_race = "human"
    self.gender = gender
    #This initializes equipment (equipped items)
    self.equipment = {}
    self.hand_slots = 2
    self.hand_slots_used = 0
    self.footgear_slots = 1
    self.footgear_slots_used = 0
    self.headgear_slots = 1
    self.headgear_slots_used = 0
    self.armor_slots = 1
    self.armor_slots_used = 0
    self.big_item_slots = 1
    self.big_item_slots_used = 0
    #This initializes backpack (hand)
    self.backpack_size = 5
    self.backpack = {}
    #This initializes closet (unequipped items)
    self.closet = {}
    #This initializes curses
    self.curses = {}
    self.bad_stuff = {}
    
    
    
