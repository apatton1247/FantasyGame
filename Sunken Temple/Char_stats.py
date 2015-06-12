import matplotlib.pyplot as plt

num_strength = 15
num_spirit = 2
num_intellect = 5

pie_labels = ['Strength', 'Spirit', 'Intellect']
pie_values = [num_strength, num_spirit, num_intellect]
pie_colors = ['FireBrick', 'Khaki', 'SteelBlue']

<<<<<<< HEAD

def format_labels(pie_labels, pie_values):
    lab_and_val = zip(pie_labels, pie_values)
=======
def format_labels(labels, values):
    lab_and_val = zip(labels, values)
>>>>>>> FETCH_HEAD
    lab_val_strings = []
    for pair in lab_and_val:
        new_pair = pair[0] + ": " + str(pair[1])
        lab_val_strings.append(new_pair)
    return lab_val_strings
  
<<<<<<< HEAD
plt.pie(pie_values, colors=pie_colors, shadow=True, startangle=90)
plt.legend(title="Attributes", labels=format_labels(pie_labels, pie_values), framealpha = 0, loc=(.8, -.1))
=======
stat_chart = plt.pie(values, colors=colors, shadow=True, startangle=90)
stat_legend = plt.legend(title="Attributes", labels= format_labels(labels, values), framealpha = 0, loc=(.8, -.1))
        #This loc form can also be used, looks about the same on my screen:
        #loc = "lower right", bbox_to_anchor = (1.1, -0.1))
>>>>>>> FETCH_HEAD

plt.axis('equal')
plt.show()

print(stat_chart)
