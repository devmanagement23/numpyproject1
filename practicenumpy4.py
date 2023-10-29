#Draw a line in a diagram from position (1, 3) to position (8, 10):
#                                       (x1,y1)     to     (x2,y2)

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])      #[x1,x2]
ypoints = np.array([3, 10])     #[y1,y2]

plt.plot(xpoints, ypoints)
plt.show()

#------------------------------------------
#Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()

#Draw a line in a diagram from 
# position (1, 3) to (2, 8) then to (6, 1) and 
#                   finally to position (8, 10):
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints,linewidth = '20.5')
plt.show()

# each point show specificaly bold 
# x points are not given so deafult value of 1,2,3 taken

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o',linestyle = 'dotted',color = 'r')
plt.show()


#Draw two lines by specifiyng the x- and y-point values for both lines:

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()

# new graph
x = np.array([80, 85, 90, 95, 100, 105, 110])
y = np.array([240, 250, 260, 270, 280, 290, 300])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1,loc = 'left')
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)

#plt.grid(axis = 'x')
#plt.grid(axis = 'y')
plt.grid()
#plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()

#---------------------------------------------------
#   MULTIPLE PLOT
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)    # subplot(row,column,position)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)    # subplot(row,column,position)
plt.plot(x,y)

plt.show()

#----------------------------------
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 2, 1)       # subplot(row,column,position)
plt.plot(x,y)
plt.title("SALES")

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 2, 2)       # subplot(row,column,position)
plt.plot(x,y)
plt.title("INCOME")

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 2, 3)       # subplot(row,column,position)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 2, 4)       # subplot(row,column,position)
plt.plot(x,y)


plt.suptitle("MY SHOP")       #SUPER TITLE
plt.show()


#-----------------SCATTER GRAPH-------------

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()

#---------------------------------------
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()

#---------------------------------------

#  BAR GRAPH

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

# ----- Horizontal bars----------

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()

#--------------------
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red", width = 0.1)
plt.show()

#--------------PIE CHART------------------------

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 
#------

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels,shadow = True)
plt.show()
#------

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 

# EXPLODE property
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 

#------------
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 

