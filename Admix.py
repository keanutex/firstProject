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
        list = None
        self.kValue = None
        self.N = None  # number of lines in the admixture files which shud be the same
        self.FamList = []
        self.CoordinateList = []
        self.PheList = []
        self.catagory = []
        self.xAxisPos = []

    def readFile1(self, fileName1):
        with open (fileName1) as myFile1:
            lines = myFile1.read().splitlines()

        s = lines[0]
        t = s.split()
        k = len(t)
        emptyList = []
        for l in range(k):
            self.FamList.append(emptyList)  #creates a list of empty lists first so that append doesnt have to be used later

        for m in range(k):
            vals =[]
            for i in range(len(lines)):
                s = lines[i]
                t = s.split()
                vals.append(t[m])
            self.FamList[m] = vals


#-------------------------------------------------------------------------------------------------
#Second File

    def readFile2(self, fileName2):

        with open(fileName2) as myFile2:
            list = myFile2.read().splitlines()

        self.N= len(list)  #gets lenght of self.list

        lines = []
        sum = []
        for i in range(self.N):
            s = list[i]
            t = s.split()        #splits the line with different co-ordinate values
            lines.append(t)
            sumVals = 0
            for index in range(len(t)):
                sumVals = sumVals+ float(t[index])
            sum.append(sumVals)

        self.kValue = len(lines[0])      #gets k value
        emptyList = []
        for l in range(self.kValue):
            self.CoordinateList.append(emptyList)  #creates a list of empty lists first so that append doesnt have to be used later

        for m in range(self.kValue):
            vals =[]
            for i in range(self.N):
                # s = self.list[i]
                # t = s.split()
                vals.append((float(lines[i][m])/sum[i]) *100)

            self.CoordinateList[m] = vals

        for m in range(self.kValue):
            self.CoordinateList[m] = np.array(self.CoordinateList[m])

        np.column_stack(self.CoordinateList)
        # print(self.CoordinateList)



            #for index in range(len(t)):
                #listVals[index] = (listVals[index]/sumVals) *100

#----------------------------------------------------------------------------------------------------------------------

#Third File

    def readFile3 (self, fileName3,pheCol):

        with open(fileName3) as myFile3:
            lines = myFile3.read().splitlines()

        s = lines[0]
        t = s.split()
        k = len(t)
        emptyList = []
        for l in range(k):
            self.PheList.append(emptyList)  #creates a list of empty lists first so that append doesnt have to be used later

        for m in range(k):
            vals =[]
            for i in range(len(lines)):
                s = lines[i]
                t = s.split()
                vals.append(t[m])
            self.PheList[m] = vals

#create the x labels properly
        catagoryCol = self.PheList[pheCol]
        counter = 0
        self.catagory.append('--------------')
        self.catagory.append(catagoryCol[0])
        self.xAxisPos.append(counter)
        for position,string in enumerate(catagoryCol):
            check= False
            max = 0
            counter = counter +1
            for i in range(0,len(self.catagory)):
                if string==self.catagory[i]:
                    #self.color.append(colorHex[i])
                    check = True
                    max = i
            if check==False:
                self.catagory.append('--------------')
                self.catagory.append(string)
                self.xAxisPos.append((self.xAxisPos[len(self.xAxisPos)-1] + counter) / 2)
                self.xAxisPos.append(counter)
                #self.color.append(colorHex[max+1])
        self.xAxisPos.append((self.xAxisPos[len(self.xAxisPos)-1] + counter) / 2)
        self.xAxisPos.append(counter)
        self.catagory.append('--------------')




#----------------------------------------------------------------------------------------------------------------------
    #Check if file3 = file1

    def checkIfFilesEqual (self):

        if ((self.PheList[0] == self.FamList[0]) or (self.PheList[1] == self.FamList[1])):
            print ("Family and Individual Identifiers match")
        else:
            print("Fam and Phe files identifiers do not match")

#----------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------------

#Plot Graphs

    def plotGraph(self,colorHex):



        ind = np.arange(self.N)  #places it into numbers i.e. [1,2,3,4...N]

        #print(self.x)
        #print(self.y)

        '''width=2
        p1 = plt.bar(ind, x, width)
        p2 = plt.bar(ind,y, width,bottom=y)
        
        '''
        arr = [0,200,400,600,1200]
        plt.xticks(self.xAxisPos,self.catagory, rotation=90)
        plt.stackplot(ind, self.CoordinateList, colors =colorHex)
        plt.ylabel('k = ' + str(self.kValue))
        plt.show()


colors = ['#0000FF','#FF0000','#008000','#00FF00','#FFFF00','#00FFFF','#008080','#C0C0C0','#FF00FF','#800080','#008000','#000000']
plotter = admixPlotter()
plotter.readFile1('small.fam')
plotter.readFile2('small.Q.2')
plotter.readFile3('small.phe',4)
plotter.checkIfFilesEqual()
plotter.plotGraph(colors)
