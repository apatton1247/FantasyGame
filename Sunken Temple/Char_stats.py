import matplotlib.pyplot as plt

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
  
plt.pie(pie_values, colors=pie_colors, shadow=True, startangle=90)
plt.legend(title="Attributes", labels=format_labels(pie_labels, pie_values), framealpha = 0, loc=(.8, -.1))

plt.axis('equal')
plt.show()
