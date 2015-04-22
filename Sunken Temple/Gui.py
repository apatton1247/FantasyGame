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
    top_label = Label(io_frame, height = 10, width = 80, bg = "dark gray", borderwidth = 0)
    output = Label(io_frame, bg = "white", anchor = "nw")
    output.config(height = 20, width = 80, wraplength = 575, text = "Welcome to the Sunken Temple!\nThis is a line of text that is so long that the Label will be either forced to wrap it or it will disappear off the side of the screen into the void!", justify = "left")
    #print(output.config().keys())
    #center_image = PhotoImage(file = "StoneWallCenterLow")
    center_label = Label(io_frame, height = 7, width = 80, bg = "dark gray", borderwidth = 0)
    entry = Entry(io_frame, width = 94)

    left_pad_frame = Frame(left_frame)
    left_image = PhotoImage(file="StoneWallLeft.gif")
    left_pic_label = Label(left_pad_frame, image = left_image, height = 590, width = 201, borderwidth = 0)
    left_pic_label.pack(side = "left", fill = "both", expand = "yes")
    left_pic_label.image = left_image

    right_pad_frame = Frame(left_frame)
    right_image = PhotoImage(file="StoneWallRight.gif")
    right_pic_label = Label(right_pad_frame, image = right_image, height = 590, width = 201, borderwidth = 0)
    right_pic_label.pack(side = "right")
    right_pic_label.image = right_image
    
    button_frame = Frame(left_frame)
    ext_button = Button(button_frame, text = ">")
    button_frame.config(bg = "dark green", height = 22)

    left_pad_frame.pack(side = "left")
    top_label.pack(side = "top")
    output.pack(side = "top")
    center_label.pack(side = "top")
    entry.pack(side = "bottom")
    ext_button.pack(side = "top")
    io_frame.pack(side = "left")
    right_pad_frame.pack(side = "left")
    button_frame.pack(side = "top")
    left_frame.pack()
    
    
gui = Gui(root)
root.mainloop()
