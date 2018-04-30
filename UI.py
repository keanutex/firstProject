from tkinter import *
from tkinter import Menu
import tkinter as tk
from tkinter.filedialog import askopenfile

 
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

def importDataFile():
    admixData = askopenfile(initialdir = "/",title = "Select file",filetypes = (("Data Files","*"),("all files","*.*")))
    print (admixData)

def importFamFile():
    admixData = askopenfile(initialdir = "/",title = "Select file",filetypes = (("Fam Files","*.fam"),("all files","*.*")))
    print (admixData)

def importPhenoFile():
    admixData = askopenfile(initialdir = "/",title = "Select file",filetypes = (("Phenotype Files","*.phe"),("all files","*.*")))
    print (admixData)

def openAdmixWindow():
    admixWin = Toplevel()
    admixWin.geometry("500x500")
    Label(admixWin, text='Admixture Input Files').pack()
    importDataFileAdmix = Button(admixWin, text='Import Data File', command = importDataFile).pack(anchor = W)
    importFamFileAdmix = Button(admixWin, text='Import Fam File', command = importFamFile).pack(anchor = W)
    importPhenoFileAdmix = Button(admixWin, text='Import Phenotype File', command = importPhenoFile).pack(anchor = W)
    cancelButton = Button(admixWin, text='Cancel').pack(side = LEFT, anchor = S)
    backButton = Button(admixWin, text='Back').pack(side = LEFT, anchor = S)
    nextButton = Button(admixWin, text='Next').pack(side = LEFT, anchor = S)
    finishButton = Button(admixWin, text='Finish').pack(side = LEFT, anchor = S)

def openPCAWindow():
    PCAWin = Toplevel()
    PCAWin.geometry("500x500")
    Label(PCAWin, text='PCA Input Files').pack()
    importDataFilePCA = Button(PCAWin, text='Import Data File', command = importDataFile).pack(anchor = W)
    importPhenoFilePCA = Button(PCAWin, text='Import Phenotype File', command = importPhenoFile).pack(anchor = W)
    cancelButton = Button(PCAWin, text='Cancel').pack(side = LEFT, anchor = S)
    backButton = Button(PCAWin, text='Back').pack(side = LEFT, anchor = S)
    nextButton = Button(PCAWin, text='Next').pack(side = LEFT, anchor = S)
    finishButton = Button(PCAWin, text='Finish').pack(side = LEFT, anchor = S)
    

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