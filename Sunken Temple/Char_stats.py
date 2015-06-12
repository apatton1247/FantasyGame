import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk

num_strength = 15
num_spirit = 2
num_intellect = 5

pie_labels = ['Strength', 'Spirit', 'Intellect']
pie_values = [num_strength, num_spirit, num_intellect]
pie_colors = ['FireBrick', 'Khaki', 'SteelBlue']

def format_labels(pie_labels, pie_values):
    lab_and_val = zip(pie_labels, pie_values)
    lab_val_strings = []
    for pair in lab_and_val:
        new_pair = pair[0] + ": " + str(pair[1])
        lab_val_strings.append(new_pair)
    return lab_val_strings

#stat_chart = plt.pie(values, colors=colors, shadow=True, startangle=90)
#stat_legend = plt.legend(title="Attributes", labels= format_labels(labels, values), framealpha = 0, loc=(.8, -.1))
        #This loc form can also be used, looks about the same on my screen:
        #loc = "lower right", bbox_to_anchor = (1.1, -0.1))
#plt.show()

root = tk.Tk()
frame = tk.Frame(master = root)
frame.pack(fill = "both", expand = True)
test_label = tk.Label(frame, width = 150, height = 2, text = "Hello!")
test_label.pack(side = "top")
f = plt.Figure(figsize = (8, 8), dpi = 100)
piechart = f.add_subplot(111)
piechart.pie(values, colors = colors, shadow = True, startangle = 90)
piechart.legend(title="Attributes", labels= format_labels(labels, values), framealpha = 0, loc=(.8, -.1))
canvas = FigureCanvasTkAgg(f, frame)
canvas.show()
canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

piechart.axis('equal')
