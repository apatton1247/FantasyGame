#At this early point, gameplay just has a list of characters that get created at
# runtime, and calls the char_stats frame creator/populator for each.

import random
from character_class import Character
import gui as g

class New_Game():
    def __init__(self):
        self.players = []
        self.colorbank = ["coral", "darkolivegreen", "dodgerblue", "darkviolet", "orangered", "darkslategray", "dimgray"]
        self.gui = g.Gui(self)

    def assign_color(self):
        color = random.choice(self.colorbank)
        self.colorbank.remove(color)
        return color

    def add_player(self, name, **kwargs):
        p_color = self.assign_color()
        player = Character(name, color = p_color, **kwargs)
        self.players.append(player)
        self.gui.add_char_stats(player)

    def text_parse(self, text_string):
        text_string = text_string.lower()
        text_string.strip()
        #TODO: look into regex to split properly around punctuation, including
        #      apostrophes, periods, etc.
        words = text_string.split()
        if len(words) > 1 and words[0] in ("look", "see", "show", "view"):
            name_set = set(words) & {player.name.lower() for player in self.players}
            if len(name_set) > 1:
                self.gui.write(text = "\nI don't understand, too many names!")
            elif len(name_set) == 1:
                name = name_set.pop()
                self.gui.show_char_stats(name)
            else:
                return 2

if __name__ == "__main__":
    game = New_Game()
    game.add_player("Dave", level=8, strength=2, spirit=6, intellect=18)
    game.add_player("Victoria", level=6, strength=17, spirit=9, intellect=5)
    game.add_player("Frank")
