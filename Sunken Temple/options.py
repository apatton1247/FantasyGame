class Options():
    """Provides the user input options and basic ways to interact with it."""
    def __init__(self, gameplay):
        self.gameplay = gameplay
        self.options = {Show(self), Clear_Output(), End_Turn(), Strength_Up(), Spirit_Up(), Intellect_Up(),
                        Level_Up(), Xp_Up(), Add_Player(), Remove_Player(), Enter(), Use(), Loot(self),
                        Place(), Hide(self), Unhide(self)}
        self.last_shown = ""

    def get_options(self):
        return self.options

    def text_parse(self, player, words):
        #New interpret now that all options are classes and gameplay.whose_action is implemented.
        for opt in self.options:
            if opt.text in words:
                remaining_words = words.replace(opt.text, "").strip().split()
                if opt.useable(player, self.gameplay, remaining_words):
                    opt.use(player, self.gameplay, remaining_words)
                    break
        else:
            #Only executes if the words you typed don't contain a valid option.
            self.gameplay.gui.write(text = "Not a valid option.")

    def show_last(self):
        player = self.gameplay.whose_action
        Show(self).use(player, self.gameplay, self.last_shown)
        
        
#################### Options Subclasses ####################

class Show(Options):
    """Displays information for the player to see. Depending on the player's input
    text, may show a character's stats, an ongoing encounter, or the player's valid
    options."""
    def __init__(self, options):
        self.visible = True
        self.text = "show"
        self.err_text = "Option should be of the form 'Show (character name/battle/options)'."
        self.options = options
    def useable(self, player, gameplay, words):
        return True
    def use(self, player, gameplay, words):
        words = " ".join(words)
        if not words:
            self.show_none(player, gameplay)
        elif words == "options":
            self.show_options(player, gameplay)
        elif words == "hidden options":
            self.show_hidden_options(player, gameplay)
        elif words == "backpack":
            self.show_backpack(player, gameplay)
        elif words == "shrine":
            self.show_shrine(player, gameplay)
        elif words in {char.name.lower() for char in gameplay.players}:
            gameplay.gui.show_char_stats(words)
        #Can easily add elifs for battle (maybe even monster's name) or guardian game.
        else:
            gameplay.gui.write(text = self.err_text)

    def show_none(self, player, gameplay):
        gameplay.gui.options_text.set("")
        self.options.last_shown = ""
        
    def show_options(self, player, gameplay):
        opts = [option.text for option in gameplay.opt.get_options() if option.visible == True and option.useable(player, gameplay, "")]
        gameplay.gui.options_text.set("Options:\n" + "\n".join(opts))
        self.options.last_shown = "options".split()

    #Secret method for displaying all "hidden" options to the player
    def show_hidden_options(self, player, gameplay):
        opts = [option.text for option in gameplay.opt.get_options() if option.visible == False and option.useable(player, gameplay, "")]
        gameplay.gui.options_text.set("Hidden Options:\n" + "\n".join(opts))
        self.options.last_shown = "hidden options".split()
        
    #Shows the player's backpack in the Options widget.
    def show_backpack(self, player, gameplay):
        backpack_items = [(item.name + "   x" + str(qty)) for item, qty in player.backpack]
        for index, item in enumerate(backpack_items):
            if item[-2:] == "x1":
                backpack_items[index] = item[:-5]
        gameplay.gui.options_text.set("Backpack:\n" + "\n".join(backpack_items))
        self.options.last_shown = "backpack".split()
        
    def show_shrine(self, player, gameplay):
        if player.dimension == player.shrine:
            shrine_items = [(item.name + "   x" + str(qty)) for item, qty in player.shrine]
            for index, item in enumerate(shrine_items):
                if item[-2:] == "x1":
                    shrine_items[index] = item[:-5]
            gameplay.gui.options_text.set("Shrine:\n" + "\n".join(shrine_items))
            self.options.last_shown = "shrine".split()
        else:
            gameplay.gui.write(text = "You can only view Shrine contents from within your Shrine.")

class Hide(Options):
    """Hides the options and output screens."""
    def __init__(self, options):
        self.options = options
        self.visible = True
        self.text = "hide"
    def useable(self, player, gameplay, words):
        return True
    def use(self, player, gameplay, words):
        gameplay.gui.options_frame.lower()
        gameplay.gui.output_text.lower()
        
