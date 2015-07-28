class Char_Race():
    def __str__(self):
        return self.__class__.__name__

class Human(Char_Race):
    def __init__(self):
        self.powers = {}
        pass
    def battle_calc(self, strength, intellect, spirit):
        pass

class Dwarf(Char_Race):
    def __init__(self):
        self.powers = {"Gem Finder"}
        pass
    def battle_calc(self, strength, intellect, spirit):
        pass
    def gem_finder(self):
        pass

class Elf(Char_Race):
    def __init__(self):
        self.powers = {"Agility"}
        pass
    def battle_calc(self, strength, intellect, spirit):
        pass
    def agility(self):
        pass

class Golem(Char_Race):
    def __init__(self):
        self.powers = {"Magic Resistance", "Volcanic Pressure", "Explode"}
        pass
    def battle_calc(self, strength, intellect, spirit):
        pass
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
    def battle_calc(self, strength, intellect, spirit):
        pass
    def predator(self):
        pass

class Phantasm(Char_Race):
    def __init__(self):
        self.powers = {"Wisp Of Smoke"}
        pass
    def battle_calc(self, strength, intellect, spirit):
        pass
    def wisp_of_smoke(self):
        pass

class Alien(Char_Race):
    def __init__(self):
        self.powers = {"Multiple Arms", "Flying"}
        pass
    def battle_calc(self, strength, intellect, spirit):
        pass
    def multiple_arms(self):
        pass
    def flying(self):
        pass

class Cyborg(Char_Race):
    def __init__(self):
        self.powers = {"Precision", "First Strike"}
        pass
    def battle_calc(self, strength, intellect, spirit):
        pass
    def precision(self):
        pass
    def first_strike(self):
        pass
