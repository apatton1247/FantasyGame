#Provides the user input options and basic ways to interact with it

class Options(object):
    def __init__(self):
        self.options = {"hidden": [], "visible": []}

    #Displays all "visible" options to the player
    def print_options(self):
        for option in self.options["visible"]:
            print(option.rjust(64))

    #Secret method for displaying all "hidden" options to the player
    def print_hidden_options(self):
        for option in self.options["hidden"]:
            print(option.rjust(64))

    #Adds an option (or list of options) to the options list. Second
    # parameter determines if the option is "visible" or "hidden".
    def add_option(self, option, visible_or_hidden):
        if type(option) == list:
            for entry in option:
                self.options[visible_or_hidden].append(entry)
        else:
            self.options[visible_or_hidden].append(option)

    #Deletes an option (or list of options) from the options list.
    def del_option(self, option, visible_or_hidden):
        if type(option) == list:
            for entry in option:
                if entry in self.options[visible_or_hidden]:
                    self.options[visible_or_hidden].remove(entry)
        else:
            if option in self.options[visible_or_hidden]:
                self.options[visible_or_hidden].remove(option)

    #Clears all options from the options list.
    def clear_options(self):
        self.options["hidden"] = []
        self.options["visible"] = []

    #Checks if an option is allowable? And does it? Maybe all the options
    # need to be classes unto themselves? But they should probably just
    # be methods if anything.  But how will the methods get the info that
    # they require to act on character or world objects or know if they
    # are allowed to be activated?
    def do_option(self, option_text):
        pass