class Unhide(Options):
    """Unhides the options and output screens."""
    def __init__(self, options):
        self.options = options
        self.visible = True
        self.text = "unhide"
    def useable(self, player, gameplay, words):
        return True
    def use(self, player, gameplay, words):
        gameplay.gui.options_frame.lift()
        gameplay.gui.output_text.lift()
        
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
        #TODO:  Need to figure out what sort of test to run to make sure that you can't end your turn in the
        # middle of action, like inside a battle or in the middle of a trade.
        return True
    def use(self, player, gameplay, words):
        gameplay.next_turn(player)
        gameplay.gui.write(text = gameplay.whose_action.name + "'s turn:")
        gameplay.gui.options_text.set("")
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
        gameplay.gui.write(text = "Player " + name + " has joined the game!")

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
        if dim_name == "Shrine":
            dim_name = player.name + " Shrine"
        dim = gameplay.get_dim(dim_name)
        if dim:
            player.chg_dimension(dim)
            gameplay.gui.write(text = player.name + " has entered " + str(dim) + " dimension!")
        else:
            gameplay.gui.write(text = "Unrecognizable dimension name.")

class Use(Options):
    """Allows a player to make use of a specified item or ability."""
    def __init__(self):
        self.visible = True
        self.text = "use"
        self.err_text = "Option should be of the form 'Use (item name / ability) (optional item/ability-dependent words)'."
    def useable(self, player, gameplay, words):
        #Will this always be useable?
        return True
    def use(self, player, gameplay, words):
        words = " ".join(words)
        items_to_search = [item for item, qty in player.backpack]
        if "Shrine" in player.dimension.name:
            items_to_search += [item for item, qty in player.shrine]
        for item in items_to_search:
            if item.name.lower() in words:
                words = words.replace(item.name.lower(), "")
                if item.useable(player, gameplay, words):
                    err_text = item.use(player, gameplay, words)
                    if err_text:
                        gameplay.gui.write(text = err_text)
                    elif item.name in player.backpack:
                        player.backpack.remove(item)
                    else:
                        player.shrine.remove(item)
                else:
                    gameplay.gui.write(text = "Item '" + item.name + "' not useable at this time.")
                #Probably shouldn't be more than one item called at a time. This will also preclude the abilities being searched.
                break
        else:
            #If there's no item that matches, they possibly wanted to use an ability. Code this later.
            #Also may want to put ability-checking ahead of item-checking; there'll likely be fewer to check
            # and it could end up saving a lot of time.
            pass

class Loot(Options):
    def __init__(self, options):
        self.visible = True
        self.text = "loot"
        #This may need to change, right now just relies on "loot".
        self.err_text = "Option should be of the form 'Loot monster'."
        self.options = options
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
                self.options.last_shown = ["backpack"]
        #If no words other than "loot" are entered, there's nothing to say what to loot
        else:
            gameplay.gui.write(text = self.err_text)

class Place(Options):
    """Allows a player to move an item from their backpack or equipment into their shrine, and vice-versa.  Only available when a player is in their shrine."""
    def __init__(self):
        self.visible = True
        self.text = "place"
        self.err_text = "Option should be of the form 'Place (item name) in (shrine/backpack)'."
    def useable(self, player, gameplay, words):
        #TODO: We'll need to change this once dimensions have their own classes.
        if "Shrine" in player.dimension.name:
            return True
        else:
            return False
    def use(self, player, gameplay, words):
        #TODO: enable the "place (item name) in (shrine/backpack)" syntax.
        if " ".join(words[-2:]) == "in backpack":
            words = words[:-2]
            for index, word in enumerate(words):
                words[index] = word[0].upper() + word[1:]
            target_item_name = " ".join(words)
            if target_item_name in player.shrine:
                player.move_item(player.shrine, player.backpack)
        elif " ".join(words[-2:]) == "in shrine":
            words = words[:-2]
            for index, word in enumerate(words):
                words[index] = word[0].upper() + word[1:]
            target_item_name = " ".join(words)
            if target_item_name in player.backpack:
                player.move_item(player.backpack, player.shrine)
            elif target_item_name in player.equipment:
                player.move_item(player.equipment, player.shrine)
        else:
            gameplay.gui.write(text = self.err_text)


        


class Equip(Options):
    """Players not in battle may put on their equipment from their backpack, or directly from in their Shrine."""
    pass

class Unequip(Options):
    """Players not in battle may take off their equipment and store it in their backpack, or directly in their Shrine."""
    pass
