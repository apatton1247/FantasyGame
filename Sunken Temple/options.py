class Options():
    """Provides the user input options and basic ways to interact with it."""
    def __init__(self, gameplay):
        self.gameplay = gameplay
        self.options = {}
        #Will be able to initialize self.options with instances of all the options
        # on startup, since they'll be classes external to the Options class and will
        # be defined once the options.py file is read into gameplay.py.

    #Won't need a populate method anymore (see above comment) once options are classes.
    def populate(self):
        self.options = {"show": [self.show, "visible"],
                        "level up": [self.char_level_up, "hidden"],
                        "xp up": [self.char_xp_up, "hidden"],
                        "attr up": [self.char_attr_up, "hidden"],
                        "add player": [self.add_player, "hidden"],
                        "clear output": [self.clear_output, "hidden"],
                        "enter": [self.enter, "visible"],
                        "use": [self.use, "visible"]}

    def text_parse(self, player, words):
        opt_keys = {keywords for keywords in self.options}
        for key in opt_keys:
            if key in words:
                remaining_words = words.replace(key, "").strip().split()
                self.options[key][0](player, remaining_words)
        #New interpret for once all options are classes and gameplay.whose_action is implemented.
        #for opt in self.options:
            #if opt.text in words:
                #remaining_words = words.replace(opt.text, "").strip().split()
                #if opt.useable(player, self.gameplay, remaining_words):
                    #opt.use(player, self.gameplay, remaining_words)
                    #break

        
    def show_options(self):
        opts = [option for option in self.options if self.options[option][1] == "visible"]
        self.gameplay.gui.options_text.set("\n".join(opts))

    #Secret method for displaying all "hidden" options to the player
    def show_hidden_options(self):
        opts = [option for option in self.options if self.options[option][1] == "hidden"]
        #print(opts)
        self.gameplay.gui.options_text.set("\n".join(opts))
        
    def clear_output(self, player, words):
        self.gameplay.gui.clear_output()

    def show(self, player, words):
        words = " ".join(words)
        if words == "options":
            self.show_options()
        elif words == "hidden options":
            self.show_hidden_options()
        elif words in {player.name.lower() for player in self.gameplay.players}:
            self.gameplay.gui.show_char_stats(words)

    def char_attr_up(self, player, words):
        if len(words) != 2:
            self.gameplay.gui.write(text = "Option should be of the form '(player name) attr up (attribute) (amount)'.")
        else:
            attr, amt = words
            player.attr_up(attr, int(amt))

    def char_level_up(self, player, words):
        if len(words) != 1:
            self.gameplay.gui.write(text = "Option should be of the form '(player name) level up (amount)'.")
        else:
            amt = int(words[0])
            player.level_up(int(amt))

    def char_xp_up(self, player, words):
        if len(words) != 1:
            self.gameplay.gui.write(text = "Option should be of the form '(player name) xp up (amount)'.")
        else:
            amt = int(words[0])
            player.xp_up(int(amt))
                
    def add_player(self, player, words):
        if not len(words) == 1:
            self.gameplay.gui.write(text = "Option should be of the form 'add player (name)'.")
        else:
            name = words[0]
            name = name[0].upper() + name[1:]
            self.gameplay.add_player(name)

    def remove_player(self, player, words):
    #Remove a player, but make it so that it only works on the player's own turn.
        if len(words) != 1:
            self.gameplay.gui.write(text = "Option should be of the form 'remove player (name)'.")
        else:
            name = words[0]
            if name == player.name.lower():
                self.gameplay.remove_player(name)

    def enter(self, player, words):
    #Causes a player to enter a different dimension.  Here's where there will be any checking of
    # whether the move is allowed or possible.
        if len(words) < 1:
            self.gameplay.gui.write(text = "Option should be of the form '(player name) enter (dimension name)'.")
        for index, word in enumerate(words):
            words[index] = word[0].upper() + word[1:]
        dim = " ".join(words[1:])
        if dim not in self.gameplay.all_dimensions:
            self.gameplay.gui.write(text = "Unrecognizable dimension name.")
        else:
            #Should check here for whether the move is allowed (e.g. you can't teleport out of a battle into your shrine.)
            #Need to get the player whose turn it is and do this to them.
            player.chg_dimension(dim)
            self.gameplay.gui.write(text = player.name + " has entered the " + dim + " dimension!")

    def use(self, player, words):
