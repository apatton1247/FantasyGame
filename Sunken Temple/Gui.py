#imports matplotlib
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from tkinter import *
#import Gameplay as game

class Gui(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.root = Frame(self)
        self.root.pack(side = "top", fill = "both", expand = True)
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
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

    def create_widgets(self, scr_height, scr_width):
        win_height = int(0.75 * scr_height)
        win_width = int(0.75 * scr_width)
        bg_canvas = Canvas(self.root, height = win_height, width = win_width)
        bg_canvas.pack(expand = True, fill = "both")

        wall = PhotoImage(file = "gui_bg_1.gif")
        bg_canvas.img = wall
        bg_canvas.create_image(0, 0, anchor = "nw", image = wall)

        self.input_text = StringVar()
        self.input_text.set("")
        entry = Entry(self.root, bg = "light gray", width = 60, font=("Arial", 16), textvariable = self.input_text, relief = "sunken")
        entry.bind("<Return>", self.write)

        self.output_text = StringVar()
        self.output_text.set("This is the sample text!\rHello World!")
        output_label = Label(self.root, bg = "light gray", anchor = "nw", width = 60, height = 18, font=("Arial", 16), relief = "sunken")
        output_label.config(textvariable = self.output_text, justify = "left")

        player_stats_label = Label(self.root, bg = "light gray", anchor ="nw", width = 20, height = 6, font=("Arial",16))

        bg_canvas.create_window((win_width//4)+20, (win_height//8), anchor = "nw", window = output_label)
        bg_canvas.create_window((win_width//4)+20, (7*win_height//10), anchor = "nw", window = entry)


gui = Gui()
