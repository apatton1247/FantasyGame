import matplotlib.pyplot as plt

num_strength = 15
num_spirit = 2
num_intellect = 5

labels = ['Strength', 'Spirit', 'Intellect']
values = [num_strength, num_spirit, num_intellect]
colors = ['FireBrick', 'Khaki', 'SteelBlue']


def my_autopct(pct):
    total=sum(values)
    val=int(pct*total/100.0)
    return '{v:d}'.format(v=val)

def format_labels(labels, values):
    lab_and_val = zip(labels, values)
    lab_val_strings = []
    for pair in lab_and_val:
        new_pair = pair[0] + ": " + str(pair[1])
        lab_val_strings.append(new_pair)
    return lab_val_strings
  
plt.pie(values, colors=colors, shadow=True,
        #When autopct is specified, internal labels show at a radius of
        #pctdistance away from the center of the graph.  Uncomment them to see!
        #autopct= my_autopct, pctdistance = 1.2,
        startangle=90)
plt.legend(title="Attributes", labels= format_labels(labels, values),
        #framealpha sets the transparency of the legend
        framealpha = 0, loc=(.8, -.1))
        #This loc form can also be used, looks about the same on my screen:
        #loc = "lower right", bbox_to_anchor = (1.1, -0.1))

plt.axis('equal')
plt.show()
