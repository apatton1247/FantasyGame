from tkinter import *

root = Tk()

class Gui(Frame):
    def __init__(self, master):
        self.master = master
        Frame.__init__(self, master)
        self.create_widgets()
        self.master.title("Sunken Temple")

    def create_widgets(self):
        win_height = 900
        win_width = 1536
        bg_canvas = Canvas(self.master, height = win_height, width = win_width)
        bg_canvas.pack(expand = True, fill = "both")
        wall = PhotoImage(file = "gui_bg_1.gif")
        bg_canvas.img = wall
        bg_canvas.create_image(0, 0, anchor = "nw", image = wall)
        entry = Entry(self.master, width = 60, font=("Arial", 20))
        output_label = Label(self.master, bg = "white", anchor = "nw", width = 60, height = 18, font=("Arial", 20))
        output_label.config(text = "This is the sample text!\nHello World!")
        bg_canvas.create_window((win_width//7)+40, (win_height//8), anchor = "nw", window = output_label)
        bg_canvas.create_window((win_width//7)+70, (6*win_height//7), anchor = "nw", window = entry)
        

gui = Gui(root)
root.mainloop()
