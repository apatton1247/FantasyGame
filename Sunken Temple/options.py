class Options(object):
    """Provides the user input options and basic ways to interact with it."""
    def __init__(self, gameplay):
        self.gameplay = gameplay
        self.options = {}

    def populate(self):
        self.add_option(**{"show": [self.show, "visible"],
                         "level up": [self.char_level_up, "hidden"],
                         "xp up": [self.char_xp_up, "hidden"],
                         "attr up": [self.char_attr_up, "hidden"],
                         "add player": [self.add_player, "hidden"],
                         "clear output": [self.clear_output, "hidden"]
                         "enter": [self.enter, "visible"]})

    #Displays all "visible" options to the player
    def show_options(self):
        opts = [option for option in self.options if self.options[option][1] == "visible"]
        self.gameplay.gui.options_text.set("\n".join(opts))

    #Secret method for displaying all "hidden" options to the player
    def show_hidden_options(self):
        opts = [option for option in self.options if self.options[option][1] == "hidden"]
        #print(opts)
        self.gameplay.gui.options_text.set("\n".join(opts))
        
    #Adds an option (or list of options) to the options list. Second
    # parameter determines if the option is "visible" or "hidden".
    def add_option(self, **option):
        for entry in option:
            self.options[entry] = option.get(entry)
        
    #Deletes an option (or list of options) from the options list.
    def del_option(self, **option):
        for entry in option:
            if entry in self.options:
                self.options.remove(entry)
        
    #Clears all options from the options list.
    def clear_options(self):
        self.options = {}

    def clear_output(self, words):
        self.gameplay.gui.clear_output()

    def show(self, words):
        words = " ".join(words)
        if words == "options":
            self.show_options()
        elif words == "hidden options":
            self.show_hidden_options()
        elif words in {player.name.lower() for player in self.gameplay.players}:
            self.gameplay.gui.show_char_stats(words)

    def char_attr_up(self, words):
        if len(words) != 3:
            self.gameplay.gui.write(text = "Option should be of the form 'attr up (attribute) (amount) (player name)'.")
        else:
            attr, amt, char = words
            for player in self.gameplay.players:
                if char == player.name.lower():
                    player.attr_up(attr, int(amt))
                    break

    def char_level_up(self, words):
        if len(words) != 2:
            self.gameplay.gui.write(text = "Option should be of the form 'level up (amount) (player name)'.")
        else:
            amt, char = words
            for player in self.gameplay.players:
                if char == player.name.lower():
                    player.level_up(int(amt))
                    break

    def char_xp_up(self, words):
        if len(words) != 2:
            self.gameplay.gui.write(text = "Option should be of the form 'xp up (amount) (player name)'.")
        else:
            amt, char = words
            for player in self.gameplay.players:
                if char == player.name.lower():
                    player.xp_up(int(amt))
                    break
                
    def add_player(self, words):
        if not len(words) == 1:
            self.gameplay.gui.write(text = "Option should be of the form 'add player (name)'.")
        else:
            name = words[0]
            name = name[0].upper() + name[1:]
            self.gameplay.add_player(name)

    def remove_player(self, words):
    #Remove a player, but make it so that it only works on the player's own turn.
        if len(words) != 1:
            self.gameplay.gui.write(text = "Option should be of the form 'remove player (name)'.")
        else:
            name = words[0]
            self.gameplay.remove_player(name)

    def enter(self, words):
    #Causes a player to enter a different dimension.  Here's where there will be any checking of
    # whether the move is allowed or possible.
        if len(words) == 0:
            self.gameplay.gui.write(text = "Option should be of the form 'enter (dimension name)'.")
        words = " ".join(words)
        if words not in self.gameplay.all_dimensions:
            self.gameplay.gui.write(text = "Unrecognizable dimension name.")
        else:
            #Should check here for whether the move is allowed (e.g. you can't teleport out of a battle into your shrine.)
            #Need to get the player whose turn it is and do this to them.
            pass

    def use(self, words):
    #Player uses the specified item.  Any remaining words must follow the item/item-type's rules.
        if len(words) == 0:
            self.gameplay.gui.write(text = "Option should be of the form 'use (item name) (optional qualifying words)'.")
        pass

    def interpret(self, words):
        opt_keys = {keywords for keywords in self.options}
        for key in opt_keys:
            if key in words:
                remaining_words = words.replace(key, "").strip().split()
                self.options[key][0](remaining_words)
        
