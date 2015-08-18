import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib.ticker import MultipleLocator
from matplotlib.font_manager import FontProperties
import matplotlib.gridspec as gridspec
import matplotlib.style as style
from PIL import Image as PILImg
from PIL import ImageTk
from tkinter import *

#################### GUI ROOT FRAME ####################
class Gui(Tk):
    def __init__(self, game):
        Tk.__init__(self)
        self.game = game
        self.root = Frame(self)
        self.root.pack(side = "top", fill = "both", expand = True)
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (self.width, self.height))
        self.resizable(width=FALSE, height=FALSE)
        self.create_widgets()
        Tk.wm_title(self, "Sunken Temple")

######## BACKGROUND IMAGE ########
    def bg(self):
                ## CREATES BACKGROUND CANVAS ##
        self.bg_canvas = Canvas(self.root, height = self.height, width = self.width)
        self.bg_canvas.pack(expand = True, fill = "both")
                ## READS IN IMAGE FILE ##
        wall2 = PILImg.open("crypt_wall_tessl.gif")
                ## SIZE AND RESOLUTION ##
        winh = int(round((self.height/968),1) * 10)
        winw = int(round((self.width/1536),1) * 10)
        self.wall2 = wall2.resize((self.width, self.height), PILImg.ANTIALIAS)
        self.bg_canvas.img2 = ImageTk.PhotoImage(self.wall2)
                ## POSITION IN ROOT FRAME ##
        self.bg_canvas.create_image(0, 0, anchor = "nw", image = self.bg_canvas.img2)

