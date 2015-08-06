class Char_Race():
    def __str__(self):
        return self.__class__.__name__

class Human(Char_Race):
    def __init__(self):
        self.powers = {}
        pass
    def race_bonus_calc(self, player):
        return (player.strength + 1*player.level), (player.spirit), (player.intellect)

class Dwarf(Char_Race):
    def __init__(self):
        self.powers = {"Gem Finder"}
        pass
    def race_bonus_calc(self, player):
        return (player.strength + 1*player.level), (player.spirit), (player.intellect + 1*player.level)
    def gem_finder(self):
        pass

class Elf(Char_Race):
    def __init__(self):
        self.powers = {"Agility"}
        pass
    def race_bonus_calc(self, player):
        return (player.strength), (player.spirit+ 1*player.level), (player.intellect+ 1*player.level)
    def agility(self):
        pass

class Golem(Char_Race):
    def __init__(self):
        self.powers = {"Magic Resistance", "Volcanic Pressure", "Explode"}
        pass
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
        pass
    def race_bonus_calc(self, player):
        return (player.strength + 1*player.level), (player.spirit+ 1*player.level), (player.intellect)
    def predator(self):
        pass

class Phantasm(Char_Race):
    def __init__(self):
        self.powers = {"Wisp Of Smoke"}
        pass
    def race_bonus_calc(self, player):
        return (player.strength), (player.spirit + 2*player.level), (player.intellect)
    def wisp_of_smoke(self):
        pass

class Alien(Char_Race):
    def __init__(self):
        self.powers = {"Multiple Arms", "Flying"}
        pass
    def race_bonus_calc(self, player):
        return (player.strength), (player.spirit), (player.intellect + 2*player.level)
    def multiple_arms(self):
        pass
    def flying(self):
        pass

class Cyborg(Char_Race):
    def __init__(self):
        self.powers = {"Precision", "First Strike"}
        pass
    def race_bonus_calc(self, player):
        return (player.strength + 1*player.level), (player.spirit), (player.intellect + 1*player.level)
    def precision(self):
        pass
    def first_strike(self):
        pass
