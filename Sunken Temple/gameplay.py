#At this early point, gameplay just has a list of characters that get created at
# runtime, and calls the char_stats frame creator/populator for each.

import random
from character_class import Character
import gui as g
from matplotlib.animation import FuncAnimation
import options

class New_Game():
    def __init__(self):
        self.players = []
        self.whose_turn = None
        self.colorbank = ["coral", "darkolivegreen", "dodgerblue", "darkviolet",
                          "orangered", "darkslategray", "dimgray", "salmon", "sienna",
                          "goldenrod", "yellow", "black"]
        self.gui = g.Gui(self)
        self.opt = options.Options(self)
        self.opt.populate()
        self.all_dimensions = {"temple", "shrine", "guardian"}
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
        for player in self.players:
            if player.name.lower() == name:
                self.players.remove(player)
                #Need to change what self.gui.char_shown shows now.
                #Also need to make sure players can only remove themselves.
                break

    def get_player(self, name):
        for player in self.players:
            if player.name.lower() == name:
                return player

    def text_parse(self, text_string):
        text_string = text_string.lower()
        text_string = text_string.replace("'", " ").strip()
        #TODO: look into regex to split properly around punctuation,
        # including apostrophes, periods, etc.
        self.opt.interpret(text_string)

if __name__ == "__main__":
    game = New_Game()
    game.gui.char_shown = Character("", color = "white")

    game.gui_ani = FuncAnimation(game.gui.plot_fig, game.gui.animate, 50000)
    game.gui.mainloop()
