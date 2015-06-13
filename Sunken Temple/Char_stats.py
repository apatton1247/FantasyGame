import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk

num_strength = 15
num_spirit = 2
num_intellect = 5
char_battle_strength = 25
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
fig = plt.Figure(figsize = (8, 8), dpi = 100)
piechart = fig.add_subplot(111)
piechart.pie(pie_values, colors = pie_colors, startangle = 90)
legend = piechart.legend(title="Attributes", labels= format_labels(pie_labels, pie_values)
                         ,framealpha = 0, loc=(.82, .01), fontsize=16)
plt.setp(legend.get_title(),fontsize=20)
piechart.text(1.14, .5, str(char_battle_strength), bbox=dict(facecolor='none', pad=20), fontsize=80)
canvas = FigureCanvasTkAgg(fig, frame)
canvas.show()
canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)
#canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

piechart.axis('equal')
