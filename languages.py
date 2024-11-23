'''
from array import array
import numpy as numpy
import matplotlib.pyplot as plot
from matplotlib import style
style.use('fivethirtyeight')
x1=[40,55,60,60,70,50,50,70,70,65,90,50,75,50,90,50,40,40]                                                    #   Asm, C, C++, C#, CSS, DART, GO, HTML, JAVA, JS, LATEX, PHP, PYTHON, R, MATLAB, MYSQL, VERILOG, XML
n1 = numpy.linspace(1,18,18)
n2=[["a"],"a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a",]







fig1=plot.figure(figsize=(10,10))


plot.stem(n2,x1)
plot.xlim(0,19)



plot.show()















data = [[ 66386, 174296,  75131, 577908,  32015],
        [ 58230, 381139,  78045,  99308, 160454],
        [ 89135,  80552, 152558, 497981, 603535],
        [ 78415,  81858, 150656, 193263,  69638],
        [139361, 331509, 343164, 781380,  52269]]

columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')
rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]

values = np.arange(0, 2500, 500)
value_increment = 1000

# Get some pastel shades for the colors
colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

# Initialize the vertical-offset for the stacked bar chart.
y_offset = np.zeros(len(columns))

# Plot bars and create text labels for the table
cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
# Reverse colors and text labels to display the last value at the top.
colors = colors[::-1]
cell_text.reverse()

# Add a table at the bottom of the axes
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')

# Adjust layout to make room for the table:
plt.subplots_adjust(left=0.2, bottom=0.2)

plt.ylabel("Loss in ${0}'s".format(value_increment))
plt.yticks(values * value_increment, ['%d' % val for val in values])
plt.xticks([])
plt.title('Loss by Disaster')

plt.show()




import numpy as np
import matplotlib.pyplot as plt


data = [[40,55,60,60,70,50,50,70]]


columns = ['ASM', 'C', 'C++', 'C#', 'CSS', 'DART', 'GO', 'HTML']


values = np.arange(0, 120, 20)
value_increment = 1

# Get some pastel shades for the colors
colors = plt.cm.BuPu(np.linspace(0, .7, 2))
n_rows = len(data)


index = np.arange(len(columns)) + 0.3
bar_width = 0.5
print(index)
# Initialize the vertical-offset for the stacked bar chart.
y_offset = np.zeros(len(columns))

# Plot bars and create text labels for the table
cell_text = []
for row in range(n_rows):
    plt.bar(index, data[0], bar_width, bottom=y_offset, color=colors[0])
    y_offset = y_offset + data[row]

    cell_text.append(["%1.0f%%" % (x) for x in y_offset])
# Reverse colors and text labels to display the last value at the top.
colors = colors[::-1]




plt.yticks(values * value_increment, ['%d%%' % val for val in values])
print(values * value_increment, ['%d%%' % val for val in values])

x=np.linspace(0,8,7)
plt.xticks(x, columns, rotation='vertical')
#plt.xticks(np.linspace(0,8,7),columns)
plt.show()
'''


import numpy as np
import matplotlib.pyplot as plt

values = np.arange(0, 120, 20)

x = np.linspace(1,18,18)
y = [40,55,60,60,70,50,50,70,70,65,90,90,50,75,50,50,40,40]
z = [0]*len(y)
z2 = [0]*len(y)
for i in range(len(y)):
  z[i]=(1-y[i]/100,1-y[i]/100,1-y[i]/100)
  z2[i] = (y[i]/100,y[i]/100,y[i]/100)

plt.rcParams["font.weight"] = "bold"
fig = plt.figure()
fig.set_facecolor((1.0, 1.0, 0.9))
ax = plt.gca()
ax.set_facecolor((.8, 1, 1))
#z=[(1-y/100,1-y/100,1-y/100)]
labels = ['Asm', 'C', 'C++', 'C#', 'CSS', 'Dart', 'Go', 'HTML', 'Java', 'JavaScript', 'LaTex', 'MATLAB', 'PHP', 'Python', 'R', 'MySql', 'Verilog', 'XML']



for i in range(len(x)):
   plt.bar(x[i],y[i], color = z[i], edgecolor = z2[i], linewidth = 2)

# You can specify a rotation for the tick labels in degrees or with keywords.
plt.xticks(x, labels, rotation='vertical',fontsize=15)
plt.yticks([0,20,40,60,80,99,100],['0%','20%','40%','60%','80%','100%','110%'],fontsize=15)
# Pad margins so that markers don't get clipped by the axes
plt.margins(0.02,0.1)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.15)


plt.show()







import numpy as np
import matplotlib.pyplot as plt

values = np.arange(0, 120, 20)

x = np.linspace(1,18,18)

y = [40,55,60,60,70,50,50,70,70,65,90,90,50,75,50,50,40,40]

labels = ['Asm', 'C', 'C++', 'C#', 'CSS', 'Dart', 'Go', 'HTML', 'Java', 'JS', 'LaTex', 'MATLAB', 'PHP', 'Python', 'R', 'SQL', 'Verilog', 'XML']
z = [0]*len(y)
z2 = [0]*len(y)
for i in range(len(y)):
  z[i]=(1-y[i]/100,1-y[i]/100,1-y[i]/100)
  z2[i] = (y[i]/100,y[i]/100,y[i]/100)

plt.rcParams["font.weight"] = "bold"
fig = plt.figure()
fig.set_facecolor((1.0, 1.0, 0.9))
ax = plt.gca()
ax.set_facecolor((.8, 1, 1))
#z=[(1-y/100,1-y/100,1-y/100)]




for i in range(len(x)):
   plt.barh(x[i],y[i], color = z[i], edgecolor = z2[i], linewidth = 2)

# You can specify a rotation for the tick labels in degrees or with keywords.
plt.yticks(x, labels, rotation='horizontal',fontsize=15)
plt.xticks([0,20,40,60,80,99],['0%','20%','40%','60%','80%','100%'],fontsize=15,rotation='vertical')
# Pad margins so that markers don't get clipped by the axes
plt.margins(0.1,0.02)
# Tweak spacing to prevent clipping of tick-labels
#plt.subplots_adjust(bottom=0)
plt.gca().invert_yaxis()
plt.gca().invert_xaxis()
ax.yaxis.tick_right()
ax.xaxis.tick_top()
plt.show()