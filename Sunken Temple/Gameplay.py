#At this early point, gameplay just has a list of characters that get created at
# runtime, and calls the char_stats frame creator/populator for each.

import random
from Character_Class import Character
import Gui

players = []
colorbank = ["coral", "darkolivegreen", "dodgerblue", "darkviolet", "orangered", "darkslategray", "dimgray"]
gui = Gui.Gui()

def assign_color():
    color = random.choice(colorbank)
    colorbank.remove(color)
    return color

def add_player(name, **kwargs):
    p_color = assign_color()
    player = Character(name, color = p_color, **kwargs)
    players.append(player)
    gui.add_char_stats(player)

if __name__ == "__main__":
    add_player("Dave", level=8, strength=2, spirit=6, intellect=18)
    add_player("Victoria", level=6, strength=17, spirit=9, intellect=5)
    add_player("Frank")
