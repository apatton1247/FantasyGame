#Provides the user input options and basic ways to interact with it

class Options(object):
    def __init__(self):
        self.options = {"hidden": [], "visible": []}

    def print_options(self):
        for option in self.options["visible"]:
            print(option.rjust(64))

    def add_hidden(option):
        if option.type == list:
            pass
        else:
            self.options["hidden"].append(option)

    def add_visible(option):
        pass

    
