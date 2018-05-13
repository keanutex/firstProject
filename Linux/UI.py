from tkinter import *

from tkinter import Menu

import tkinter as tk
from tkinter import ttk

from tkinter.filedialog import askopenfile
from tkinter.filedialog import askopenfilename

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
LARGE_FONT = ("Verdana", 12)
from matplotlib.figure import Figure

import demo
import Admix

mainWindow = tk.Tk()
mainWindow.geometry("1000x700")
mainWindow.title("Genesis V2.0")
menu = Menu(mainWindow)
frame = tk.Frame(mainWindow)
frame.pack()
new_item = Menu(menu)
new_item.add_command(label='New')
menu.add_cascade(label='File', menu=new_item)
mainWindow.config(menu=menu)


#--------------------------------------------------------------------------

columnAdmix = 0

columnPCAEvec1 = 0
columnPCAEvec2 = 0
columnPCAEvec3 = 0
columnPCAPheno = 0

PCAData = ""
PCAPheno = ""

AdmixData = ""
AdmixFam = ""
AdmixPheno = ""
#----------------------Colour Options------------------------------------------------

# Add column thing

options = [
    "Red",
    "Blue",
    "Green",
    "Yellow",
    "Purple"
]

variable = StringVar(mainWindow)
variable.set("Colours") # default value
colourList = OptionMenu(mainWindow, variable, *options)
colourList.pack()

def getColours():
    print(variable.get())
    return variable.get()


colors = ['#0000FF', '#FF0000', '#008000', '#00FF00', '#FFFF00', '#00FFFF', '#008080', '#C0C0C0', '#FF00FF', '#800080',
          '#008000', '#000000']

#---------------------------------------------------------------------

PCAplotter = demo.PCAPlotter()
AdmixPlotter = Admix.admixPlotter()

def importDataFilePCA():
    global PCAData
    PCAData = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Data Files",".evec"),("all files","*.*")))
    PCAplotter.readFile2(PCAData)


def importPhenoFilePCA():
    global PCAPheno
    PCAPheno = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Phenotype Files","*.phe"),("all files","*.*")))
    #plotter.readFile2('comm-SYMCL.pca.evec')

    PCAplotter.readFile1(PCAPheno)

def drawPCAGraph():
    global columnPCAEvec1
    global columnPCAEvec2
    global columnPCAEvec3
    global columnPCAPheno

    PCAplotter.connectFilesAddColour(int(columnPCAEvec1), int(columnPCAEvec2), int(columnPCAEvec3), int(columnPCAPheno))
    PCAplotter.plotGraph()
    PCAplotter.reset()

    print(columnPCAEvec1)
    print(columnPCAEvec2)
    print(columnPCAEvec3)
    print(columnPCAPheno)


def importDataFileAdmix():
    global AdmixData
    AdmixData = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Data Files","*"),("all files","*.*")))
    AdmixPlotter.readFile2(AdmixData)
    return

def importFamFileAdmix():
    global AdmixFam
    AdmixFam = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Fam Files","*.fam"),("all files","*.*")))
    AdmixPlotter.readFile1(AdmixFam)
    return

def importPhenoFileAdmix():
    global AdmixPheno
    AdmixPheno = askopenfilename(initialdir="/", title="Select file",
                               filetypes=(("Phenotype Files", "*.phe"), ("all files", "*.*")))
    AdmixPlotter.readFile3(AdmixPheno)

    return

def drawAdmixGraph():
   # if(AdmixPlotter.getColumnMax() < columnAdmix):
   #     return
   # print(AdmixPlotter.getColumnMax())
    global columnAdmix
    print(columnAdmix)
    AdmixPlotter.plotGraph(colors, int(columnAdmix))
    AdmixPlotter.reset()
    return

def setNumber(num1):
    global columnAdmix
    columnAdmix = num1
    print(columnAdmix)


def setPCAColumns(num1, num2, num3, num4):
    global columnPCAEvec1
    global columnPCAEvec2
    global columnPCAEvec3
    global columnPCAPheno
    columnPCAEvec1 = num1
    columnPCAEvec2 = num2
    columnPCAEvec3 = num3
    columnPCAPheno = num4
    print(columnPCAEvec1)
    print(columnPCAEvec2)
    print(columnPCAEvec3)
    print(columnPCAPheno)

