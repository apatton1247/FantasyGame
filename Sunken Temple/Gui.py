import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib.ticker import MultipleLocator
from matplotlib.font_manager import FontProperties
import matplotlib.gridspec as gridspec

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

    def format_labels(self, pie_labels, pie_values):
        lab_and_val = zip(pie_labels, pie_values)
        lab_val_strings = []
        for pair in lab_and_val:
            new_pair = pair[0] + ": " + str(pair[1])
            lab_val_strings.append(new_pair)
        return lab_val_strings
    
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
        char_stats_name = Label(char_stats, textvariable = player_name_text, width = 30, height = 2)
        char_stats_name.pack(side = "top")

        mid_frame = Frame(char_stats)
        mid_frame.pack(side = "top")

        gs = gridspec.GridSpec(16,16, left = .075)
        p_level = 7
        p_color = "darkviolet"
        plot_fig = Figure(figsize = (6, 4))
        level_bar = plot_fig.add_subplot(gs[:14,0:3])
        level_bar.set_title(level_bar.get_title(), text = "Level", fontsize = 20)
        level_bar.bar(0, p_level, width = .1, color = p_color)
        level_bar.yaxis.set_major_locator(MultipleLocator(1))
        level_bar.yaxis.grid()
        level_bar.set_ylim(1, 11)
        level_bar.set_xlim(0, 0.1)
        level_bar.tick_params(axis = "x", top = "off", bottom = "off", labelbottom = "off")
        level_canvas = FigureCanvasTkAgg(plot_fig, mid_frame)
        level_canvas.show()
        level_canvas.get_tk_widget().pack(side = "left")

        pie_strength = 15
        pie_spirit = 2
        pie_intellect = 5
        char_battle_strength = 25
        pie_labels = ['Strength', 'Spirit', 'Intellect']
        pie_values = [pie_strength, pie_spirit, pie_intellect]
        pie_colors = ['FireBrick', 'Khaki', 'SteelBlue']
        pie_chart = plot_fig.add_subplot(gs[0:14,1:])
        pie_chart.pie(pie_values, colors = pie_colors, startangle = 90)
        pie_chart.axis("equal")
        pie_legend = pie_chart.legend(title="Attributes", labels= self.format_labels(pie_labels, pie_values),
                         framealpha = 0, loc=(.78, .01), fontsize=11)
        pie_legend.set_title(title = "Attributes", prop = FontProperties(size = 14))
        pie_chart.text(1.15, .60, str(char_battle_strength), bbox = dict(facecolor="none", pad=20), fontsize = 65)

        xp_owned = 250
        xp_for_level = 350
        xp_bar = plot_fig.add_subplot(gs[15:,:])
        xp_bar.barh(0, xp_owned, color = "lime")
        xp_bar.tick_params(axis = "y", left = "off", right = "off", labelleft = "off")
        xp_bar.set_ylabel("Xp", rotation='horizontal', fontsize=18)
        xp_bar.yaxis.set_label_coords(1.04, .1)
        xp_bar.set_xlim(0, xp_for_level)
        xp_bar.set_ylim(0, 0.8)

#TODO: Once we have multiple players's stats, this will return char_stats_stack
        return char_stats

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

        self.bg_canvas.create_window((win_width//6)+10, (win_height//8), anchor = "nw", window = output_label)
        self.bg_canvas.create_window((win_width//6)+10, (7*win_height//10), anchor = "nw", window = entry)

#        stats_frame = Frame(self.root, height = 250, width = 250)
#        stats_name = Label(stats_frame, width = 20, height = 2, justify = "left", anchor = "nw", bg = "light gray", font=("Arial",16), text = "Name\t   Status\nClass, Race", relief = "sunken")
#        stats_mid_frame = Frame(stats_frame)
#        stats_level_bar = Label(stats_mid_frame, width = 4, height = 6, justify = "left", anchor = "nw", bg = "light gray", font=("Arial",16), text = "L\ne\nv\ne\nl\n!", relief = "sunken")
#        stats_pie_chart = Label(stats_mid_frame, width = 16, height = 6, bg = "light gray", font=("Arial",16), text = "Pie Chart\ngoes here!", relief = "sunken")
#        stats_xp_bar = Label(stats_frame, width = 20, height = 2, bg = "light gray", font=("Arial",16), text = "Here is the\nXP bar!", relief = "sunken")

        char_stats_frame = self.char_stats()
        self.bg_canvas.create_window((7*win_width/10), (win_height/8), anchor = "nw", window = char_stats_frame)


#        stats_name.pack(side = "top")
#        stats_level_bar.pack(side = "left")
#        stats_pie_chart.pack(side = "left")
#        stats_mid_frame.pack(side = "top")
#        stats_xp_bar.pack(side = "top")
#        self.bg_canvas.create_window((8*win_width/10), (win_height/4), anchor = "nw", window = stats_frame)

        
gui = Gui()
