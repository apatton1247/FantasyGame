import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

#Variables
char_level = 6
char_color = "darkviolet"

#Basic changes
fig = plt.figure()
ax = fig.add_subplot(111)
plt.title("Level", fontsize=20)
ax.bar(0, char_level, color=char_color)

#Ticker changes
plt.setp(ax.get_yticklabels(), fontsize=16)
plt.tick_params(axis='x', which='both', top='off', bottom='off'
                ,labelright='off', labelbottom='off')
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.grid()

#Size changes
plt.ylim(0,11)
plt.xlim(0,.8)
plt.subplots_adjust(right=.25)

plt.show()
