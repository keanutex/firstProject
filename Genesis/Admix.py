import numpy as np                                       #Used for multi-dimensional arrays
import matplotlib.pyplot as plt                             #Used to plot graph




class admixPlotter():                                               #Class for Plotting Admixture Graph
    def __init__(self):                                         #Declare variables
        self.famFile = None
        self.dataFile = None
        list = None
        self.kValue = None
        self.N = None
        self.FamList = []
        self.CoordinateList = []
        self.PheList = []
        self.catagory = []
        self.xAxisPos = []
        self.MaxColumn = 0

    def reset(self):                                        #Variable Reset
        self.famFile = None
        self.dataFile = None
        list = None
        self.kValue = None
        self.N = None
        self.FamList = []
        self.CoordinateList = []
        self.PheList = []
        self.catagory = []
        self.xAxisPos = []
        self.MaxColumn = 0


    # ---------------------------------------------------------------------------------------------
    # First File

    def readFile1(self, fileName1):                                                          #Function to read in File 1 - Fam File
        with open(fileName1) as famFile:                                                       # Open file and returns a list with all the lines in a string
            listofLines = famFile.read().splitlines()

        firstLine = listofLines[0]                                            #returns first line of file
        lineString = firstLine.split()                                           #Splits line into list of strings
        wordsinString = len(lineString)                                              #returns number of words in the string
        emptyList = []

        for l in range(wordsinString):
            self.FamList.append(emptyList)                                  # creates a list of empty lists first so that append doesnt have to be used later

        for m in range(wordsinString):
            vals = []

            for i in range(len(listofLines)):
                lines = listofLines[i]
                lineString = lines.split()
                vals.append(lineString[m])                                  #appends values to string

            self.FamList[m] = vals

    # -------------------------------------------------------------------------------------------------
    # Second File

    def readFile2(self, fileName2):

        with open(fileName2) as dataFile:
            listofLines = dataFile.read().splitlines()

        self.N = len(listofLines)                                                   # gets length of listofLines

        lines = []
        sum = []
        emptyList = []


        for i in range(self.N):
            s = listofLines[i]
            lineString = s.split()
            lines.append(lineString)
            sumVals = 0

            for index in range(len(lineString)):
                sumVals = sumVals + float(lineString[index])                        #converts to float and sums values

            sum.append(sumVals)                                                         #Gets sum of all values in the file in case the values dont equal 100%

        self.kValue = len(lines[0])                                                  # gets k value


        for l in range(self.kValue):
            self.CoordinateList.append(emptyList)                               # creates a list of empty lists first so that append doesnt have to be used later

        for m in range(self.kValue):
            values = []

            for i in range(self.N):
                values.append((float(lines[i][m]) / sum[i]) * 100)              #Calculates actual percentage of each value

            self.CoordinateList[m] = values                                     #Store these values into co-ordinate list

        for m in range(self.kValue):
            self.CoordinateList[m] = np.array(self.CoordinateList[m])           #Numpy array

        np.column_stack(self.CoordinateList)                                    #Stacks 1D arrays as columns into 2D array


    # ----------------------------------------------------------------------------------------------------------------------
    # Third File

    def readFile3(self, fileName3):

        with open(fileName3) as pheFile:
            listofLines = pheFile.read().splitlines()

        firstLine = listofLines[0]
        lineString = firstLine.split()
        wordsInString = len(lineString)
        self.MaxColumn = wordsInString
        emptyList = []

        for l in range(wordsInString):
            self.PheList.append(emptyList)                                       # creates a list of empty lists first so that append doesnt have to be used later

        for m in range(wordsInString):
            words = []

            for i in range(len(listofLines)):
                lines = listofLines[i]
                stringLines = lines.split()
                words.append(stringLines[m])

            self.PheList[m] = words

    # ----------------------------------------------------------------------------------------------------------------------
    # Check if file3 = file1

    def checkIfFilesEqual(self):

        if ((self.PheList[0] == self.FamList[0]) or (self.PheList[1] == self.FamList[1])):
            print("Family and Individual Identifiers match")                                    #Check to see if columns in phe and fam files are equal. print error if not
        else:
            print("Fam and Phe files identifiers do not match")


    # ----------------------------------------------------------------------------------------------------------------------
    # Plot Graphs

    def plotGraph(self, colorHex, pheCol):

        catagoryCol = self.PheList[pheCol]                           #The user selected catagory coloumn
        counter = 0
        self.catagory.append('--------------')          #String used as an indicator to demark catagories
        self.catagory.append(catagoryCol[0])
        self.xAxisPos.append(counter)

        for position, string in enumerate(catagoryCol):        #Function is used to determine the postion to place the catagory labels on the graph
            isKnownCatagory = False
            counter = counter + 1
            for i in range(0, len(self.catagory)):
                if string == self.catagory[i]:
                    isKnownCatagory = True

            if isKnownCatagory == False:
                self.catagory.append('--------------')
                self.catagory.append(string)
                self.xAxisPos.append((self.xAxisPos[len(self.xAxisPos) - 1] + counter) / 2)        #calculates the position to place label
                self.xAxisPos.append(counter)

        self.xAxisPos.append((self.xAxisPos[len(self.xAxisPos) - 1] + counter) / 2)         #calculates the last label Position
        self.xAxisPos.append(counter)
        self.catagory.append('--------------')

        ind = np.arange(self.N)                                                          # places it into a List of numbers i.e. [1,2,3,4...N]

        plt.xticks(self.xAxisPos, self.catagory, rotation=90)                          #Show the labels in the correct position angled at 90 degrees
        plt.stackplot(ind, self.CoordinateList, colors=colorHex)
        plt.ylabel('k = ' + str(self.kValue))                                          #Show k value on Y Axis
        plt.show()                                                                     #Show graph

    # ----------------------------------------------------------------------------------------------------------------------
    # Get Columns number

    def getColumnMax(self):
        return self.MaxColumn
