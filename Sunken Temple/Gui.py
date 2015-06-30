import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib.ticker import MultipleLocator
from matplotlib.font_manager import FontProperties
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import matplotlib.style as style

from tkinter import *

#style.use("ggplot")

class Gui(Tk):
    def __init__(self, game):
        Tk.__init__(self)
        self.game = game
        self.root = Frame(self)
        self.root.pack(side = "top", fill = "both", expand = True)
        ####Top Level Frame Fixed and Resolution?####
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (width, height))
        self.resizable(width=FALSE, height=FALSE)
        
        self.create_widgets(height, width)
        Tk.wm_title(self, "Sunken Temple")

        #print("Hello")
        #self.mainloop()
        #print("bye!")

    def animate(interval):
        for character in self.char_stats:
            ####Player Label####
            p_name = character.name
            p_race = character.char_race
            p_class = character.char_class
            p_status = character.status
            player_name_text = StringVar()
            player_name_text.set("%s\t%s\n%s %s " % (p_name, p_status, p_race, p_class)) 
            char_stats_name = Label(char_stats_frame, textvariable = player_name_text, width = 30, height = 2)
            char_stats_name.pack(side = "top")

            lower_frame = Frame(char_stats_frame)
            lower_frame.pack(side = "top")
            
            gs = gridspec.GridSpec(32,32, left = .075)
            plot_fig = Figure(figsize = (5.5, 4))
            char_stats_canvas = FigureCanvasTkAgg(plot_fig, lower_frame)
            char_stats_canvas.show()
            char_stats_canvas.get_tk_widget().pack(side = "left")
            ####Battle Strength####
            bs = "25"
            bs_label = Label(lower_frame, text = bs, font=("Arial", 60))
            bs_label.pack(side = "right")
            char_stats_canvas.get_tk_widget().create_window(355, 25, anchor = "nw", window = bs_label)
            ####LEVEL####
            p_level = character.level
            p_color = character.color
            level_bar = plot_fig.add_subplot(gs[:28,0:4])
            level_bar.set_title(level_bar.get_title(), text = "Level", fontsize = 16)
            level_bar.bar(0, p_level, width = .1, color = p_color)
            level_bar.yaxis.set_major_locator(MultipleLocator(1))
            level_bar.yaxis.grid()
            level_bar.set_ylim(1, 11)
            level_bar.set_xlim(0, 0.1)
            level_bar.tick_params(axis = "x", top = "off", bottom = "off", labelbottom = "off")
            ####ATTRIBUTES####
            p_strength = character.strength
            p_spirit = character.spirit
            p_intellect = character.intellect
            p_battle_strength = character.battle_strength_calc()
            pie_labels = ['Strength', 'Spirit', 'Intellect']
            pie_values = [p_strength, p_spirit, p_intellect]
            pie_colors = ['FireBrick', 'Khaki', 'SteelBlue']
            pie_chart = plot_fig.add_subplot(gs[0:28,0:])
            pie_chart.pie(pie_values, colors = pie_colors, startangle = 90)
            pie_chart.axis("equal")
            pie_legend = pie_chart.legend(title="Attributes", labels= self.format_labels(pie_labels, pie_values),
                             framealpha = 0, loc=(.78, .01), fontsize=11)
            pie_legend.set_title(title = "Attributes", prop = FontProperties(size = 14))
            ####Experience####
            xp_owned = character.xp
            xp_for_level = 350
            xp_bar = plot_fig.add_subplot(gs[30:,:])
            xp_bar.barh(0, xp_owned, color = "lime")
            xp_bar.tick_params(axis = "y", left = "off", right = "off", labelleft = "off")
            xp_bar.set_ylabel("Xp", rotation='horizontal', fontsize=18)
            xp_bar.yaxis.set_label_coords(1.04, -.3)
            xp_bar.set_xlim(0, xp_for_level)
            xp_bar.set_ylim(0, 0.8)

    def write(self, event=None, text = ""):
        if text:
            for line in text:
                self.output_text.set(self.output_text.get() + line)
        else:
            new_text = self.input_text.get()
            self.input_text.set("")
            self.output_text.set(self.output_text.get() + "\n" + new_text)
            self.game.text_parse(new_text)
            #print(self.input_text.get())
        
    def format_labels(self, pie_labels, pie_values):
        lab_and_val = zip(pie_labels, pie_values)
        lab_val_strings = []
        for pair in lab_and_val:
            new_pair = pair[0] + ": " + str(pair[1])
            lab_val_strings.append(new_pair)
        return lab_val_strings
    
    def add_char_stats(self, character):
        