#TODO:  modify so that this can also activate race/class abilities!
    #Player uses the specified item.  Any remaining words must follow the item/item-type's rules.
        if len(words) == 0:
            self.gameplay.gui.write(text = "Option should be of the form '(player name) use (item name) (optional qualifying words)'.")
        words = " ".join(words)
        for item in player.backpack:
#TODO:  if the player is in the shrine, it should search the shrine's items too.
            if item.name in words:
                words = words.split()
                start = words.index(item.name.split()[0])
                #This will remove the words making up the item name, in order, from the
                # remaining words.
                for word in item.name.split():
                    words.pop(start)
                item_to_use = item
                #Probably won't/shouldn't be more than one item called at a time.
                break
        if item_to_use.useable(player, self.gameplay, words):
            item_to_use.use(player, self.gameplay, words)

    #Loots the body of a slain monster.  Internally, transforms items-as-text into item objects.
    def loot(self, player, words):
        pass

#################### Options Subclasses ####################

class Show(Options):
    """Displays information for the player to see. Depending on the player's input
    text, may show a character's stats, an ongoing encounter, or the player's valid
    options."""
    def __init__(self):
        self.visibile = True
        self.text = "show"
        self.err_text = "Option should be of the form 'Show (character name/battle/options)'."
    def useable(self, player, gameplay, words):
        return True
    def use(self, player, gameplay, words):
        words = " ".join(words)
        if words == "options":
            self.show_options()
        elif words == "hidden options":
            self.show_hidden_options()
        elif words in {char.name.lower() for char in self.gameplay.players}:
            gameplay.gui.show_char_stats(words)
        #Can easily add elifs for battle (maybe even monster's name) or guardian game.
        else:
            gameplay.gui.write(text = self.err_text)

    def show_options(self):
        opts = [option.text for option in self.options if option.visible == True]
        self.gameplay.gui.options_text.set("\n".join(opts))

    #Secret method for displaying all "hidden" options to the player
    def show_hidden_options(self):
        opts = [option.text for option in self.options if option.visible == False]
        self.gameplay.gui.options_text.set("\n".join(opts))

class Clear_Output(Options):
    """Clears the output screen.  Mainly used, as an Option, for debugging."""
    def __init__(self):
        self.visible = False
        self.text = "clear output"
        self.err_text = "Option should be of the form 'Clear output'."
    def useable(self, player, gameplay, words):
        return True
    def use(self, player, gameplay, words):
        gameplay.gui.clear_output()

class Set_Action(Options):
    """Manually sets the game's action to be a particular player's.  Mainly used, as an Option, for debugging."""
    def __init__(self):
        self.visible = False
        self.text = "set action"
        self.err_text = "Option should be of the form 'Set action (player name)'."
    def useable(self, player, gameplay, words):
        return True
    def use(self, player, gameplay, words):
        gameplay.whose_action = gameplay.get_player(" ".join(words))
        if not gameplay.whose_action:
            gameplay.gui.write(text = self.err_text)

class Attr_Up(Options):
    """Increases the strength, spirit, or intellect of the character.  Mainly used, as an Option, for debugging.\nGiven the new method for calculating a player's attributes, this method is somewhat deprecated."""
    def __init__(self):
        self.visible = False
        self.text = "attr up"
        self.err_text = "Option should be of the form '(player name) attr up (attribute) (amount)'."
    def useable(self, player, gameplay, words):
        return True
    def use(self, player, gameplay, words):
        if len(words) != 2:
            gameplay.gui.write(text = self.err_text)
        else:
            attr, amt = words
            player.attr_up(attr, int(amt))

