import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class PCAPlotter():
    def __init__(self):
        self.myFile1 = None
        self.myFile2 = None
        self.x = []
        self.col1 = []
        self.col2 = []
        self.col3 = []
        self.color = []
        self.a = []
        self.b = []
        self.bcol = []
        self.coloumnPhe = []
        self.coloumnEvec = []

    def readFile1(self, fileName1):
        with open (fileName1) as self.myFile1:                #Open and read into comm(PCA)file
            lines = self.myFile1.read().splitlines()              #Return list with all lines in a string


        emptyList = []
        s = lines[0]
        t = s.split()
        k = len(t)
        for l in range(k):
            self.coloumnPhe.append(emptyList)

        # for i in range (len(lines)):
        #     s = lines[i]                                #Returns lines in list
        #     t = s.split()                               #Splits lines into columns
        #
        #     #k=len(t)
        #     #listVals.append(t)
        #
        #     self.a.append(t[0])                              #Adds 0th column into list
        #     self.b.append(t[3])
        #     self.bcol.append(t[2])



        for m in range(k):
            vals =[]
            for i in range(len(lines)):
                s = lines[i]
                t = s.split()
                vals.append(t[m])

            self.coloumnPhe[m] = vals

        #print(self.coloumnPhe[0])


#-------------------------------------------------------------------------------------------

#Second File
    def readFile2(self, fileName2):

        with open(fileName2) as myFile2:
            next(myFile2)                                #Skip over first line of file
            lines = myFile2.read().splitlines()          #lines are the list of lines


        for i in range(len(lines)):
            s = lines[i]
            m = s.replace(":", "\t")          #Replace any colon found with a tab, to seperate columns
            lines[i] = m
            t = m.split()
            self.x.append((t[0]))
            # self.col1.append(float(t[2]))
            # self.col2.append(float(t[3]))
            # self.col3.append(float(t[4]))

        emptyList = []                                 #creating the coloumns
        s = lines[0]
        t = s.split()
        k = len(t)
        notAllowedColoums = 0
        for l in range(k):
            self.coloumnEvec.append(emptyList)

        for m in range(0,k):
            vals =[]
            isNum = True
            for i in range(len(lines)):
                s = lines[i]
                t = s.split()

                try:
                    vals.append(float(t[m]))
                except ValueError:
                    isNum = False
                    pass

            if (isNum == True):
                self.coloumnEvec[m] = vals
            else:
                notAllowedColoums= notAllowedColoums + 1

        for n in range(notAllowedColoums):
            self.coloumnEvec.remove([])





#-------------------------------------------------------------------------------------

# Connect files and add self.color
    def connectFilesAddColour(self,evecCol1,evecCol2,evecCol3,pheCol):

        index = [i for i, item in enumerate(self.x) if item in self.coloumnPhe[0]]
        T = [self.x[i] for i in index] # gives only the values indexed to right eigenvalue
        for j in range(len(self.coloumnEvec)):
            self.coloumnEvec[j] = [self.coloumnEvec[j][i] for i in index]


        if (len(self.coloumnEvec) < 3):
            emptylist = []
            for j in range(len(self.coloumnEvec[0])):
                 emptylist.append(0)
            self.coloumnEvec.append(emptylist)

        # col1 = [self.col1[i] for i in index]
        # col2 = [self.col2[i] for i in index]
        # col3 = [self.col3[i] for i in index]

        self.col1 = self.coloumnEvec[evecCol1]
        self.col2 = self.coloumnEvec[evecCol2]
        self.col3 = self.coloumnEvec[evecCol3]
        catagoryCol = self.coloumnPhe[pheCol]

        index2 = [n for n, item in enumerate(self.x) if item in self.coloumnPhe[0]]
        T2 = [self.x[n] for n in index]
        catagoryCol = [catagoryCol[n] for n in index]

        #print(self.bcol)

        colorHex = ['#C0C0C0','#FF0000','#FFFF00','#00FF00','#008000','#00FFFF','#008080','#0000FF','#FF00FF','#800080','#008000','#000000']

        catagory = []
        catagory.append(catagoryCol[0])
        for position,string in enumerate(catagoryCol):
            check= False
            max = 0
            for i in range(0,len(catagory)):
                if string==catagory[i]:
                    self.color.append(colorHex[i])
                    check = True
                    max = i
            if check==False:
                catagory.append(string)
                self.color.append(colorHex[max+1])
        '''
        for position,string in enumerate(self.b):
                if string=='EUR':
                    self.color.append('#ff0000')
                if string == 'ASN':
                    self.color.append('#00ff00')
                if string == 'AFR':
                    self.color.append('#0000ff')

        self.color = [self.color[i] for i in index]'''
#-------------------------------------------------------------------------------------------------------
    def plotGraph(self):
#Plot as graph
        fig = plt.figure()
        ax = plt.axes(projection='3d')

        ax.scatter3D(self.col1, self.col2, self.col3,s=1,c=self.color);
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        plt.show()

plotter = PCAPlotter()
plotter.readFile1('comm.phe')
plotter.readFile2('comm-SYMCL.pca.evec')
plotter.connectFilesAddColour(1,2,4,2)
plotter.plotGraph()