#TODO: Once we get to animating the matplotlib objects, we should use that function to update the player name/race/class/status text fields.

    ########Character Stats Frame########
        char_stats_frame = Frame(self.char_stats_stack)
        ####Player Label####
        p_name = character.name
        p_race = character.char_race
        p_class = character.char_class
        p_status = character.status
        player_name_text = StringVar()
        player_name_text.set("%s\t%s\n%s %s " % (p_name, p_status, p_race, p_class)) 
        char_stats_name = Label(char_stats_frame, textvariable = player_name_text, width = 30, height = 2)
        char_stats_name.pack(side = "top")

        lower_frame = Frame(char_stats_frame)
        lower_frame.pack(side = "top")
        
        gs = gridspec.GridSpec(32,32, left = .075)
        plot_fig = Figure(figsize = (5.5, 4))
        char_stats_canvas = FigureCanvasTkAgg(plot_fig, lower_frame)
        char_stats_canvas.show()
        char_stats_canvas.get_tk_widget().pack(side = "left")
        ####Battle Strength####
        bs = "25"
        bs_label = Label(lower_frame, text = bs, font=("Arial", 60))
        bs_label.pack(side = "right")
        char_stats_canvas.get_tk_widget().create_window(355, 25, anchor = "nw", window = bs_label)
        ####LEVEL####
        p_level = character.level
        p_color = character.color
        level_bar = plot_fig.add_subplot(gs[:28,0:4])
        level_bar.set_title(level_bar.get_title(), text = "Level", fontsize = 16)
        level_bar.bar(0, p_level, width = .1, color = p_color)
        level_bar.yaxis.set_major_locator(MultipleLocator(1))
        level_bar.yaxis.grid()
        level_bar.set_ylim(1, 11)
        level_bar.set_xlim(0, 0.1)
        level_bar.tick_params(axis = "x", top = "off", bottom = "off", labelbottom = "off")
        ####ATTRIBUTES####
        p_strength = character.strength
        p_spirit = character.spirit
        p_intellect = character.intellect
        p_battle_strength = character.battle_strength_calc()
        pie_labels = ['Strength', 'Spirit', 'Intellect']
        pie_values = [p_strength, p_spirit, p_intellect]
        pie_colors = ['FireBrick', 'Khaki', 'SteelBlue']
        pie_chart = plot_fig.add_subplot(gs[0:28,0:])
        pie_chart.pie(pie_values, colors = pie_colors, startangle = 90)
        pie_chart.axis("equal")
        pie_legend = pie_chart.legend(title="Attributes", labels= self.format_labels(pie_labels, pie_values),
                         framealpha = 0, loc=(.78, .01), fontsize=11)
        pie_legend.set_title(title = "Attributes", prop = FontProperties(size = 14))
        ####Experience####
        xp_owned = character.xp
        xp_for_level = 350
        xp_bar = plot_fig.add_subplot(gs[30:,:])
        xp_bar.barh(0, xp_owned, color = "lime")
        xp_bar.tick_params(axis = "y", left = "off", right = "off", labelleft = "off")
        xp_bar.set_ylabel("Xp", rotation='horizontal', fontsize=18)
        xp_bar.yaxis.set_label_coords(1.04, -.3)
        xp_bar.set_xlim(0, xp_for_level)
        xp_bar.set_ylim(0, 0.8)
        
        char_stats_frame.grid(column=0, row=0, sticky = "NSEW")
        self.char_stats[character] = char_stats_frame

    def show_char_stats(self, char_name):
        for player in self.game.players:
            if player.name.lower() == char_name:
                self.char_stats[player].lift()
                break
            
    ########Background Image########
    def bg(self,win_height, win_width):
        self.bg_canvas = Canvas(self.root, height = win_height, width = win_width)
        self.bg_canvas.pack(expand = True, fill = "both")

        winh = int(round((win_height/968),1) * 10)
        winw = int(round((win_width/1536),1) * 10)
        wall = PhotoImage(file = "crypt_wall_tessl.gif")
        wall = wall.zoom(winw+1, winh+1)
        wall = wall.subsample(10, 10)
        self.bg_canvas.img = wall
        self.bg_canvas.create_image(0, 0, anchor = "nw", image = wall)

    ########Entry and Ouput Widgets########
    def create_widgets(self, scr_height, scr_width):
        win_height = (scr_height)
        win_width = (scr_width)

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

        self.char_stats_stack = Frame(self.root)
        self.char_stats = {}

        self.bg_canvas.create_window((7*win_width/10), (win_height/8), anchor = "nw", window = self.char_stats_stack)

    #TODO: implement parsing of the text from the Entry widget, and if it matches
    # the option show (player name)", raises that player's char_stats frame to
    # the top of the frame stack.
