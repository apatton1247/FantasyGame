from tkinter import *
#import Introduction as intro

root = Tk()

class Gui(Frame):
    def __init__(self, master):
        self.master = master
        Frame.__init__(self, master)
        self.create_widgets()
        self.master.title("Sunken Temple")

    def key(self, event):
        self.output_text.set(self.output_text.get() + "\n" + self.input_text.get())
        self.input_text.set("")

    def create_widgets(self):
        win_height = 900
        win_width = 1536
        bg_canvas = Canvas(self.master, height = win_height, width = win_width)
        bg_canvas.pack(expand = True, fill = "both")
        wall = PhotoImage(file = "gui_bg_1.gif")
        bg_canvas.img = wall
        bg_canvas.create_image(0, 0, anchor = "nw", image = wall)
        self.input_text = StringVar()
        self.input_text.set("")
        entry = Entry(self.master, width = 60, font=("Arial", 20), text = self.input_text)
        entry.bind("<Return>", self.key)
        self.output_text = StringVar()
        self.output_text.set("This is the sample text!\rHello World!")
        output_label = Label(self.master, bg = "white", anchor = "nw", width = 60, height = 18, font=("Arial", 20))
        output_label.config(textvariable = self.output_text, justify = "left")
        bg_canvas.create_window((win_width//4)+20, (win_height//8), anchor = "nw", window = output_label)
        bg_canvas.create_window((win_width//4)+20, (6.5*win_height//10), anchor = "nw", window = entry)

            

gui = Gui(root)
root.mainloop()
