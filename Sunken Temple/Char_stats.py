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
  
plt.pie(values, colors=colors, autopct= my_autopct, shadow=True, startangle=90)
plt.legend(title="Attributes", labels=labels, loc='lower right')

plt.axis('equal')
plt.show()
