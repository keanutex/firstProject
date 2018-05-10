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
        self.nextList = None
        self.kValue = None
        self.newList = []
        # self.string1 = []
        # self.string2 = []
        # self.string3 = []
        # self.string4 = []
        self.col1 =[]
        self.col2 = []
        self.empty = []
        self.empty1 = []

    def readFile1(self, fileName1):
        with open (fileName1) as myFile1:
            lines = myFile1.read().splitlines()

        xPos = []

        for j in range (len(lines)):
            n = lines[j]
            m = n.split()
            xPos.append(m[3])
            self.col1.append(m[0])
            self.col2.append(m[1])



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
            self.kValue = len(t)
            listVals = []
            sumVals = 0
            for index in range(len(t)):
                listVals.append(float(t[index]))
                sumVals = sumVals+ float(t[index])

            #for index in range(len(t)):
                #listVals[index] = (listVals[index]/sumVals) *100

            self.newList.append(listVals)
            #a = float(t[0])*100
            #b = float(t[1])*100

            #print(listVals)

            self.x.append(listVals[0]/sumVals)    #to get 100%
            self.y.append(listVals[1]/sumVals)

#----------------------------------------------------------------------------------------------------------------------

#Third File

    def readFile3 (self, fileName3):

        with open(fileName3) as myFile3:
            nextList = myFile3.read().splitlines()



        for v in range(len(nextList)):
            a = nextList[v]
            b = a.split()
            self.empty.append(b[0])
            self.empty1.append(b[1])

#----------------------------------------------------------------------------------------------------------------------
    #Check if file3 = file1

    def checkIfFilesEqual (self):



        if self.col1 == self.empty:

            print ("Right files")


        else:
            print ("Wrong Fam/Phe File")

        if self.col2 == self.empty1:
            print ("Right Files")

        else:
            print("Wrong Fam/Phe File")

#----------------------------------------------------------------------------------------------------------------------
#Plot Graphs

    def plotGraph(self):

        N= len(self.list)  #gets lenght of self.list

        ind = np.arange(N)  #places it into numbers i.e. [1,2,3,4...N]

        #print(self.x)
        #print(self.y)

        '''width=2
        p1 = plt.bar(ind, x, width)
        p2 = plt.bar(ind,y, width,bottom=y)
        
        '''
        plt.stackplot(ind, self.x, self.y, colors =['r','c'])
        plt.ylabel('k = ' + str(self.kValue))
        plt.show()
        #print(self.newList)


# plotter = admixPlotter()
# plotter.readFile1('small.phe')
# plotter.readFile2('small.Q.2')
# plotter.readFile3('small.fam')
# plotter.checkIfFilesEqual()
# plotter.plotGraph()