######## CHARACTER STATS FRAME ########
    def add_char_stats_frame(self): 
        self.char_stats_frame = Frame(self.root, bg="light gray", bd=2, relief = "sunken")
    ###### TOP PLAYER LABEL ######
        upper_frame = Frame(self.char_stats_frame, bg="light gray")
        upper_frame.pack(side = "top")
                ## VARIABLES ##
        self.p_name = StringVar()
        self.p_race_class = StringVar()
        self.p_status = StringVar()
                ## CREATES LEFT BLANK LABEL ##
        blank_label = Label(upper_frame, width = 9, height = 3, bg="light gray", font = ("Arial", (self.width//100)))
        blank_label.pack(side = "left")
                ## CREATES RIGHT STATUS LABEL ##
        status_label = Label(upper_frame, textvariable = self.p_status, width = 9,
                             height = 2, bg="light gray", font = ("Arial italic", (round((self.width/self.height)*12))), anchor = "w", justify = "left")
        status_label.pack(side = "right")
                ## CREATES CENTER NAME, CLASS, RACE LABELS ##
        name_label = Label(upper_frame, textvariable = self.p_name, width = 10,
                           height = 1, bg="light gray", font = ("Arial bold", (round((self.width/self.height)*13))))
        name_label.pack(side = "top")
        race_class_label = Label(upper_frame, textvariable = self.p_race_class,
                                 width = 16, height = 1, bg="light gray", font = ("Arial", (round((self.width/self.height)*10))))
        race_class_label.pack(side = "top")
    ###### MIDDLE PLAYER GRAPHS ######
        middle_frame = Frame(self.char_stats_frame)
        middle_frame.pack(side = "top")
                ## CREATES GRID ##
        gs = gridspec.GridSpec(32,32, left = .075)
        gs.update(wspace=.95)
                ## FIGURE SIZE ##
        self.plot_fig = Figure(figsize = (self.width/300, self.height/255))
                ## TURNS FIGURE INTO CANVAS ##
        char_stats_canvas = FigureCanvasTkAgg(self.plot_fig, middle_frame)
        char_stats_canvas.show()
        char_stats_canvas.get_tk_widget().configure(background='light gray', highlightcolor='light gray', highlightbackground='light gray')
        char_stats_canvas.get_tk_widget().pack(side = "left")
        #### BATTLE STRENGTH ####
                ## VARIABLES ##
        self.p_bs = StringVar()
                ## CREATES LABEL ##
        bs_label = Label(middle_frame, textvariable = self.p_bs, font=("Arial", (round((self.width/self.height)*36.25))))
        bs_label.pack(side = "right")
                ## POSITION ##
        char_stats_canvas.get_tk_widget().create_window((45*self.width/200), (3*self.height/100), anchor = "n", window = bs_label)
        #### LEVEL ####
                ## VARIABLES ##
        self.p_level = IntVar()
        self.p_color = StringVar()
                ## POSITION ##
        self.level_bar = self.plot_fig.add_subplot(gs[:28,1:5])
        #### ATTRIBUTES ####
                ## VARIABLES ##
        self.p_strength = IntVar()
        self.p_spirit = IntVar()
        self.p_intellect = IntVar()
                ## POSITION ##
        self.pie_chart = self.plot_fig.add_subplot(gs[0:28,0:-3])
                ## SHAPE ##
        self.pie_chart.axis("equal")
        #### EXPERIENCE ####
                ## VARIABLES ##
        self.p_xp = IntVar()
        self.p_xp_for_level = IntVar()
                ## POSITION ##
        self.xp_bar = self.plot_fig.add_subplot(gs[30:,:])
    ###### LOWER DIMENSION LABEL ######                                               
        lower_frame = Frame(self.char_stats_frame, bg="light gray")
        lower_frame.pack(side = "top")
                ## VARIABLES ##
        self.p_dimension = StringVar()
                ## CREATES LABEL ##
        dimension_label = Label(lower_frame, textvariable = self.p_dimension, width = 27,
                                height = 1, bg="light gray", font = ("Arial", (round((self.width/self.height)*13))))
        dimension_label.pack(side = "top")

        self.char_stats_frame.pack()
    ###### HIDES CHAR STATS WHEN 0 PLAYERS ######
        if not self.game.players:
            self.char_stats_frame.lower()

######## FORMAT ATTRIBUTE LABELS METHOD ########        
    def format_labels(self, pie_labels, pie_values):
        lab_and_val = zip(pie_labels, pie_values)
        lab_val_strings = []
        for pair in lab_and_val:
            new_pair = pair[0] + ": " + str(pair[1])
            lab_val_strings.append(new_pair)
        return lab_val_strings
        
######## ANIMATE METHOD #########
    def animate(self, interval):
        if self.game.players:
            self.char_stats_frame.lift()
        else:
            self.char_stats_frame.lower()
        #### CHARACTER VARIABLES ####
        self.p_name.set(self.char_shown.name)
        self.p_race_class.set(str(self.char_shown.char_race) + " " + str(self.char_shown.char_class))
        self.p_status.set(self.char_shown.status)
        self.p_bs.set(str(self.char_shown.battle_strength_calc()))
        self.p_level.set(self.char_shown.level)
        self.p_color.set(self.char_shown.color)
        self.p_strength.set(self.char_shown.strength)
        self.p_spirit.set(self.char_shown.spirit)
        self.p_intellect.set(self.char_shown.intellect)
        self.p_xp.set(self.char_shown.xp)
        self.p_xp_for_level.set(self.char_shown.xp_for_level)
        self.p_dimension.set(self.char_shown.dimension)
        #### CLEARS ALL CHARTS ####
        self.level_bar.clear()
        self.pie_chart.clear()
        self.xp_bar.clear()
        #### UPDATES LEVEL ####
        self.level_bar.bar(0, self.p_level.get(), width = .1, color = self.p_color.get())
        self.level_bar.set_title(self.level_bar.get_title(), text = "Level", fontsize = (self.width//91))
        self.level_bar.yaxis.set_major_locator(MultipleLocator(1))
        self.level_bar.yaxis.grid()
        self.level_bar.set_ylim(0, 11)
        self.level_bar.set_xlim(0, 0.1)
        self.level_bar.tick_params(axis = "x", top = "off", bottom = "off", labelbottom = "off")
        #### UPDATES ATTRIBUTES ####
        pie_labels = ['Strength', 'Spirit', 'Intellect']
        pie_values = [self.p_strength.get(), self.p_spirit.get(), self.p_intellect.get()]
        pie_colors = ['FireBrick', 'Khaki', 'SteelBlue']
        self.pie_chart.pie(pie_values, colors = pie_colors, startangle = 90)
        pie_legend = self.pie_chart.legend(title="Attributes", labels= self.format_labels(pie_labels, pie_values),
                                           framealpha = 0, loc=(.76, .01), fontsize=(self.width//116))
        pie_legend.set_title(title = "Attributes", prop = FontProperties(size = (self.width//91)))
        #### UPDATES EXPERIENCE ####
        self.xp_bar.barh(0, self.p_xp.get(), color = "lime")
        self.xp_bar.tick_params(axis = "y", left = "off", right = "off", labelleft = "off")
        self.xp_bar.set_ylabel("Xp", rotation='horizontal', fontsize=(self.width//80))
        self.xp_bar.yaxis.set_label_coords(1.04, -.3)
        self.xp_bar.set_xlim(0, self.p_xp_for_level.get())
        self.xp_bar.set_ylim(0, 0.8)

######## ADD OPTIONS FRAME ########
    def add_options_frame(self):
        self.options_frame = Frame(self.root)
                ## VARIABLES ##
        self.options_text = StringVar()
                ## CREATES LABEL ##
        self.options_label = Label(self.options_frame, bg = "light gray", width = 32, height = 8, anchor = "nw",
                                   justify = "left", font=("Arial", 20), textvariable = self.options_text, relief = "sunken")
        self.options_label.pack()
        self.options_frame.pack()
            
######### CREATE GUI WIDGETS METHOD #######
    def create_widgets(self):
                ## VARIABLES ##
        self.bg()
        self.input_text = StringVar()
        self.input_text.set("")
        #### CREATES ENTRY WIDGET ####
        entry = Entry(self.root, bg = "light gray", width = 65, font=("Arial", 20), textvariable = self.input_text, relief = "sunken")
        entry.bind("<Return>", self.write)
                ## POSITION ##
        self.bg_canvas.create_window((5*self.width/100), (80*self.height/100), anchor = "nw", window = entry)
        #### CREATES OUTPUT WIDGET ####
        self.output_text = Text(self.root, bg = "light gray", width = 65, height = 20, font=("Arial", 20), relief = "sunken", state = "normal", wrap = "word")
        self.output_text.insert("end", "After adding a player, use the new 'set action (player name)' command to set which character will be implicitly acting in all commands following this one, until another 'set action (player name)' command is sent.  Once an actor is set, you may (and should) omit their name from future commands.  To change players's attributes, type an option (e.g. 'level up', 'show hidden options') and then the proper arguments to go with the option.  For example:\n'set action Dave'\n'level up 1'\n'intellect up -4'\n")
        self.output_text.config(state = "disabled")
                ## POSITION ##
        self.bg_canvas.create_window((5*self.width/100), (10*self.height/100), anchor = "nw", window = self.output_text)
        #### CHAR STATS WIDGET POSITION ####
        self.add_char_stats_frame()
        self.bg_canvas.create_window((67*self.width/100), (10*self.height/100), anchor = "nw", window = self.char_stats_frame)
        #### OPTIONS WIDGET POSITION ####
        self.add_options_frame()
        self.bg_canvas.create_window((67*self.width/100), (60*self.height/100), anchor = "nw", window = self.options_frame)

######## SHOW CHARACTER STATS METHOD ########
    def show_char_stats(self, char_name):
        for player in self.game.players:
            if player.name.lower() == char_name:
                self.char_shown = player
                break
        #Temporarily supports both passing a lower-case name (which will be compared
        # against all players' names) or a player object, which will exhaust the for-
        # loop above and get to this else-block.
        else:
            self.char_shown = char_name

######## WRITE METHOD ########
    def write(self, event=None, text = ""):
        self.output_text.config(state = "normal")
        if text:
            self.output_text.insert("end", text+"\n")
        else:
            self.options_text.set("")
            new_text = self.input_text.get()
            self.game.interpret(new_text)
            self.input_text.set("")
            self.output_text.insert("end", new_text+"\n")
        self.output_text.config(state = "disabled")
        self.output_text.see("end")

######## CLEAR OUTPUT METHOD ########
    def clear_output(self):
        self.output_text.config(state = "normal")
        self.output_text.delete("1.0", "end")
        self.output_text.config(state = "disabled")

if __name__ == "__main__":
    print("Run gameplay.py instead.")
