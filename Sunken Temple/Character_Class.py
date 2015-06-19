class Character(object):
  def __init__(self, name, color, level=1, strength=5, spirit=5, intellect=5):
    #This initializes basic Character traits
    self.name = name
    self.level = level
    self.bonus = 0
    self.char_class = ["normal"]
    self.char_race = ["human"]
    self.status = "Normal"
    self.color = color
    self.xp = 0
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
    #This initializes backpack (hand)
    self.backpack_size = 25#revise later
    self.backpack = []
    #This initializes closet (unequipped items)
    self.shrine = []

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
    elif attribute == "spirit":
      self.spirit += amount
    elif attribute == "intellect":
      self.intellect += amount

  def level_up(self, amount):
    self.level += amount

  def equip(self, equipment):
    #Should be able to check what type of object (e.g. footgear, slotless) the
    # equipment is, and if it's slotted check the self.(type)_slots vs the
    # self.(type)_slots_used to see if there's room to equip it.  If so, does.
    pass
  
  def unequip(self, equipment):
    #Checks to see if the equipment is equipped, and if so unequips it (it goes
    # in the backpack? or the closet?
    pass
