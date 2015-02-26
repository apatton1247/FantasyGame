class Monster(object):
  def __init__(self)
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
      
    def bad_stuff(self, battle_dict):
        for character in battle_dict["character"].keys():
            pass

    def update_monster(self, battle_dict):
        self.battle_strength = self.level

    def fight(self, battle_dict):
        pass

    def chase(self, battle_dict):
        pass

    def good_stuff(self, battle_dict):
        pass
