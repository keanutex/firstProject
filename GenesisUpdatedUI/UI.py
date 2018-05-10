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


#----------------------Colour Options------------------------------------------------

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

#---------------------------------------------------------------------

PCAplotter = demo.PCAPlotter()
AdmixPlotter = Admix.admixPlotter()

def importDataFilePCA():
    PCAData = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Data Files",".evec"),("all files","*.*")))
    PCAplotter.readFile2(PCAData)


def importPhenoFilePCA():
    PCAPheno = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Phenotype Files","*.phe"),("all files","*.*")))
    #plotter.readFile2('comm-SYMCL.pca.evec')
    PCAplotter.readFile1(PCAPheno)

def drawPCAGraph():
        PCAplotter.connectFilesAddColour()
        PCAplotter.plotGraph()


def importDataFileAdmix():
    AdmixData = askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Data Files","*"),("all files","*.*")))
    AdmixPlotter.readFile2(AdmixData)
    return

def importFamFileAdmix():
    return

def importPhenoFileAdmix():

    AdmixPheno = askopenfilename(initialdir="/", title="Select file",
                               filetypes=(("Phenotype Files", "*.phe"), ("all files", "*.*")))
    AdmixPlotter.readFile1(AdmixPheno)

    return

def drawAdmixGraph():
    AdmixPlotter.plotGraph()
    return



def openAdmixWindow():
    admixWin = Toplevel()
    admixWin.geometry("500x500")
    Label(admixWin, text='Admixture Input Files').pack()
    importDataFileAdmixBut = Button(admixWin, text='Import Data File', command = importDataFileAdmix).pack(anchor = W)
    importFamFileAdmixBut = Button(admixWin, text='Import Fam File', command = importFamFileAdmix).pack(anchor = W)
    importPhenoFileAdmixBut = Button(admixWin, text='Import Phenotype File', command = importPhenoFileAdmix).pack(anchor = W)
    cancelButton = Button(admixWin, text='Cancel').pack(side = LEFT, anchor = S)
    backButton = Button(admixWin, text='Back').pack(side = LEFT, anchor = S)
    nextButton = Button(admixWin, text='Next').pack(side = LEFT, anchor = S)
    finishButton = Button(admixWin, text='Finish', command = drawAdmixGraph).pack(side = LEFT, anchor = S)


def openPCAWindow():
    PCAWin = Toplevel()
    PCAWin.geometry("500x500")
    Label(PCAWin, text='PCA Input Files').pack()
    importDataFilePCABut = Button(PCAWin, text='Import Data File', command = importDataFilePCA).pack(anchor = W)
    importPhenoFilePCABut = Button(PCAWin, text='Import Phenotype File', command = importPhenoFilePCA).pack(anchor = W)
    cancelButton = Button(PCAWin, text='Cancel').pack(side = LEFT, anchor = S)
    backButton = Button(PCAWin, text='Back').pack(side = LEFT, anchor = S)
    nextButton = Button(PCAWin, text='Next').pack(side = LEFT, anchor = S)
    finishButton = Button(PCAWin, text='Finish', command = drawPCAGraph).pack(side = LEFT, anchor = S)

admixButton = tk.Button(frame,
                   text="Admix",
                   command = openAdmixWindow)
admixButton.pack(side=tk.LEFT)

pcaButton = tk.Button(frame,
                   text="PCA",
                   command = openPCAWindow)
pcaButton.pack(side=tk.LEFT)

saveButton = tk.Button(frame,
                   text="Save Project")
saveButton.pack(side=tk.LEFT)


loadButton = tk.Button(frame,
                   text="Load Project")
loadButton.pack(side=tk.LEFT)


dataOptionsButton = tk.Button(frame,
                   text="Data Options")
dataOptionsButton.pack(side=tk.LEFT)


appearanceOptionsButton = tk.Button(frame,
                   text="Appearance Options")
appearanceOptionsButton.pack(side=tk.LEFT)


refreshButton = tk.Button(frame,
                   text="Refresh")
refreshButton.pack(side=tk.LEFT)


rotateButton = tk.Button(frame,
                   text="Rotate")
rotateButton.pack(side=tk.LEFT)


findIndividualsButton = tk.Button(frame,
                   text="Find Individuals")
findIndividualsButton.pack(side=tk.LEFT)


unhideButton = tk.Button(frame,
                   text="Unhide")
unhideButton.pack(side=tk.LEFT)



drawLineButton = tk.Button(frame,
                   text="Draw Lines")
drawLineButton.pack(side=tk.LEFT)



exportImageButton = tk.Button(frame,
                   text="Export Image")
exportImageButton.pack(side=tk.LEFT)


closeProjectButton = tk.Button(frame,
                   text="Close Project")
closeProjectButton.pack(side=tk.LEFT)

mainWindow.mainloop()
