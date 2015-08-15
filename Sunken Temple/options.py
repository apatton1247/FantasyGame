class Options():
    """Provides the user input options and basic ways to interact with it."""
    def __init__(self, gameplay):
        self.gameplay = gameplay
        self.options = {Show, Clear_Output, End_Turn, Strength_Up, Spirit_Up, Intellect_Up,
                        Level_Up, Xp_Up, Add_Player, Remove_Player, Enter, Use, Loot, Place}

    def get_options(self):
        return self.options

    def text_parse(self, player, words):
        #New interpret now that all options are classes and gameplay.whose_action is implemented.
        for opt in self.options:
            opt = opt()
            if opt.text in words:
                remaining_words = words.replace(opt.text, "").strip().split()
                if opt.useable(player, self.gameplay, remaining_words):
                    opt.use(player, self.gameplay, remaining_words)
                    break
        else:
            #Only executes if the words you typed don't contain a valid option.
            self.gameplay.gui.write(text = "Not a valid option.")
            Show().show_options(self.gameplay)
            
        
#################### Options Subclasses ####################

class Show(Options):
    """Displays information for the player to see. Depending on the player's input
    text, may show a character's stats, an ongoing encounter, or the player's valid
    options."""
    def __init__(self):
        self.visible = True
        self.text = "show"
        self.err_text = "Option should be of the form 'Show (character name/battle/options)'."
    def useable(self, player, gameplay, words):
        return True
    def use(self, player, gameplay, words):
        words = " ".join(words)
        if words == "options":
            self.show_options(gameplay)
        elif words == "hidden options":
            self.show_hidden_options(gameplay)
        elif words == "backpack":
            self.show_backpack(player, gameplay)
        elif words in {char.name.lower() for char in gameplay.players}:
            gameplay.gui.show_char_stats(words)
        #Can easily add elifs for battle (maybe even monster's name) or guardian game.
        else:
            gameplay.gui.write(text = self.err_text)

    def show_options(self, gameplay):
        opts = [option().text for option in gameplay.opt.get_options() if option().visible == True]
        gameplay.gui.options_text.set("\n".join(opts))

    #Secret method for displaying all "hidden" options to the player
    def show_hidden_options(self, gameplay):
        opts = [option().text for option in gameplay.opt.get_options() if option().visible == False]
        gameplay.gui.options_text.set("\n".join(opts))

    #Shows the player's backpack in the Options widget.
    def show_backpack(self, player, gameplay):
        backpack_items = [str(item) for item in player.backpack]
        gameplay.gui.options_text.set("\n".join(backpack_items))
        
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

class End_Turn(Options):
    """Scrolls through the turn order to the next player. At the moment, only the player whose turn it is may act."""
    def __init__(self):
        self.visible = False
        self.text = "end turn"
        self.err_text = "Option should be of the form 'End Turn'."
    def useable(self, player, gameplay, words):
        return True
    def use(self, player, gameplay, words):
        gameplay.next_turn(player)
        if not gameplay.whose_action:
            gameplay.gui.write(text = self.err_text)

class Strength_Up(Options):
    """Increases the strength of the character.  Mainly used, as an Option, for debugging.\nGiven the new method for calculating a player's attributes, this method is somewhat deprecated."""
    def __init__(self):
        self.visible = False
        self.text = "strength up"
        self.err_text = "Option should be of the form 'Strength up (amount)'."
    def useable(self, player, gameplay, words):
        return True
    def use(self, player, gameplay, words):
        if len(words) != 1:
            gameplay.gui.write(text = self.err_text)
        else:
            amt = words[0]
            player.attr_up("strength", int(amt))

class Spirit_Up(Options):
    """Increases the spirit of the character.  Mainly used, as an Option, for debugging.\nGiven the new method for calculating a player's attributes, this method is somewhat deprecated."""
    def __init__(self):
        self.visible = False
        self.text = "spirit up"
        self.err_text = "Option should be of the form 'Spirit up (amount)'."
    def useable(self, player, gameplay, words):
        return True
    def use(self, player, gameplay, words):
        if len(words) != 1:
            gameplay.gui.write(text = self.err_text)
        else:
            amt = words[0]
            player.attr_up("spirit", int(amt))

class Intellect_Up(Options):
    """Increases the intellect of the character.  Mainly used, as an Option, for debugging.\nGiven the new method for calculating a player's attributes, this method is somewhat deprecated."""
    def __init__(self):
        self.visible = False
        self.text = "intellect up"
        self.err_text = "Option should be of the form 'intellect up (amount)'."
    def useable(self, player, gameplay, words):
        return True
    def use(self, player, gameplay, words):
        if len(words) != 1:
            gameplay.gui.write(text = self.err_text)
        else:
            amt = words[0]
            player.attr_up("intellect", int(amt))

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
        if player.name == rem_name:
            gameplay.gui.write(text = self.err_text)
            return True
        #Should there be any other sort of stipulations about when you can/can't use this method?
        else:
            return False
    def use(self, player, gameplay, words):
        gameplay.remove_player(words.strip())
    
class Enter(Options):
    """A player enters a specified dimension."""
    def __init__(self):
        self.visible = True
        self.text = "enter"
        self.err_text = "Option should be of the form 'Enter (dimension name)'."
    def useable(self, player, gameplay, words):
        #We'll need some advanced criteria so that a player can enter the temple after a battle is over, but not during.  For now,
        return True
    def use(self, player, gameplay, words):
        dim_name = []
        for word in words:
            dim_name.append(word[0].upper() + word[1:])
        dim_name = " ".join(dim_name)
        if dim_name in gameplay.all_dimensions:
            player.chg_dimension(dim_name)
            gameplay.gui.write(text = player.name + " has entered the " + dim_name + " dimension!")
        else:
            gameplay.gui.write(text = "Unrecognizable dimension name.")

class Use(Options):
    """Allows a player to make use of a specified item or ability."""
    def __init__(self):
        self.visible = True
        self.text = "use"
        #TODO:  Need to finish the error text
        self.err_text = "Option should be of the form 'Use (item name / ability) (optional item/ability-dependent words)'."
    def useable(self, player, gameplay, words):
        return True
    def use(self, player, gameplay, words):
        words = " ".join(words)
        items_to_search = [item for item in player.backpack]
        if player.dimension == "Shrine":
            items_to_search += [item for item in player.shrine]
        for item in items_to_search:
            if item.name.lower() in words:
                words = words.replace(item.name.lower(), "")
                if item.useable(player, gameplay, words):
                    item.use(player, gameplay, words)
                    if item in player.backpack:
                        player.backpack.remove(item)
                    else:
                        player.shrine.remove(item)
                else:
                    gameplay.gui.write(text = "Item '" + item.name + "' not useable at this time.")
                #Probably shouldn't be more than one item called at a time. This will also preclude the abilities being searched.
                break
        else:
            #If there's no item that matches, they possibly wanted to use an ability. Code this later.
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
                player.backpack.add(item)

class Place(Options):
    """Allows a player to move an item from their backpack or equipment into their shrine.  Only available when a player is in their shrine."""
    def __init__(self):
        self.visible = True
        self.text = "place"
        self.err_text = "Option should be of the form 'Place (item name) in (location)'."
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
    """Players not in battle may put on their equipment from their backpack, or directly from in their Shrine."""
    pass

class Unequip(Options):
    """Players not in battle may take off their equipment and store it in their backpack, or directly in their Shrine."""
    pass
