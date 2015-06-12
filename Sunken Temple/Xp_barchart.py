import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#variables
char_xp = 250
level_xp = 300

y_pos = np.arange(1)
#This says there is only one bar
fig = plt.figure()
#Something to do with turning the plot into a figure?
ax = fig.add_subplot(111)
#Defining ax and positioning the subplot??
ax.barh(y_pos, char_xp, color='lime')
#Basic construction of the bar chart

plt.tick_params(axis='y', which='both', left='off', right='off',labelleft='off')
#Removes the left and right ticks and default tick labels
plt.ylabel("Xp", rotation='horizontal', fontsize=18, verticalalignment='center')
#Defines the y axis label and rotates
ax.yaxis.set_label_coords(1.04,.65)
#Moves y label to the correct position
plt.xlim(0,level_xp)
#Sets limits on the x axis
plt.ylim(0,.1)
#set limits on the y axis
plt.subplots_adjust(top=.15)
#Decreases width of entire chart


plt.show()
