############### RACES ###############
class Char_Race():
    def __str__(self):
        return self.__class__.__name__

class Human(Char_Race):
    def __init__(self):
        self.powers = {}
        self.class_combos = {Classless, Sorceror, Necromancer, Shaman, Druid, Telepath, Assassin, Warrior}
    def race_bonus_calc(self, player):
        return (player.strength + 1*player.level), (player.spirit), (player.intellect)

class Dwarf(Char_Race):
    def __init__(self):
        self.powers = {"Gem Finder"}
        self.class_combos = {Classless, Sorceror, Shaman, Warrior}
    def race_bonus_calc(self, player):
        return (player.strength + 1*player.level), (player.spirit), (player.intellect + 1*player.level)
    def gem_finder(self):
        pass

class Elf(Char_Race):
    def __init__(self):
        self.powers = {"Agility"}
        self.class_combos = {Classless, Sorceror, Necromancer, Druid}
    def race_bonus_calc(self, player):
        return (player.strength), (player.spirit+ 1*player.level), (player.intellect+ 1*player.level)
    def agility(self):
        pass

class Golem(Char_Race):
    def __init__(self):
        self.powers = {"Magic Resistance", "Volcanic Pressure", "Explode"}
        self.class_combos = {Classless, Shaman, Telepath, Warrior}
    def race_bonus_calc(self, player):
        return (player.strength + 2*player.level), (player.spirit), (player.intellect)
    def magic_resistance(self):
        pass
    def volcanic_pressure(self):
        pass
    def explode(self):
        pass

class Reptilian(Char_Race):
    def __init__(self):
        self.powers = {"Predator"}
        self.class_combos = {Classless, Necromancer, Shaman, Druid}
    def race_bonus_calc(self, player):
        return (player.strength + 1*player.level), (player.spirit+ 1*player.level), (player.intellect)
    def predator(self):
        pass

class Phantasm(Char_Race):
    def __init__(self):
        self.powers = {"Wisp Of Smoke"}
        self.class_combos = {Classless, Sorceror, Necromancer, Assassin}
    def race_bonus_calc(self, player):
        return (player.strength), (player.spirit + 2*player.level), (player.intellect)
    def wisp_of_smoke(self):
        pass

class Alien(Char_Race):
    def __init__(self):
        self.powers = {"Multiple Arms", "Flying"}
        self.class_combos = {Classless, Druid, Telepath, Assassin}
    def race_bonus_calc(self, player):
        return (player.strength), (player.spirit), (player.intellect + 2*player.level)
    def multiple_arms(self):
        pass
    def flying(self):
        pass

class Cyborg(Char_Race):
    def __init__(self):
        self.powers = {"Precision", "First Strike"}
        self.class_combos = {Classless, Telepath, Assassin, Warrior}
    def race_bonus_calc(self, player):
        return (player.strength + 1*player.level), (player.spirit), (player.intellect + 1*player.level)
    def precision(self):
        pass
    def first_strike(self):
        pass

############### CLASSES ###############
class Char_Class():
    def __str__(self):
        return self.__class__.__name__

class Classless(Char_Class):
    def __str__(self):
        return ""
    def __init__(self):
        self.powers = {}
        self.race_combos = {Human, Dwarf, Golem, Elf, Reptilian, Phantasm, Alien, Cyborg}
    def battle_calc(self, strength, intellect, spirit):
        return (strength + intellect + spirit)

class Sorceror(Char_Class):
    def __init__(self):
        self.powers = {"Lightning Bolt", "Fire Ball"}
        self.race_combos = {Human, Dwarf, Elf, Phantasm}
    def battle_calc(self, strength, intellect, spirit):
        return (strength + 2*intellect + int(1.5*spirit))
    def lightning_bolt(self):
        pass
    def fire_ball(self):
        pass

class Necromancer(Char_Class):
    def __init__(self):
        self.powers = {"Icy Touch", "Summon"}
        self.race_combos = {Human, Elf, Reptilian, Phantasm}
    def battle_calc(self, strength, intellect, spirit):
        return (strength + int(.5*spirit) + 2*intellect)
    def icy_touch(self):
        pass
    def summon(self):
        pass

class Shaman(Char_Class):
    def __init__(self):
        self.powers = {"Sacrifice", "Summon"}
        self.race_combos = {Human, Dwarf, Golem, Reptilian}
    def battle_calc(self, strength, intellect, spirit):
        return (int(1.5*strength) + 2*spirit + intellect)
    def sacrifice(self):
        pass
    def summon(self):
        pass

class Druid(Char_Class):
    def __init__(self):
        self.powers = {"In Tune With Nature", "Growth"}
        self.race_combos = {Human, Elf, Reptilian, Alien}
    def battle_calc(self, strength, intellect, spirit):
        return (strength + 3*spirit + intellect)
    def in_tune_with_nature(self):
        pass
    def growth(self):
        pass

class Telepath(Char_Class):
    def __init__(self):
        self.powers = {"Third Eye", "Foresight"}
        self.race_combos = {Human, Golem, Alien, Cyborg}
    def battle_calc(self, strength, intellect, spirit):
        return (strength + spirit + 3*intellect)
    def third_eye(self):
        pass
    def foresight(self):
        pass

class Assassin(Char_Class):
    def __init__(self):
        self.powers = {"Stealth", "Master Of Disguise", "Theft", "Hidden Blade"}
        self.race_combos = {Human, Phantasm, Alien, Cyborg}
    def battle_calc(self, strength, intellect, spirit):
        return (2*strength + spirit + int(1.5*intellect))
    def stealth(self):
        pass
    def master_of_disguise(self):
        pass
    def theft(self):
        pass
    def hidden_blade(self):
        pass

class Warrior(Char_Class):
    def __init__(self):
        self.powers = {"Strength"}
        self.race_combos = {Human, Dwarf, Golem, Cyborg}
    def battle_calc(self, strength, intellect, spirit):
        return (3*strength + spirit + intellect)
    def strength(self):
        pass
