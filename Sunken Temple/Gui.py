from tkinter import *

root = Tk()

class Gui(Frame):
  def __init__(self, master):
    self.master = master
    Frame.__init__(self, master)
    self.create_widgets()
    self.master.title("Sunken Temple")

  def create_widgets(self):
    left_frame = Frame(self.master, bg = "dark green")

    io_frame = Frame(left_frame, bg = "dark green")
    output = Label(io_frame, bg = "white", anchor = "nw")
    output.config(height = 20, width = 80, wraplength = 575, text = "Welcome to the Sunken Temple!\n This is a line of text that is so long that the Label will be either forced to wrap it or it will disappear off the side of the screen into the void!", justify = "left")
    print(output.config().keys())
    entry = Entry(io_frame, width = 79)
    left_pad_frame = Frame(left_frame, width = 20, bg = "dark green")

    button_frame = Frame(left_frame)
    ext_button = Button(button_frame, text = ">")
    button_frame.config(bg = "dark green", height = 22)

    left_pad_frame.pack(side = "left")
    output.pack(side = "top", pady = 10)
    entry.pack(side = "bottom")
    ext_button.pack(side = "top", padx = 10, pady = 10)
    io_frame.pack(side = "left")
    button_frame.pack(side = "top")
    left_frame.pack()
    
    
gui = Gui(root)
root.mainloop()
