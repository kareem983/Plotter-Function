from tkinter import *
from tkinter.ttk import Combobox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PlotStatus import PlotStatus
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
        self.status_message = ""
        self.equation = StringVar(self.root, "x")
        self.minLimit = StringVar(self.root, "-10")
        self.maxLimit = StringVar(self.root, "10")
        self.selected_equation = StringVar(self.root, "")
        self.common_equations = ('X', 'X^2', 'X^3', '5 / (x^2)', '5', '(x+5) / (x)')

    def showErrorMessage(self):
        ms.showerror("ERROR: InValid Input", self.status_message)

    def plotFunction(self):
        try:
            self.status_message = self.plotter.validate(self.equation.get(), self.minLimit.get(), self.maxLimit.get())
            if self.status_message == PlotStatus.no1.value:  # if Dene
                self.fig = self.plotter.plotFunction(self.minLimit.get(), self.maxLimit.get())
                self.updateFigure()
            else:
                self.showErrorMessage()
        except:
            self.status_message = PlotStatus.no4.value
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
        e.config(font=('Comic Sans MS bold', 10), fg="#008000", bg="#FFF")
        e.place(x=100, y=417)

        # Create The Plot Button
        b = Button(self.root, text="PLOT", width=30, command=self.plotFunction)
        b.config(font=('Comic Sans MS bold', 12), fg="#FF0000", bg="#FFF")
        b.place(x=450, y=410)

        # Create Min Limit Label & Entry
        label = StringVar()
        l = Label(self.root, textvariable=label)
        label.set("Min X Limit: ")
        l.config(font=('Comic Sans MS bold', 10), fg="#000", bg="#DECBA4")
        l.place(x=20, y=465)

        e = Entry(self.root, textvariable=self.minLimit)
        e.config(font=('Comic Sans MS bold', 10), fg="#008000", bg="#FFF")
        e.place(x=120, y=467)

        # Create Max Limit Label & Entry
        label = StringVar()
        l = Label(self.root, textvariable=label)
        label.set("Max X Limit: ")
        l.config(font=('Comic Sans MS bold', 10), fg="#000", bg="#DECBA4")
        l.place(x=20, y=510)

        e = Entry(self.root, textvariable=self.maxLimit)
        e.config(font=('Comic Sans MS bold', 10), fg="#008000", bg="#FFF")
        e.place(x=120, y=512)

        # Create Max Limit Label & Entry
        label = StringVar()
        l = Label(self.root, textvariable=label)
        label.set("Common Equations: ")
        l.config(font=('Comic Sans MS bold', 10), fg="#000", bg="#DECBA4")
        l.place(x=450, y=465)

        equation_choose = Combobox(self.root, width=20, font=('Comic Sans MS bold', 10), textvariable=self.selected_equation)
        equation_choose.place(x=578, y=467)
        equation_choose['values'] = self.common_equations
        equation_choose.current(0)
        equation_choose.bind("<<ComboboxSelected>>", self.selectedEquation)

        self.root.mainloop()

    def selectedEquation(self, event):
        self.equation.set(self.selected_equation.get())
