from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Plotter import Plotter
import tkinter.messagebox as ms


class UserInterface:

    def __init__(self):
        # Objects and Variables Initialization
        self.plotter = Plotter()
        self.root = Tk()
        self.NAME = 'Equation Plotting'
        self.WIDTH = 800
        self.HEIGHT = 600
        self.fig = Figure(figsize=(8, 4))
        plot1 = self.fig.add_subplot(111)
        plot1.plot(1, 1)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.checkFlag = 1
        self.equation = StringVar(self.root, "")
        self.minLimit = IntVar(self.root, -10)
        self.maxLimit = IntVar(self.root, 10)

    def showErrorMessage(self):
        if self.checkFlag == 0:
            ms.showerror("Empty Cell", "Please Enter the Empty Cell")

    def plotFunction(self):
        self.fig, self.checkFlag = self.plotter.plotFunction(self.equation.get(), self.minLimit.get(), self.maxLimit.get())
        if self.checkFlag == 1:
            self.updateFigure()
        else:
            self.showErrorMessage()

    def updateFigure(self):
        self.canvas.close_event()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().place(x=0, y=0)
        self.canvas.draw()

    def buildUI(self):
        self.root.title(self.NAME)
        self.root.geometry(str(self.WIDTH) + 'x' + str(self.HEIGHT))
        self.root.config(bg="#DECBA4")
        self.root.resizable(False, False)

        # Create Canvas to draw the plot
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

        # Create Equation Label & Entry
        label = StringVar()
        l = Label(self.root, textvariable=label)
        label.set("Equation: ")
        l.config(font=('Comic Sans MS bold', 10), fg="#000", bg="#DECBA4")
        l.pack()
        l.place(x=20, y=415)

        e = Entry(self.root, textvariable=self.equation, width=40)
        e.config(font=('Comic Sans MS bold', 10), fg="#000", bg="#FFF")
        e.place(x=100, y=417)

        # Create The Plot Button
        b = Button(self.root, text="Plot", width=30, command=self.plotFunction)
        b.config(font=('Comic Sans MS bold', 12), fg="#000000", bg="#FFF")
        b.place(x=450, y=410)

        # Create Min Limit Label & Entry
        l = Label(self.root, textvariable=label)
        label.set("Min Limit: ")
        l.config(font=('Comic Sans MS bold', 10), fg="#000", bg="#DECBA4")
        l.place(x=20, y=465)

        e = Entry(self.root, textvariable=self.minLimit)
        e.config(font=('Comic Sans MS bold', 10), fg="#000", bg="#FFF")
        e.place(x=100, y=467)

        # Create Max Limit Label & Entry
        l = Label(self.root, textvariable=label)
        label.set("Max Limit: ")
        l.config(font=('Comic Sans MS bold', 10), fg="#000", bg="#DECBA4")
        l.place(x=20, y=510)

        e = Entry(self.root, textvariable=self.maxLimit)
        e.config(font=('Comic Sans MS bold', 10), fg="#000", bg="#FFF")
        e.place(x=100, y=512)

        self.root.mainloop()
