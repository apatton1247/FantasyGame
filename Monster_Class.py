class Monster(object):
  def __init__(self, name, level, description, bias, undead, plant, speed,
               fight_method, chase_method,
               bad_stuff_description, bad_stuff_method,
               good_stuff_method, level_rewarded, treasure_rewarded):
    self.type = "monster"
    self.name = name
    self.level = level
    self.description = description
    self.bias = bias
    self.undead = undead
    self.plant = plant
    self.speed = speed
    
    self.fight_method = fight_method
    self.chase_method = chase_method
    
    self.bad_stuff_description = bad_stuff_description
    self.bad_stuff_method = bad_stuff_method

    self.good_stuff_method = good_stuff_method
    self.level_rewarded = level_rewarded
    self.treasure_rewarded = treasure_rewarded
