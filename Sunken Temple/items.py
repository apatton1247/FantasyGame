import gameplay
from races_and_classes import Human, Dwarf, Elf, Golem, Reptilian, Phantasm, Alien, Cyborg, Classless, Sorceror, Necromancer, Shaman, Druid, Telepath, Assassin, Warrior

class Items(object):
    """An overarching class for all item objects."""
    def __init__(self, item, name):
        item.name = name
    def __str__(self):
        return self.name
    def useable(self, character, gameplay, words):
        return True
    def use(self, character, gameplay, words):
        return "Item is not of a type that can be used"
    def equip(self, character, gameplay, words):
        return "Item is not of a type that can be equipped or unequipped"
    def unequip(self, character, gameplay, words):
        return "Item is not of a type that can be equipped or unequipped"

class Class_Race_Items(Items):
    """Items whose function is to change the player's race or class."""
    def __init__(self, item, name):
        Items.__init__(self, item, name)
        item.dimension = "Shrine"
        item.type = "class race item"

    def useable(self, character, game, words):
        if self.dimension in character.dimension.name:
            return True
        else:
            return False

class Enchanted_Flask_Of_Ale(Class_Race_Items):
    """The Enchanted Flask of Ale changes a player into a Dwarf."""
    def __init__(self):
        Class_Race_Items(self, "Enchanted Flask Of Ale")
    def use(self, character, gameplay, words):
        err_text = character.change_race(Dwarf)
        return err_text

class Magical_Flute(Class_Race_Items):
    """The Magical_Flute changes a player into an Elf."""
    def __init__(self):
        Class_Race_Items(self, "Magical Flute")
    def use(self, character, gameplay, words):
        err_text = character.change_race(Elf)
        return err_text
        
class Obsidian_Shard(Class_Race_Items):
    """The Obsidian Shard changes a player into a Golem."""
    def __init__(self):
        Class_Race_Items(self, "Obsidian Shard")
    def use(self, character, gameplay, words):
        err_text = character.change_race(Golem)
        return err_text
        
class Petrified_Egg(Class_Race_Items):
    """The Petrified Egg changes a player into a Reptilian."""
    def __init__(self):
        Class_Race_Items(self, "Petrified Egg")
    def use(self, character, gameplay, words):
        err_text = character.change_race(Reptilian)
        return err_text
        
class Dark_Orb(Class_Race_Items):
    """The Dark Orb changes a player into a Phantasm."""
    def __init__(self):
        Class_Race_Items(self, "Dark Orb")
    def use(self, character, gameplay, words):
        err_text = character.change_race(Phantasm)
        return err_text
        
class Strange_Moon_Rock(Class_Race_Items):
    """The Strange Moon Rock changes a player into an Alien."""
    def __init__(self):
        Class_Race_Items(self, "Strange Moon Rock")
    def use(self, character, gameplay, words):
        err_text = character.change_race(Alien)
        return err_text
        
class Vial_Of_Quicksilver(Class_Race_Items):
    """The Vial of Quicksilver changes a player into a Cyborg."""
    def __init__(self):
        Class_Race_Items(self, "Vial Of Quicksilver")
    def use(self, character, gameplay, words):
        err_text = character.change_race(Cyborg)
        return err_text
        
class Sorceror_Tome(Class_Race_Items):
    """The Sorceror Tome changes a player into a Sorceror."""
    def __init__(self):
        Class_Race_Items(self, "Sorceror Tome")
    def use(self, character, gameplay, words):
        err_text = character.change_class(Sorceror)
        return err_text
        
class Cursed_Skull(Class_Race_Items):
    """The Cursed Skull changes a player into a Necromancer."""
    def __init__(self):
        Class_Race_Items(self, "Cursed Skull")
    def use(self, character, gameplay, words):
        err_text = character.change_class(Necromancer)
        return err_text

class Ceremonial_Mask(Class_Race_Items):
    """The Ceremonial Mask changes a player into a Shaman."""
    def __init__(self):
        Class_Race_Items(self, "Ceremonial Mask")
    def use(self, character, gameplay, words):
        err_text = character.change_class(Shaman)
        return err_text

class Herbal_Potion(Class_Race_Items):
    """The Herbal Potion changes a player into a Druid."""
    def __init__(self):
        Class_Race_Items(self, "Herbal Potion")
    def use(self, character, gameplay, words):
        err_text = character.change_class(Druid)
        return err_text

class Mystic_Crystal(Class_Race_Items):
    """The Mystic Crystal changes a player into a Telepath."""
    def __init__(self):
        Class_Race_Items(self, "Mystic Crystal")
    def use(self, character, gameplay, words):
        err_text = character.change_class(Telepath)
        return err_text

class Blood_Oath_Contract(Class_Race_Items):
    """The Blood Oath Contract changes a player into an Assassin."""
    def __init__(self):
        Class_Race_Items(self, "Blood Oath Contract")
    def use(self, character, gameplay, words):
        err_text = character.change_class(Assassin)
        return err_text

class War_Horn(Class_Race_Items):
    """The War Horn changes a player into a Warrior."""
    def __init__(self):
        Class_Race_Items(self, "War Horn")
    def use(self, character, gameplay, words):
        err_text = character.change_class(Warrior)
        return err_text

class Bone(Items):
    """A bone earned from defeating a monster in combat."""
    #After you defeat a monster, you earn a certain percentage of experience,
    # and you may loot the corpse for treasure and bone(s).  If you take a
    # bone to the shrine, you can use the bone as a sacrificial offering to
    # earn an additional 50 XP (Shamans earn additional XP (75?)).
    # In battle, Necromancers may use any bones they're carrying to summon
    # skeletons, which boost the Necromancer's battle strength. (perhaps they
    # also gain some battle strength as a passive ability based on the number
    # of bones they have?)
    def __init__(self):
        Items(self, "Bone")
    def useable(self, character, gameplay, words):
        if "Shrine" in character.dimension.name:
            return True
        else:
            return False
    def use(self, character, gameplay, words):
        #Should the words that the player types be of the form 'sacrifice (number) bone(s)?'
        # This method could be where we parse the words to understand the intent.
        if str(character.char_class) == "Shaman":
            character.xp_up(75)
        else:
            character.xp_up(50)

class Equipment(Items):
    """Items, like armor and headgear, that a player can equip onto their body, and have constant/continuous effects."""
    def __init__(self, item, name):
        Items(item, name)
        item.type = "equipment"

class Base_Headgear(Equipment):
    """Generic headgear, off of which all specialized headgear is based."""
    def __init__(self):
        Equipment(self, "Base Headgear")
    def equip(self):
        pass
    def unequip(self):
        pass

class Base_Armor(Equipment):
    """Generic armor, off of which all specialized armor is based."""
    def __init__(self):
        Equipment(self, "Base Armor")
    def equip(self):
        pass
    def unequip(self):
        pass

class Base_Footgear(Equipment):
    """Generic footgear, off of which all specialized footgear is based."""
    def __init__(self):
        Equipment(self, "Base Footgear")
    def equip(self):
        pass
    def unequip(self):
        pass

class Base_Weapon(Equipment):
    """Generic weapon, off of which all specialized weapon is based."""
    def __init__(self):
        Equipment(self, "Base Weapon")
    def equip(self):
        pass
    def unequip(self):
        pass

class Base_Slotless(Equipment):
    """Generic slotless equipment, off of which all specialized slotless equipment is based."""
    def __init__(self):
        Equipment(self, "Base Slotless")
    def equip(self):
        pass
    def unequip(self):
        pass
