import numpy as np                    #package is used for multidimentional arrays
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  #package used to create 3D graphs


class PCAPlotter(object):
    def __init__(self):
        self.PheFile = None
        self.EvecFile = None
        self.EigVals = []
        self.col1 = []
        self.col2 = []
        self.col3 = []
        self.color = []
        self.coloumnPhe = []
        self.coloumnEvec = []
        self.getMaxColumn = 0
        self.categories = []

    def reset(self):
        self.PheFile = None
        self.EvecFile = None
        self.EigVals = []
        self.col1 = []
        self.col2 = []
        self.col3 = []
        self.color = []
        self.a = []
        self.b = []
        self.bcol = []
        self.coloumnPhe = []
        self.coloumnEvec = []
        self.getMaxColumn = 0



    def readFile1(self, fileName1):
        with open(fileName1) as self.PheFile:                #Open and read into comm(Phenotype)file
            ListOfLines = self.PheFile.read().splitlines()              #Return list with all lines in a string


        emptyList = []
        firstLine = ListOfLines[0]
        words = firstLine.split()          #splits the first line into a list of strings
        numberOfWords = len(words)         #returns the number of words contained in the first line

        for i in range(numberOfWords):                 #For loop is used to initiallly occupy the PhenoList with emptylists
            self.coloumnPhe.append(emptyList)

        for j in range(numberOfWords):  #For loops used to occupy the PhenotypeList with lists in coloumn format i.e. [ [coloumn1], [coloumn2],...[coloumnN] ]
            coloumn =[]
            for k in range(len(ListOfLines)):
                line = ListOfLines[k]
                wordsInLine = line.split()
                coloumn.append(wordsInLine[j])

            self.coloumnPhe[j] = coloumn

#-------------------------------------------------------------------------------------------

#Second File
    def readFile2(self, fileName2):

        with open(fileName2) as EvecFile:
            next(EvecFile)                                #Skip over first line of file
            ListOfLines = EvecFile.read().splitlines()          #lines are the list of lines

        for i in range(len(ListOfLines)):
            line = ListOfLines[i]
            newLine = line.replace(":", "\t")          #Replace any colon found with a tab, to seperate columns
            ListOfLines[i] = newLine
            words = newLine.split()
            self.EigVals.append((words[0]))                      #Populates the Individual Identifier List containing eigenvalues

        emptyList = []
        firstLine = ListOfLines[0]
        words = firstLine.split()          #splits the first line into a list of strings
        numberOfWords = len(words)         #returns the number of words contained in the first line

        notAllowedColoums = 0
        for i in range(numberOfWords):
            self.coloumnEvec.append(emptyList)

                                                #For loops used to occupy the EvecList with lists in coloumn format i.e. [ [coloumn1], [coloumn2],...[coloumnN] ]
        for j in range(0,numberOfWords):        #With the exception that it will only store coloumns with values and disregard coloumns with strings
            values =[]
            isNum = True
            for k in range(len(ListOfLines)):
                line = ListOfLines[k]
                words = line.split()

                try:                           # Determines if a word is a number and if not informs a variable
                    values.append(float(words[j]))
                except ValueError:
                    isNum = False
                    pass

            if (isNum == True):
                self.coloumnEvec[j] = values   #if a coloumn contains only numerical values, it will add it to the EvecList
            else:
                notAllowedColoums= notAllowedColoums + 1   #Updates the variable on the number of coloumns that contain stings

        for n in range(notAllowedColoums):   #Removes empty lists from the EvecList
            self.coloumnEvec.remove([])





#-------------------------------------------------------------------------------------

# Connect files and add self.color
    def connectFilesAddColour(self,evecCol1,evecCol2,evecCol3,pheCol):

        index1 = [i for i, item in enumerate(self.EigVals) if item in self.coloumnPhe[0]]
        LinkedEigenVals1 = [self.EigVals[i] for i in index1]                        #returns list that gives only the values indexed to right eigenvalue from EvecFile
        for j in range(len(self.coloumnEvec)):
            self.coloumnEvec[j] = [self.coloumnEvec[j][i] for i in index1]          #Updates the EvecList with values that correspond correctly with eignevalues of the PheList


        if (len(self.coloumnEvec) < 3):                                          #precaution against the possibility that the EvecList only has 2 coloumns, thus a 3D graph cant be rendered
            emptylist = []
            for j in range(len(self.coloumnEvec[0])):
                 emptylist.append(0)
            self.coloumnEvec.append(emptylist)

        self.col1 = self.coloumnEvec[evecCol1]          #List of X Values
        self.col2 = self.coloumnEvec[evecCol2]          #List of Y Values
        self.col3 = self.coloumnEvec[evecCol3]          #List of Z values
        catagoryCol = self.coloumnPhe[pheCol]           #List of values in the chosen Catagory coloumn

        index2 = [n for n, item in enumerate(self.EigVals) if item in self.coloumnPhe[0]]
        LinkedEigenVals2 = [self.EigVals[n] for n in index2]                              #returns list that gives only the values indexed to right eigenvalue from PheFile
        catagoryCol = [catagoryCol[n] for n in index2]                                    #removes lines of the catagory coloumn that do not have matching eigenvalues in the EvecList

        colorHex = ['#C0C0C0','#FF0000','#FFFF00','#00FF00','#008000','#00FFFF','#008080','#0000FF','#FF00FF','#800080','#008000','#000000']    #List of colours used for the graphs

        self.categories.append(catagoryCol[0])              #Loops are used to Create a list of Catagories in the selected cataogry coloumn of the PhenotypeFile
        for position,string in enumerate(catagoryCol):         #and store the Colours used to indicate the different Catagories
            isKnownCatagory= False
            max = 0
            for i in range(0,len(self.categories)):
                if string==self.categories[i]:
                    self.color.append(colorHex[i])
                    isKnownCatagory = True
                    max = i
            if isKnownCatagory==False:
                self.categories.append(string)
                self.color.append(colorHex[max+1])

#-------------------------------------------------------------------------------------------------------
    def plotGraph(self):
#Plot as graph

        colorHex = ['#C0C0C0', '#FF0000', '#FFFF00', '#00FF00', '#008000', '#00FFFF', '#008080', '#0000FF', '#FF00FF','#800080', '#008000', '#000000']
        fig = plt.figure()
        ax = plt.axes(projection='3d')     #Indicates that the graph will have three dimension and be ploted in 3D
        ax.set_xlabel('X Label')           #Labels the X,Y,Z axes
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')

        for i in range(len(self.categories)):         #Creates the data needed for the Legend
            x = self.col1[len(self.col1)-1]
            y = self.col2[len(self.col2)-1]
            ax.scatter(x, y, c = colorHex[i], s = 5, label = self.categories[i], alpha=1)
        ax.legend()

        ax.scatter3D(self.col1, self.col2, self.col3, s=5, c=self.color);      #Provides the coordinates used to plot the graph
        plt.show()                                                              #Plots and Displays the graph


    def getMaxColumnEvec(self):                 #Function used to give the user the maximum number of coloumns the user can choose from for EvecList
        return len(self.coloumnEvec)

    def getMaxColumnPheno(self):              #Function used to give the user the maximum number of coloumns the user can choose from for PhenoList
        return len(self.getMaxColumnPheno)


# plotter = PCAPlotter()
# plotter.readFile1('comm.phe')
# plotter.readFile2('comm-SYMCL.pca.evec')
# plotter.connectFilesAddColour(1,2,4,2)
# plotter.plotGraph()