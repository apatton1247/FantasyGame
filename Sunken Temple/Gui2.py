from tkinter import *

class Gui(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.root = Frame(self)
        self.root.pack(side = "top", fill = "both", expand = True)
        self.create_widgets()
        Tk.wm_title(self, "Sunken Temple")

        self.mainloop()

    def create_widgets(self):
        win_height = 900
        win_width = 1536
        bg_canvas = Canvas(self.root, height = win_height, width = win_width)
        bg_canvas.pack(expand = True, fill = "both")
        wall = PhotoImage(file = "gui_bg_1.gif")
        bg_canvas.img = wall
        bg_canvas.create_image(0, 0, anchor = "nw", image = wall)
        entry = Entry(self.root, width = 60, font=("Arial", 20))
        output_label = Label(self.root, bg = "white", anchor = "nw", width = 60, height = 18, font=("Arial", 20))
        output_label.config(text = "This is the sample text!\nHello World!")
        bg_canvas.create_window((win_width//7)+40, (win_height//8), anchor = "nw", window = output_label)
        bg_canvas.create_window((win_width//7)+70, (6*win_height//7), anchor = "nw", window = entry)

gui = Gui()
