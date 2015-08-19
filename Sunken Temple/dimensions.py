class Dimensions():
    def __init__(self, dim, name):
        dim.name = name
    def __str__(self):
        return self.name

class Shrine(Dimensions):
    def __init__(self, name):
        #TODO: this will change once only 1 shrine exists per personal_gameplay instance.
        Dimensions(self, name)
        self.contents = {}
    def __str__(self):
        return "The Shrine"
    def __contains__(self, item_name):
        for item in self.contents:
            if item.name == item_name:
                self.last_item = item
                return True
        else:
            return False
    def __iter__(self):
        return iter(self.contents.items())
    def add(self, item):
        existing_item = self.get_item(item.name)
        if existing_item:
            #If item already exists in shrine, just increment quantity.
            self.contents[existing_item] += 1
        else:
            #If it doesn't already exist, add item as a qty 1.
            self.contents[item] = 1
    def remove(self, item):
        #This method will only be called when it is possible to be called; checking
        # to see if the item is already in the shrine will be left up to the caller.
        #Decrements the quantity of a certain item, and if qty hits 0, deletes the item.
        self.contents[item] -= 1
        if self.contents[item] < 1:
            del(self.contents[item])
    def get_item(self, item_name):
        if item_name in self:
            return self.last_item
        else:
            return None

class Temple(Dimensions):
    def __init__(self):
        Dimensions(self, "The Temple")

class Guardian_Dimension(Dimensions):
    def __init__(self):
        Dimensions(self, "The Guardian Dimension")
