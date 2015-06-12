from pylab import *

char_xp = 250
level_xp = 300 #for example max 300xp for level 6

pos = arange(1)

fig = barh(pos, (char_xp), align = "center", color= "green")
plt.ylabel('Xp', rotation=90)

plt.tick_params(axis='y',which='both',left='off',right='off',labelleft='off')

plt.xlim(0,level_xp)
subplots_adjust(top=.15)

show()
