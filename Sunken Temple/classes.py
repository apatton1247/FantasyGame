class Char_Class():
    def __str__(self):
        return self.__class__.__name__

class Classless(Char_Class):
    def __init__(self):
        self.powers = {}
        pass
    def battle_calc(self, strength, intellect, spirit):
        return (strength + intellect + spirit)

class Sorceror(Char_Class):
    def __init__(self):
        self.powers = {"Lightning Bolt", "Fire Ball"}
        pass
    def battle_calc(self, strength, intellect, spirit):
        return (strength + 2*intellect + int(1.5*spirit))
    def lightning_bolt(self):
        pass
    def fire_ball(self):
        pass

class Necromancer(Char_Class):
    def __init__(self):
        self.powers = {"Icy Touch", "Summon"}
        pass
    def battle_calc(self, strength, intellect, spirit):
        return (strength + int(.5*spirit) + 2*intellect)
    def icy_touch(self):
        pass
    def summon(self):
        pass

class Shaman(Char_Class):
    def __init__(self):
        self.powers = {"Sacrifice", "Summon"}
        return (int(1.5*strength) + 2*spirit + intellect)
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
        return (strength + 3*spirit + intellect)
    def in_tune_with_nature(self):
        pass
    def growth(self):
        pass

class Telepath(Char_Class):
    def __init__(self):
        self.powers = {"Third Eye", "Foresight"}
        pass
    def battle_calc(self, strength, intellect, spirit):
        return (strength + spirit + 3*intellect)
    def third_eye(self):
        pass
    def foresight(self):
        pass

class Assassin(Char_Class):
    def __init__(self):
        self.powers = {"Stealth", "Master Of Disguise", "Theft", "Hidden Blade"}
        pass
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
        pass
    def battle_calc(self, strength, intellect, spirit):
        return (3*strength + spirit + intellect)
    def strength(self):
        pass

    
