#Character class only included in the gameplay main file until we figure out how to import
# it correctly from another .py file in the same folder or something.
class Character(object):
  def __init__(self, name):
    #This initializes basic Character traits
    self.name = name
    self.level = 1
    self.bonus = 0
    self.char_class = ["normal"]
    self.char_race = ["human"]
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
    self.big_item_slots = 1
    self.big_item_slots_used = 0
    #This initializes backpack (hand)
    self.backpack_size = 25#revise later
    self.backpack = []
    #This initializes closet (unequipped items)
    self.shrine = []

  def equip(equipment):
    pass
  
  def unequip(equipment):
    pass
