class Items(object):
"""An overarching class for all item objects."""
    def __init__(self, name):
        self.name = name
    
class Class_Race_Items(Items):
"""Items whose function is to change the player's race or class."""
    def __init__(self, name):
        Items.__init__(self, name)
        self.dimensions = ["shrine"]