def openAdmixWindow():
    admixWin = Toplevel()
    admixWin.geometry("500x500")
    Label(admixWin, text='Admixture Input Files').pack()
    importDataFileAdmixBut = Button(admixWin, text='Import Data File', command = importDataFileAdmix).pack(anchor = W)
    importFamFileAdmixBut = Button(admixWin, text='Import Fam File', command = importFamFileAdmix).pack(anchor = W)
    importPhenoFileAdmixBut = Button(admixWin, text='Import Phenotype File', command = importPhenoFileAdmix).pack(anchor = W)

    Label(admixWin, text='Phenotype Column:').pack(anchor = W)

    columnEntry = Entry(admixWin)
    columnEntry.pack(anchor = W)
    enterColumnButton = Button(admixWin, text = "Set Column", command = lambda: setNumber(columnEntry.get())).pack(anchor = W)

    cancelButton = Button(admixWin, text='Cancel').pack(side = LEFT, anchor = S)
    backButton = Button(admixWin, text='Back').pack(side = LEFT, anchor = S)
    nextButton = Button(admixWin, text='Next').pack(side = LEFT, anchor = S)
    finishButton = Button(admixWin, text='Finish', command = drawAdmixGraph).pack(side = LEFT, anchor = S)

    AdmixPlotter.reset()

def openPCAWindow():
    PCAWin = Toplevel()
    PCAWin.geometry("500x500")
    Label(PCAWin, text='PCA Input Files').pack()
    importDataFilePCABut = Button(PCAWin, text='Import Data File', command = importDataFilePCA).pack(anchor = W)
    importPhenoFilePCABut = Button(PCAWin, text='Import Phenotype File', command = importPhenoFilePCA).pack(anchor = W)

    Label(PCAWin, text='EigenVector Columns:').pack(anchor=W)
    columnEvec1Entry = Entry(PCAWin)
    columnEvec1Entry.pack(anchor=W)
    columnEvec2Entry = Entry(PCAWin)
    columnEvec2Entry.pack(anchor=W)
    columnEvec3Entry = Entry(PCAWin)
    columnEvec3Entry.pack(anchor=W)

    Label(PCAWin, text='Phenotype Column: ').pack(anchor=W)
    columnPhenoEntry = Entry(PCAWin)
    columnPhenoEntry.pack(anchor=W)

    enterColumnButton = Button(PCAWin, text="Set Column", command=lambda: setPCAColumns(columnEvec1Entry.get(),
                                                                                        columnEvec2Entry.get(),
                                                                                        columnEvec3Entry.get(),
                                                                                        columnPhenoEntry.get())).pack(anchor=W)

    cancelButton = Button(PCAWin, text='Cancel').pack(side = LEFT, anchor = S)
    backButton = Button(PCAWin, text='Back').pack(side = LEFT, anchor = S)
    nextButton = Button(PCAWin, text='Next').pack(side = LEFT, anchor = S)
    finishButton = Button(PCAWin, text='Finish', command = drawPCAGraph).pack(side = LEFT, anchor = S)

    PCAplotter.reset()

def openSavePCA():
    savePCAWin = Toplevel()
    savePCAWin.geometry("500x500")
    Label(savePCAWin, text='Save PCA Project').pack()
    Label(savePCAWin, text='File Name:').pack(anchor=W)
    saveFileNameEntry = Entry(savePCAWin)
    saveFileNameEntry.pack(anchor=W)

    enterColumnButton = Button(savePCAWin, text="SaveFile", command=lambda: saveProjectPCA(saveFileNameEntry.get())).pack(anchor = W)

def saveProjectPCA(saveFileName):
    global PCAData
    global PCAphenP
    global columnPCAEvec1
    global columnPCAEvec2
    global columnPCAEvec3
    global columnPCAPheno


    saveFile = open(saveFileName + ".txt", "w+")
    saveFile.write(PCAData + "\n" + PCAPheno + "\n"+ columnPCAEvec1  + "\n"
                    +  columnPCAEvec2  + "\n"+ columnPCAEvec3  + "\n" + columnPCAPheno)
    saveFile.close()



