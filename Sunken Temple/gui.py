import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib.ticker import MultipleLocator
from matplotlib.font_manager import FontProperties
import matplotlib.gridspec as gridspec
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
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (self.width, self.height))
        self.resizable(width=FALSE, height=FALSE)
        
        self.create_widgets()
        Tk.wm_title(self, "Sunken Temple")

    def animate(self, interval):

        ####Char Stats Update####
        self.p_name.set(self.char_shown.name)
        self.p_race_class.set(self.char_shown.char_race + " " + self.char_shown.char_class)
        self.p_status.set(self.char_shown.status)
        self.p_bs.set(str(self.char_shown.battle_strength_calc()))
        self.p_level.set(self.char_shown.level)
        self.p_color.set(self.char_shown.color)
        self.p_strength.set(self.char_shown.strength)
        self.p_spirit.set(self.char_shown.spirit)
        self.p_intellect.set(self.char_shown.intellect)
        self.p_xp.set(self.char_shown.xp)
        self.p_xp_for_level.set(self.char_shown.xp_for_level)

        ####Charts Clear####
        self.level_bar.clear()
        self.pie_chart.clear()
        self.xp_bar.clear()

        ####Level Bar Chart Update####
        self.level_bar.bar(0, self.p_level.get(), width = .1, color = self.p_color.get())
        self.level_bar.set_title(self.level_bar.get_title(), text = "Level", fontsize = (self.width//91))
        self.level_bar.yaxis.set_major_locator(MultipleLocator(1))
        self.level_bar.yaxis.grid()
        self.level_bar.set_ylim(1, 11)
        self.level_bar.set_xlim(0, 0.1)
        self.level_bar.tick_params(axis = "x", top = "off", bottom = "off", labelbottom = "off")

        ####Attribute Pie Chart Update####
        pie_labels = ['Strength', 'Spirit', 'Intellect']
        pie_values = [self.p_strength.get(), self.p_spirit.get(), self.p_intellect.get()]
        pie_colors = ['FireBrick', 'Khaki', 'SteelBlue']
        self.pie_chart.pie(pie_values, colors = pie_colors, startangle = 90)
        pie_legend = self.pie_chart.legend(title="Attributes", labels= self.format_labels(pie_labels, pie_values),
                                           framealpha = 0, loc=(.73, .01), fontsize=11)
        pie_legend.set_title(title = "Attributes", prop = FontProperties(size = (self.width//91)))
########       self.subplots_adjust(left=.10)
        
        ####XP Bar Chart Update####
        self.xp_bar.barh(0, self.p_xp.get(), color = "lime")
        self.xp_bar.tick_params(axis = "y", left = "off", right = "off", labelleft = "off")
        self.xp_bar.set_ylabel("Xp", rotation='horizontal', fontsize=(self.width//80))
        self.xp_bar.yaxis.set_label_coords(1.04, -.3)
        self.xp_bar.set_xlim(0, self.p_xp_for_level.get())
        self.xp_bar.set_ylim(0, 0.8)

    def write(self, event=None, text = ""):
        if text:
            self.output_text.set(self.output_text.get() + "\n" + line)
        else:
            new_text = self.input_text.get()
            self.input_text.set("")
            self.output_text.set(self.output_text.get() + "\n" + new_text)
            self.options_text.set("")
            self.game.text_parse(new_text)
            #TODO: once the options widget exists, should also clear its contents.
        
    def format_labels(self, pie_labels, pie_values):
        lab_and_val = zip(pie_labels, pie_values)
        lab_val_strings = []
        for pair in lab_and_val:
            new_pair = pair[0] + ": " + str(pair[1])
            lab_val_strings.append(new_pair)
        return lab_val_strings
    
    def add_char_stats_frame(self):
        
    ########Character Stats Frame########
        self.char_stats_frame = Frame(self.root)
        upper_frame = Frame(self.char_stats_frame)
        upper_frame.pack(side = "top")

        ####Player Label####
        self.p_name = StringVar()
        self.p_race_class = StringVar()
        self.p_status = StringVar()

        race_class_label = Label(upper_frame, textvariable = self.p_race_class,
                                width = 30, height = 1, font = ("Arial", (self.width//80)))
        race_class_label.pack(side = "bottom")
        name_label = Label(upper_frame, textvariable = self.p_name, width = 15,
                                height = 1, font = ("Arial bold", (self.width//64)), anchor = "e")
        name_label.pack(side = "left")
        status_label = Label(upper_frame, textvariable = self.p_status, width = 15,
                                  height = 1, font = ("Arial italic", (self.width//80)), anchor = "w")
        status_label.pack(side = "left")
        
        lower_frame = Frame(self.char_stats_frame)
        lower_frame.pack(side = "top")
        
        gs = gridspec.GridSpec(32,32, left = .075)
        self.plot_fig = Figure(figsize = (self.width/275, self.height/255))
        char_stats_canvas = FigureCanvasTkAgg(self.plot_fig, lower_frame)
        char_stats_canvas.show()
        char_stats_canvas.get_tk_widget().pack(side = "left")
        
        ####Battle Strength####
        self.p_bs = StringVar()
        bs_label = Label(lower_frame, textvariable = self.p_bs, font=("Arial", (self.width//22)))
        bs_label.pack(side = "right")
        char_stats_canvas.get_tk_widget().create_window((25*self.width/100), (3*self.height/100), anchor = "n", window = bs_label)

        ####LEVEL####
        self.p_level = IntVar()
        self.p_color = StringVar()
        
        self.level_bar = self.plot_fig.add_subplot(gs[:28,0:4])
        
        ####ATTRIBUTES####
        self.p_strength = IntVar()
        self.p_spirit = IntVar()
        self.p_intellect = IntVar()
        self.pie_chart = self.plot_fig.add_subplot(gs[0:28,0:])
        self.pie_chart.axis("equal")

        ####Experience####
        self.p_xp = IntVar()
        self.p_xp_for_level = IntVar()
        self.xp_bar = self.plot_fig.add_subplot(gs[30:,:])
        
        self.char_stats_frame.pack()

    def show_char_stats(self, char_name):
        for player in self.game.players:
            if player.name.lower() == char_name:
                self.char_shown = player
                break

    def add_options_frame(self):
        self.options_frame = Frame(self.root)
        self.options_text = StringVar()
        self.options_label = Label(self.options_frame, bg = "light gray", width = 35, height = 8, anchor = "nw",
                                   justify = "left", font=("Arial", 20), textvariable = self.options_text, relief = "sunken")
        self.options_label.pack()
        self.options_frame.pack()
        
    
    ########Background Image########
    def bg(self):
        self.bg_canvas = Canvas(self.root, height = self.height, width = self.width)
        self.bg_canvas.pack(expand = True, fill = "both")

        wall = PhotoImage(file = "crypt_wall_tessl.gif")

        winh = int(round((self.height/968),1) * 10)
        winw = int(round((self.width/1536),1) * 10)
        wall = wall.zoom(winw+1, winh+1)
        wall = wall.subsample(10, 10)
        
        self.bg_canvas.img = wall
        self.bg_canvas.create_image(0, 0, anchor = "nw", image = wall)

    ########Entry and Ouput Widgets########
    def create_widgets(self):
        
        self.bg()
        
        self.input_text = StringVar()
        self.input_text.set("")
        entry = Entry(self.root, bg = "light gray", width = 65, font=("Arial", 20), textvariable = self.input_text, relief = "sunken")
        entry.bind("<Return>", self.write)

        self.output_text = StringVar()
        self.output_text.set("This is the sample text!\rHello World!\rTo change players's attributes, type an option (e.g. 'level up', 'show hidden options')\r and then the proper arguments to go with the option.  For example:\r'show Dave'\r'level up 1 Dave'\r'attr up intellect -4 Dave'")
        output_label = Label(self.root, bg = "light gray", anchor = "nw", width = 65, height = 20, font=("Arial", 20), relief = "sunken")
        output_label.config(textvariable = self.output_text, justify = "left")

        self.bg_canvas.create_window((5*self.width/100), (10*self.height/100), anchor = "nw", window = output_label)
        self.bg_canvas.create_window((5*self.width/100), (80*self.height/100), anchor = "nw", window = entry)

        self.add_char_stats_frame()
        self.bg_canvas.create_window((66*self.width/100), (10*self.height/100), anchor = "nw", window = self.char_stats_frame)

        self.add_options_frame()
        self.bg_canvas.create_window((66*self.width/100), (55*self.height/100), anchor = "nw", window = self.options_frame)

if __name__ == "__main__":
    print("Run gameplay.py instead.")
