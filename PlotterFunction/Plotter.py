from matplotlib.figure import Figure
import numpy as np


class Plotter:
    def __init__(self):
        pass

    def validateMinMax(self):
        pass

    def validateEquation(self):
        pass

    def plotFunction(self, equation, minLimit, maxLimit):
        x = np.linspace(minLimit, maxLimit, 100)
        tst = f""+equation
        y = eval(tst)

        fig = Figure(figsize=(8, 4))
        plot1 = fig.add_subplot(111)
        plot1.plot(x, y)

        return fig, 1
