#At this early point, gameplay just has a list of characters that get created at
# runtime, and calls the char_stats frame creator/populator for each.

import random
from character_class import Character
import gui as g
from matplotlib.animation import FuncAnimation
import options
import items as items_module

class New_Game():
    def __init__(self):
        self.players = []
        self.whose_action = None
        self.colorbank = ["coral", "darkolivegreen", "dodgerblue", "darkviolet",
                          "orangered", "darkslategray", "dimgray", "salmon", "sienna",
                          "goldenrod", "yellow", "black"]
        self.gui = g.Gui(self)
        self.opt = options.Options(self)
        self.opt.populate()
        self.all_dimensions = {"Temple", "Shrine", "Temple Guardian Dimension"}
        #May revise what the guardian one is called, remember to add more.
        
    def assign_color(self):
        color = random.choice(self.colorbank)
        self.colorbank.remove(color)
        return color

    def add_player(self, name, **kwargs):
        p_color = self.assign_color()
        player = Character(name, color = p_color, **kwargs)
        self.players.append(player)
        self.gui.char_shown = player

    def remove_player(self, name):
        player = get_player(name)
        #Through the magic of list indexing using negative numbers, next_player is the
        # player immediately following the player who's removing themself from play.
        next_player = self.players[self.players.index(player) - (len(self.players)-1)]
        if player == self.gui.char_shown:
            self.gui.char_shown = next_player
        self.whose_action = next_player
        #Note: no provision currently made for the corner-case of there being only one
        # player who subsequently removes themself.
        #Maybe something to the effect of:
        #if not self.players:
        #    self.gui.char_shown = Character("", color = "white")
        self.players.remove(player)

    def get_player(self, name):
        for player in self.players:
            if player.name.lower() == name:
                return player
        else:
            return None

    def item_initialize(lower_case_item_name):
        item_name = []
        for word in lower_case_item_name.split():
            word = word[0].upper() + word[1:]
            item_name.append(word)
        item_name = " ".join(item_name)
        #This command gets the class of the item from items.py, and makes a new object from it.
        item = getattr(items_module, item_name, None)()
        return item

    def interpret(self, text_string):
        text_string = text_string.lower()
        text_string = text_string.replace("'", " ").strip()
        #TODO: look into regex to split properly around punctuation,
        # including apostrophes, periods, etc.
        player_name = text_string.split()[0]
        player = self.get_player(player_name)
        #Allows backwards compatibility with giving commands in third-person,
        # while also allowing an acting-player variable to be set, and reference
        # that variable in the same way we'll hope to do once we can use websockets.
        if player:
            self.opt.text_parse(player, text_string.replace(player_name, ""))
        else:
            self.opt.text_parse(self.whose_action, text_string)

if __name__ == "__main__":
    game = New_Game()
    game.gui.char_shown = Character("", color = "white")

    game.gui_ani = FuncAnimation(game.gui.plot_fig, game.gui.animate, 50000)
    game.gui.mainloop()