class Level_Up(Options):
    """Increases the level of the character.  Mainly used, as an Option, for debugging."""
    def __init__(self):
        self.visible = False
        self.text = "level up"
        self.err_text = "Option should be of the form '(player name) level up (amount)'."
    def useable(self, player, gameplay, words):
        return True
    def use(self, player, gameplay, words):
        if len(words) != 1:
            gameplay.gui.write(text = self.err_text)
        else:
            amt = words[0]
            player.level_up(int(amt))

class Xp_Up(Options):
    """Increases the xp of the character.  Mainly used, as an Option, for debugging."""
    def __init__(self):
        self.visible = False
        self.text = "xp up"
        self.err_text = "Option should be of the form '(player name) xp up (amount)'."
    def useable(self, player, gameplay, words):
        return True
    def use(self, player, gameplay, words):
        if len(words) != 1:
            gameplay.gui.write(text = self.err_text)
        else:
            amt = words[0]
            player.xp_up(int(amt))

class Add_Player(Options):
    """Adds a player to the game."""
    def __init__(self):
        self.visible = False
        self.text = "add player"
        self.err_text = "Option should be of the form 'Add player (player name)'."
    def useable(self, player, gameplay, words):
        return True
    def use(self, player, gameplay, words):
        for index, word in enumerate(words):
            words[index] = word[0].upper() + word[1:]
        name = " ".join(words)
        gameplay.add_player(name)

class Remove_Player(Options):
    """Removes a player from the game. May only be used by the player who wishes to be removed."""
    def __init__(self):
        self.visible = False
        self.text = "remove player"
        self.err_text = "Option should be of the form 'Remove player (own name)'."
    def useable(self, player, gameplay, words):
        for index, word in enumerate(words):
            words[index] = word[0].upper() + word[1:]
        rem_name = " ".join(words)
        if not player.name == rem_name:
            gameplay.gui.write(text = self.err_text)
            return False
        #Should there be any other sort of stipulations about when you can/can't use this method?
        else:
            return True
    def use(self, player, gameplay, words):
        gameplay.remove_player(name)
    
class Enter(Options):
    """A player enters a specified dimension."""
    pass

class Use(Options):
    """Allows a player to make use of a specified item or ability."""
    pass

class Loot(Options):
    def __init__(self):
        self.visible = True
        self.text = "loot"
        #This may need to change, right now just relies on "loot".
        self.err_text = "Option should be of the form 'Loot monster'."
    def useable(self, player, gameplay, words):
        #TODO: determine when this is useable.  For now, it always is, for the purpose of the OP use-case below.
        return True
    def use(self, player, gameplay, words):
        #TODO: For now, if a player types 'loot (item name), they'll get a copy of that item for free.
        # Need to change this once we've tested item use so that only monster corpses can be looted.
        if words:
            words = " ".join(words)
            item = gameplay.item_initialize(words)
            if item:
                player.add_backpack(item)

class Put(Options):
    """Allows a player to move an item from their backpack or equipment into their shrine.  Only available when a player is in their shrine."""
    def __init__(self):
        self.visible = True
        self.text = "put"
        self.err_text = "Option should be of the form 'Put (item name) in shrine'."
    def useable(self, player, gameplay, words):
        #TODO: We'll need to change this once dimensions have their own classes.
        if player.dimension == "Shrine":
            return True
        else:
            return False
    def use(self, player, gameplay, words):
        for index, word in enumerate(words):
            words[index] = word[0].upper() + word[1:]
        target_item_name = " ".join(words)
        #TODO: Need to figure out a way to search equally for items and their names.
        for item in player.backpack:
            if target_item_name == item.name:
                player.add_shrine(item)
                break
        else:
            equip_loc = player.equipment_loc(item)
            if equip_loc:
                player.add_shrine(item)

class Equip(Options):
    pass

class Unequip(Options):
    pass
