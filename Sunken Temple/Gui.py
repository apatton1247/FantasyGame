import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt

from tkinter import *
#import Gameplay as game

class Gui(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.root = Frame(self)
        self.root.pack(side = "top", fill = "both", expand = True)
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (width, height))
        self.resizable(width=FALSE, height=FALSE)
        #print(width, height)
        
        self.create_widgets(height, width)
        Tk.wm_title(self, "Sunken Temple")

        #self.game = game.New()
        self.mainloop()

    def write(self, event, *text):
        if text:
            for line in text:
                self.output_text.set(self.output_text.get() + line)
        else:
            self.output_text.set(self.output_text.get() + "\n" + self.input_text.get())
        self.input_text.set("")

    def char_stats(self):
        #For future implementation
        #char_stats_stack = Frame(self.root)
        #for player in game.players:
        #(pull stats from player, like player.strength, player.spirit, player.name, etc)
        #name = StringVar(); name.set(player.name)
#TODO: Once we get to animating the matplotlib objects, we should use that function to update the player name/race/class/status text fields.
        
#TODO: Once we have multiple players's stats, this one's parent will be char_stats_stack
        char_stats = Frame(self.root)

        p_name = "Player 1"
        p_race = "Reptilian"
        p_class = "Shaman"
        p_status = "Confused"
        player_name_text = StringVar()
        player_name_text.set("%s\t%s\n%s %s " % (p_name, p_status, p_race, p_class)) 
        char_stats_name = Label(char_stats_stack, textvariable = player_name_text, width = 100, height = 2)
        char_stats_name.pack(side = "top")

        mid_frame = Frame(char_stats)

        p_level = 7
        p_color = "darkviolet"
        level_fig = Figure()
        level_bar = level_fig.add_subplot(111)
        level_bar.title("Level", fontsize = 20)
        level_bar.bar(0, p_level, color = p_color)
        level_bar.yaxis.set_major_locator(MultipleLocator(1))
        level_bar.yaxis.grid()
        

#TODO: Once we have multiple players's stats, this will return char_stats_stack
        return char_stats
        #pass

    def bg(self,win_height, win_width):
        self.bg_canvas = Canvas(self.root, height = win_height, width = win_width)
        self.bg_canvas.pack(expand = True, fill = "both")

        wall = PhotoImage(file = "crypt_wall_tessl.gif")
        self.bg_canvas.img = wall
        self.bg_canvas.create_image(0, 0, anchor = "nw", image = wall)

    def create_widgets(self, scr_height, scr_width):
        win_height = int(0.75 * scr_height)
        win_width = int(0.75 * scr_width)

        self.bg(win_height, win_width)
        
        self.input_text = StringVar()
        self.input_text.set("")
        entry = Entry(self.root, bg = "light gray", width = 60, font=("Arial", 16), textvariable = self.input_text, relief = "sunken")
        entry.bind("<Return>", self.write)

        self.output_text = StringVar()
        self.output_text.set("This is the sample text!\rHello World!")
        output_label = Label(self.root, bg = "light gray", anchor = "nw", width = 60, height = 18, font=("Arial", 16), relief = "sunken")
        output_label.config(textvariable = self.output_text, justify = "left")

        self.bg_canvas.create_window((win_width//4)+20, (win_height//8), anchor = "nw", window = output_label)
        self.bg_canvas.create_window((win_width//4)+20, (7*win_height//10), anchor = "nw", window = entry)

        stats_frame = Frame(self.root, height = 250, width = 250)
        stats_name = Label(stats_frame, width = 20, height = 2, justify = "left", anchor = "nw", bg = "light gray", font=("Arial",16), text = "Name\t   Status\nClass, Race", relief = "sunken")
        stats_mid_frame = Frame(stats_frame)
        stats_level_bar = Label(stats_mid_frame, width = 4, height = 6, justify = "left", anchor = "nw", bg = "light gray", font=("Arial",16), text = "L\ne\nv\ne\nl\n!", relief = "sunken")
        stats_pie_chart = Label(stats_mid_frame, width = 16, height = 6, bg = "light gray", font=("Arial",16), text = "Pie Chart\ngoes here!", relief = "sunken")
        stats_xp_bar = Label(stats_frame, width = 20, height = 2, bg = "light gray", font=("Arial",16), text = "Here is the\nXP bar!", relief = "sunken")

        stats_name.pack(side = "top")
        stats_level_bar.pack(side = "left")
        stats_pie_chart.pack(side = "left")
        stats_mid_frame.pack(side = "top")
        stats_xp_bar.pack(side = "top")

        self.bg_canvas.create_window((8*win_width/10), (win_height/4), anchor = "nw", window = stats_frame)

        
gui = Gui()
