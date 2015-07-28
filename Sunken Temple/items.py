import gameplay
from races import Human, Dwarf, Elf, Golem, Reptilian, Phantasm, Alien, Cyborg
from classes import Classless, Sorceror, Necromancer, Shaman, Druid, Telepath, Assassin, Warrior

class Items(object):
    """An overarching class for all item objects."""
    def __init__(self, name):
        self.name = name

    def chg_char_class(char, char_class):
        for player in gameplay.players:
            if char == player.name.lower():
                player.char_class = char_class

    def chg_char_race(char, char_race):
        for player in gameplay.players:
            if char == player.name.lower():
                player.char_race = char_race
                
class Class_Race_Items(Items):
    """Items whose function is to change the player's race or class."""
    def __init__(self, name):
        Items.__init__(self, name)
        self.dimensions = ["Shrine"]

    def useable(self, game, character, words):
        if character.dimension in self.dimensions:
            return True
        else:
            return False

class Enchanted_Flask_Of_Ale(Class_Race_Items):
    """The Enchanted Flask of Ale changes a player into a Dwarf."""
    def __init__(self):
        Class_Race_Items(self, "Enchanted Flask of Ale")
    def use(self, gameplay, character, words):
        character.char_race = Dwarf()

class Magical_Flute(Class_Race_Items):
    """The Magical_Flute changes a player into an Elf."""
    def __init__(self):
        Class_Race_Items(self, "Magical Flute")
    def use(self, gameplay, character, words):
        character.char_race = Elf()

class Obsidian_Shard(Class_Race_Items):
    """The Obsidian Shard changes a player into a Golem."""
    def __init__(self):
        Class_Race_Items(self, "Obsidian Shard")
    def use(self, gameplay, character, words):
        character.char_race = Golem()

class Petrified_Egg(Class_Race_Items):
    """The Petrified Egg changes a player into a Reptilian."""
    def __init__(self):
        Class_Race_Items(self, "Petrified Egg")
    def use(self, gameplay, character, words):
        character.char_race = Reptilian()

class Dark_Orb(Class_Race_Items):
    """The Dark Orb changes a player into a Phantasm."""
    def __init__(self):
        Class_Race_Items(self, "Dark Orb")
    def use(self, gameplay, character, words):
        character.char_race = Phantasm()

class Strange_Moon_Rock(Class_Race_Items):
    """The Strange Moon Rock changes a player into an Alien."""
    def __init__(self):
        Class_Race_Items(self, "Strange Moon Rock")
    def use(self, gameplay, character, words):
        character.char_race = Alien()

class Vial_Of_Quicksilver(Class_Race_Items):
    """The Vial of Quicksilver changes a player into a Cyborg."""
    def __init__(self):
        Class_Race_Items(self, "Vial of Quicksilver")
    def use(self, gameplay, character, words):
        character.char_race = Cyborg()

class Sorcerors_Tome(Class_Race_Items):
    """The Sorceror's Tome changes a player into a Sorceror."""
    def __init__(self):
        Class_Race_Items(self, "Sorceror's Tome")
    def use(self, gameplay, character, words):
        character.char_class = Sorceror()

class Cursed_Skull(Class_Race_Items):
    """The Cursed Skull changes a player into a Necromancer."""
    def __init__(self):
        Class_Race_Items(self, "Cursed Skull")
    def use(self, gameplay, character, words):
        character.char_class = Necromancer()

class Ceremonial_Mask(Class_Race_Items):
    """The Ceremonial Mask changes a player into a Shaman."""
    def __init__(self):
        Class_Race_Items(self, "Ceremonial Mask")
    def use(self, gameplay, character, words):
        character.char_class = Shaman()

class Herbal_Potion(Class_Race_Items):
    """The Herbal Potion changes a player into a Druid."""
    def __init__(self):
        Class_Race_Items(self, "Herbal Potion")
    def use(self, gameplay, character, words):
        character.char_class = Druid()

class Mystic_Crystal(Class_Race_Items):
    """The Mystic Crystal changes a player into a Telepath."""
    def __init__(self):
        Class_Race_Items(self, "Mystic Crystal")
    def use(self, gameplay, character, words):
        character.char_class = Telepath()

class Blood_Oath_Contract(Class_Race_Items):
    """The Blood Oath Contract changes a player into an Assassin."""
    def __init__(self):
        Class_Race_Items(self, "Blood Oath Contract")
    def use(self, gameplay, character, words):
        character.char_class = Assassin()

class War_Horn(Class_Race_Items):
    """The War Horn changes a player into a Warrior."""
    def __init__(self):
        Class_Race_Items(self, "War Horn")
    def use(self, gameplay, character, words):
        character.char_class = Warrior()

