class Char_Class():
    def __str__(self):
        return self.__class__.__name__

class Classless(Char_Class):
    def __init__(self):
        self.powers = {}
        pass
    def battle_calc(self, strength, intellect, spirit):
        pass

class Sorceror(Char_Class):
    def __init__(self):
        self.powers = {"Lightning Bolt", "Fire Ball"}
        pass
    def battle_calc(self, strength, intellect, spirit):
        pass
    def lightning_bolt(self):
        pass
    def fire_ball(self):
        pass

class Necromancer(Char_Class):
    def __init__(self):
        self.powers = {"Icy Touch", "Summon"}
        pass
    def battle_calc(self, strength, intellect, spirit):
        pass
    def icy_touch(self):
        pass
    def summon(self):
        pass

class Shaman(Char_Class):
    def __init__(self):
        self.powers = {"Sacrifice", "Summon"}
        pass
    def battle_calc(self, strength, intellect, spirit):
        pass
    def sacrifice(self):
        pass
    def summon(self):
        pass

class Druid(Char_Class):
    def __init__(self):
        self.powers = {"In Tune With Nature", "Growth"}
        pass
    def battle_calc(self, strength, intellect, spirit):
        pass
    def in_tune_with_nature(self):
        pass
    def growth(self):
        pass

class Telepath(Char_Class):
    def __init__(self):
        self.powers = {"Third Eye", "Foresight"}
        pass
    def battle_calc(self, strength, intellect, spirit):
        pass
    def third_eye(self):
        pass
    def foresight(self):
        pass

class Assassin(Char_Class):
    def __init__(self):
        self.powers = {"Stealth", "Master Of Disguise", "Theft", "Hidden Blade"}
        pass
    def battle_calc(self, strength, intellect, spirit):
        pass
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
        pass
    def battle_calc(self, strength, intellect, spirit):
        pass
    def strength(self):
        pass

    
