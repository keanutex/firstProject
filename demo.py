import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



#-----------------------------------------------------------------------------------------------

#First File

with open ('comm.phe') as myfile:                #Open and read into comm(PCA)file
 lines = myfile.read().splitlines()              #Return list with all lines in a string

a = []                                          #Create empty list
b = []

for i in range (len(lines)):
    s = lines[i]                                #Returns lines in list
    t = s.split()                               #Splits lines into columns
    a.append(t[0])                              #Adds 0th column into list
    b.append(t[3])



#-------------------------------------------------------------------------------------------

#Second File

with open('comm-SYMCL.pca.evec') as myFile:
    next(myFile)                                #Skip over first line of file
    list = myFile.read().splitlines()

x = []
col1 = []
col2 = []
col3 = []
col4 = []


for i in range(len(list)):
    s = list[i]
    m = s.replace(":", "\t")          #Replace any colon found with a tab, to seperate columns
    t = m.split()
    x.append((t[0]))
    col1.append(float(t[2]))
    col2.append(float(t[3]))
    col3.append(float(t[4]))


print (x)


#-------------------------------------------------------------------------------------

# Connect files and add color


index = [i for i, item in enumerate(x) if item in a]
T = [x[i] for i in index] # gives only the values indexed to right eigenvalue
col1 = [col1[i] for i in index]
col2 = [col2[i] for i in index]
col3 = [col3[i] for i in index]

print (col1)


color = []
for position,string in enumerate(b):
        if string=='EUR':
            color.append('#ff0000')
        if string == 'ASN':
            color.append('#00ff00')
        if string == 'AFR':
            color.append('#0000ff')

color = [color[i] for i in index]
#-------------------------------------------------------------------------------------------------------

#Plot as graph

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.scatter3D(col1, col2, col3,s=1,c=color);
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()