def loadProjectPCA():
    saveFileName = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Phenotype Files","*"),("all files","*.*")))
    saveFileObject = open(saveFileName)

    i = 0;
    next = saveFileObject.readline()
    PCADataRead = next
    PCADataRead = PCADataRead.strip()

    while i < 5:
        if(i == 0):
            PCAPhenoRead = saveFileObject.readline()
            PCAPhenoRead = PCAPhenoRead.rstrip('\n')
        if(i == 1):
            columnPCAEvec1read = saveFileObject.readline()
            columnPCAEvec1read = columnPCAEvec1read.strip()
        if(i == 2):
            columnPCAEvec2read = saveFileObject.readline()
            columnPCAEvec2read = columnPCAEvec2read.strip()
        if(i == 3):
            columnPCAEvec3read = saveFileObject.readline()
            columnPCAEvec3read = columnPCAEvec3read.strip()
        if(i == 4):
            columnPCAPhenoRead = saveFileObject.readline()
            columnPCAPhenoRead = columnPCAPhenoRead.strip()
        i = i + 1

    PCAPlotterLoad = demo.PCAPlotter()
    PCAPlotterLoad.readFile1(PCAPhenoRead)
    PCAPlotterLoad.readFile2(PCADataRead)
    PCAPlotterLoad.connectFilesAddColour(int(columnPCAEvec1read), int(columnPCAEvec2read), int(columnPCAEvec3read), int(columnPCAPhenoRead))
    PCAPlotterLoad.plotGraph()

pcaButton = tk.Button(frame,
                   text="New PCA Project",
                   command = openPCAWindow)
pcaButton.pack(side=tk.LEFT)

saveButtonPCA = tk.Button(frame,
                   text="Save PCA Project",
                    command = openSavePCA)
saveButtonPCA.pack(side=tk.LEFT)

loadButtonPCA = tk.Button(frame,
                   text="Load PCA Project",
                       command= loadProjectPCA)
loadButtonPCA.pack(side=tk.LEFT)


def openSaveAdmix():
    saveAdmixWin = Toplevel()
    saveAdmixWin.geometry("500x500")
    Label(saveAdmixWin, text='Save Admix Project').pack()
    Label(saveAdmixWin, text='File Name:').pack(anchor=W)
    saveFileNameEntry = Entry(saveAdmixWin)
    saveFileNameEntry.pack(anchor=W)

    enterColumnButton = Button(saveAdmixWin, text="SaveFile", command=lambda: saveProjectAdmix(saveFileNameEntry.get())).pack(anchor = W)

def saveProjectAdmix(saveFileName):
    global AdmixData
    global AdmixFam
    global AdmixPheno
    global columnAdmix

    saveFile = open(saveFileName + ".txt", "w+")
    saveFile.write(AdmixData + "\n" + AdmixFam + "\n"+ AdmixPheno  + "\n"
                    +  columnAdmix)
    saveFile.close()

def loadProjectAdmix():
    saveFileName = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Phenotype Files","*"),("all files","*.*")))
    saveFileObject = open(saveFileName)

    i = 0;
    next = saveFileObject.readline()
    AdmixDataRead = next
    AdmixDataRead = AdmixDataRead.strip()

    while i < 3:
        if(i == 0):
            AdmixFamRead = saveFileObject.readline()
            AdmixFamRead = AdmixFamRead.rstrip('\n')
        if(i == 1):
            admixPhenoRead = saveFileObject.readline()
            admixPhenoRead = admixPhenoRead.strip()
        if(i == 2):
            columnAdmixRead = saveFileObject.readline()
            columnAdmixRead = columnAdmixRead.strip()
        i = i + 1

    AdmixPlotterLoad = Admix.admixPlotter()
    AdmixPlotterLoad.readFile1(AdmixFamRead)
    AdmixPlotterLoad.readFile2(AdmixDataRead)
    AdmixPlotterLoad.readFile3(admixPhenoRead)
    AdmixPlotterLoad.plotGraph(colors, int(columnAdmixRead))

admixButton = tk.Button(frame,
                   text="New Admix Project",
                   command = openAdmixWindow)
admixButton.pack(side=tk.LEFT)

saveButtonAdmix = tk.Button(frame,
                   text="Save Admix Project",
                    command = openSaveAdmix)
saveButtonAdmix.pack(side=tk.LEFT)

loadButtonAdmix = tk.Button(frame,
                   text="Load Admix Project",
                       command= loadProjectAdmix)
loadButtonAdmix.pack(side=tk.LEFT)


dataOptionsButton = tk.Button(frame,
                   text="Data Options")
dataOptionsButton.pack(side=tk.LEFT)


appearanceOptionsButton = tk.Button(frame,
                   text="Appearance Options")
appearanceOptionsButton.pack(side=tk.LEFT)


findIndividualsButton = tk.Button(frame,
                   text="Find Individuals")
findIndividualsButton.pack(side=tk.LEFT)


mainWindow.mainloop()