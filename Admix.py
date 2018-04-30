import numpy as np
import matplotlib.pyplot as plt


#---------------------------------------------------------------------------------------------
#First File


with open ('small.phe') as myfile:
 lines = myfile.read().splitlines()

x = []

for i in range (len(lines)):
    s = lines[i]
    t = s.split()
    x.append(t[3])


color = []

for position,string in enumerate(x):
    if string=='west-africa':
        color.append('#ff0000')
    if string == 'europe':
        color.append('#00ff00')
    if string == 'east-africa':
        color.append('#0000ff')
    if string == 'east-asia':
        color.append('#ffff00')
    if string == 'south-asia':
        color.append('#000000')
    if string == 'north-america':
        color.append('#EE82EE')





#-------------------------------------------------------------------------------------------------

#Second File

with open('small.Q.2') as myFile:
    list = myFile.read().splitlines()

x = []
y = []


for i in range(len(list)):
    s = list[i]
    t = s.split()
    a=float(t[0])*100
    b=float(t[1])*100

    x.append(a/(a+b))    #to get 100%
    y.append(b/(a+b))

#----------------------------------------------------------------------------------------------------------------------
#Plot Graphs

N= len(list)  #gets lenght of list
ind = np.arange(N)  #places it into numbers i.e. [1,2,3,4...N]

print(x)
print(y)
'''width=2

p1 = plt.bar(ind, x, width)
p2 = plt.bar(ind,y, width,bottom=y)
'''

plt.stackplot(ind, x,y, colors =['r','c'])
plt.ylabel('k=2')
plt.show()
