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



    def readFile1(self, fileName1):
        with open (fileName1) as self.myFile1:                #Open and read into comm(PCA)file
            lines = self.myFile1.read().splitlines()              #Return list with all lines in a string



        for i in range (len(lines)):
            s = lines[i]                                #Returns lines in list
            t = s.split()                               #Splits lines into columns
            self.a.append(t[0])                              #Adds 0th column into list
            self.b.append(t[3])
#-------------------------------------------------------------------------------------------

#Second File
    def readFile2(self, fileName2):

        with open(fileName2) as myFile2:
            next(myFile2)                                #Skip over first line of file
            list = myFile2.read().splitlines()




        for i in range(len(list)):
            s = list[i]
            m = s.replace(":", "\t")          #Replace any colon found with a tab, to seperate columns
            t = m.split()
            self.x.append((t[0]))
            self.col1.append(float(t[2]))
            self.col2.append(float(t[3]))
            self.col3.append(float(t[4]))


        print (self.x)


#-------------------------------------------------------------------------------------

# Connect files and add self.color
    def connectFilesAddColour(self):

        index = [i for i, item in enumerate(self.x) if item in self.a]
        T = [self.x[i] for i in index] # gives only the values indexed to right eigenvalue
        col1 = [self.col1[i] for i in index]
        col2 = [self.col2[i] for i in index]
        col3 = [self.col3[i] for i in index]

        print (col1)



        for position,string in enumerate(self.b):
                if string=='EUR':
                    self.color.append('#ff0000')
                if string == 'ASN':
                    self.color.append('#00ff00')
                if string == 'AFR':
                    self.color.append('#0000ff')

        self.color = [self.color[i] for i in index]
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

#plotter = PCAPlotter()
#plotter.readFile1('comm.phe')
#plotter.readFile2('comm-SYMCL.pca.evec')
#plotter.connectFilesAddColour()
#plotter.plotGraph()
