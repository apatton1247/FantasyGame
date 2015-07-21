import gameplay

class Items(object):
"""An overarching class for all item objects."""
    def __init__(self, name):
        self.name = name

    def chg_char_class(char, char_class):
        for player in gameplay.players:
            if char = player.name.lower():
                player.char_class = char_class

    def chg_char_race(char, char_race):
        for player in gameplay.players:
            if char = player.name.lower():
                player.char_race = char_race
                
class Class_Race_Items(Items):
"""Items whose function is to change the player's race or class."""
    def __init__(self, name):
        Items.__init__(self, name)
        self.dimensions = ["shrine"]

    def use(self, char

class Enchanted_Flask_Of_Ale(Class_Race_Items):
"""The Enchanted Flask of Ale changes a player into a Dwarf."""
    def __init__(self):
        Class_Race_Items(self, "Enchanted Flask of Ale")

    
