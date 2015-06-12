import matplotlib.pyplot as plt

#variables
char_xp = 250
level_xp = 300

fig = plt.figure()
ax = fig.add_subplot(111)
ax.barh(0, char_xp, color='lime', hatch = "*")

plt.tick_params(axis='y', left='off', right='off', labelleft='off')
plt.ylabel("Xp", rotation='horizontal', fontsize=18)
ax.yaxis.set_label_coords(1.04,.25)
plt.xlim(0,level_xp)
plt.ylim(0,.8)
plt.subplots_adjust(top=.15)

plt.show()
