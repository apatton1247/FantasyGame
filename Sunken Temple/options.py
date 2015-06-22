#Provides the user input options and basic ways to interact with it

class Options(object):
    def __init__(self, gameplay):
        self.gameplay = gameplay
        self.options = {"hidden": [], "visible": []}

    #Displays all "visible" options to the player
    def print_options(self):
        for option in self.options["visible"]:
            gameplay.gui.write(option.rjust(64))

    #Secret method for displaying all "hidden" options to the player
    def print_hidden_options(self):
        for option in self.options["hidden"]:
            gameplay.gui.write(option.rjust(64))

    #Adds an option (or list of options) to the options list. Second
    # parameter determines if the option is "visible" or "hidden".
    def add_option(self, *option, visible_or_hidden):
        for entry in option:
            self.options[visible_or_hidden].append(entry)
        
    #Deletes an option (or list of options) from the options list.
    def del_option(self, *option, visible_or_hidden):
        for entry in option:
            if entry in self.options[visible_or_hidden]:
                self.options[visible_or_hidden].remove(entry)
        
    #Clears all options from the options list.
    def clear_options(self):
        self.options["hidden"] = []
        self.options["visible"] = []

    #All the options should probably just be methods of the Options class/
    # instance.  They will get the required access to things in-game or the
    # gui by going through self.gameplay.
    
    #def do_option(self, option_text):
    #    pass
    #
    #do_option is now deprecated in favor of option methods, like show_char_stats

    def interpret(self, *words):
        if len(words) > 1 and words[0] in ("look", "see", "show", "view"):
            name_set = set(words) & {player.name.lower() for player in self.gameplay.players}
            if len(name_set) > 1:
                self.gameplay.gui.write(text = "\nI don't understand, too many names!")
            elif len(name_set) == 1:
                name = name_set.pop()
                self.gameplay.gui.show_char_stats(name)
            else:
                return 2
