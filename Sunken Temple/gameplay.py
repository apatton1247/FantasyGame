#At this early point, gameplay just has a list of characters that get created at
# runtime, and calls the char_stats frame creator/populator for each.

import random
from character_class import Character
import gui as g
import matplotlib.animation as animation
import options

class New_Game():
    def __init__(self):
        self.players = []
        self.colorbank = ["coral", "darkolivegreen", "dodgerblue", "darkviolet",
                          "orangered", "darkslategray", "dimgray", "salmon", "sienna",
                          "goldenrod", "yellow", "black"]
        self.gui = g.Gui(self)
        self.opt = options.Options(self)
        self.opt.populate()
        
    def assign_color(self):
        color = random.choice(self.colorbank)
        self.colorbank.remove(color)
        return color

    def add_player(self, name, **kwargs):
        p_color = self.assign_color()
        player = Character(name, color = p_color, **kwargs)
        self.players.append(player)
        self.gui.char_shown = player

    def text_parse(self, text_string):
        text_string = text_string.lower()
        text_string = text_string.replace("'", " ").strip()
        #TODO: look into regex to split properly around punctuation,
        # including apostrophes, periods, etc.
        self.opt.interpret(text_string)

if __name__ == "__main__":
    game = New_Game()
    game.add_player("Dave", level=8, strength=2, intellect=18)
    game.add_player("Victoria", level=6, strength=17, spirit=9)
    game.add_player("Frank", level=6, strength=3, intellect=20, spirit=12)

    game.gui_ani = animation.FuncAnimation(game.gui.plot_fig, game.gui.animate, 50000)
    game.gui.mainloop()
