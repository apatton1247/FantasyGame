from tkinter import *

root = Tk()

class Gui(Frame):
    def __init__(self, master):
        self.master = master
        Frame.__init__(self, master)
        self.create_widgets()
        self.master.title("Sunken Temple")

    def create_widgets(self):
        bg_canvas = Canvas(self.master, height = 590, width = 1180)
        bg_canvas.pack(expand = True, fill = "both")
        wall = PhotoImage(file = "StoneWall.gif")
        bg_canvas.img = wall
        bg_canvas.create_image(0, 0, anchor = "nw", image = wall)
        entry = Entry(self.master, width = 80)
        output_label = Label(self.master, bg = "white", anchor = "nw", width = 80, height = 20)
        bg_canvas.create_window(300, 100, anchor = "nw", window = output_label)
        bg_canvas.create_window(340, 500, anchor = "nw", window = entry)
        

gui = Gui(root)
root.mainloop()
