from matplotlib.figure import Figure
import numpy as np

from PlotStatus import PlotStatus


class Plotter:
    def __init__(self):
        self.plot_status = ""
        self.limitCheckFlag = 1

    def validateMinMax(self, minLimit, maxLimit):
        if len(minLimit) == 0 or len(maxLimit) == 0:
            self.plot_status = PlotStatus.no0.value
        elif not (minLimit.lstrip("-").isdigit()) or not (maxLimit.lstrip("-").isdigit()):
            self.plot_status = PlotStatus.no2.value
        elif int(maxLimit) <= int(minLimit):
            self.plot_status = PlotStatus.no3.value
        else:
            self.plot_status = PlotStatus.no1.value

    def validateEquation(self, equation):
        pass

    def validate(self, equation, minLimit, maxLimit):
        self.validateMinMax(minLimit, maxLimit)
        self.validateEquation(equation)

        return self.plot_status

    def plotFunction(self, equation, minLimit, maxLimit):
        minLimit = int(minLimit)
        maxLimit = int(maxLimit)
        x = np.linspace(minLimit, maxLimit, 100)
        tst = f"" + equation
        y = eval(tst)

        fig = Figure(figsize=(8, 4))
        plot1 = fig.add_subplot(111)
        plot1.plot(x, y)

        return fig
