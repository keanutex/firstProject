import numpy as np
import matplotlib.pyplot as plt

#---------------------------------------------------------------------------------------------

#First File

class admixPlotter():
    def __init__ (self):
        self.myFile1 = None
        self.myFile2 = None
        self.x = []
        self.y = []
        self.list = None

    def readFile1(self, fileName1):
        with open (fileName1) as myFile1:
            lines = myFile1.read().splitlines()

        xPos = []

        for j in range (len(lines)):
            n = lines[j]
            m = n.split()
            xPos.append(m[3])

        color = []

        for position,string in enumerate(xPos):
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

    def readFile2(self, fileName2):

        with open(fileName2) as myFile2:
            self.list = myFile2.read().splitlines()

        for i in range(len(self.list)):
            s = self.list[i]
            t = s.split()
            a = float(t[0])*100
            b = float(t[1])*100

            self.x.append(a/(a+b))    #to get 100%
            self.y.append(b/(a+b))

#----------------------------------------------------------------------------------------------------------------------

#Plot Graphs

    def plotGraph(self):

        N= len(self.list)  #gets lenght of self.list

        ind = np.arange(N)  #places it into numbers i.e. [1,2,3,4...N]

        print(self.x)
        print(self.y)

        '''width=2
        p1 = plt.bar(ind, x, width)
        p2 = plt.bar(ind,y, width,bottom=y)
        
        '''
        plt.stackplot(ind, self.x, self.y, colors =['r','c'])
        plt.ylabel('k=2')
        plt.show()

plotter = admixPlotter()
plotter.readFile1('small.phe')
plotter.readFile2('small.Q.2')
plotter.plotGraph()
