from matplotlib.figure import Figure
import numpy as np
from PlotStatus import PlotStatus


class Plotter:
    def __init__(self):
        self.plot_status = ""
        self.equation = ""
        self.ops = ['+', '-', '*', '/', '^']
        self.brc = ['(', ')']

    def validateMinMax(self, minLimit, maxLimit):
        # Check for the Min/Max X Limit Validation
        if len(minLimit) == 0 or len(maxLimit) == 0:
            self.plot_status = PlotStatus.no0.value
        elif not (minLimit.lstrip("-").isdigit()) or not (maxLimit.lstrip("-").isdigit()):
            self.plot_status = PlotStatus.no2.value
        elif int(maxLimit) <= int(minLimit):
            self.plot_status = PlotStatus.no3.value
        else:
            self.plot_status = PlotStatus.no1.value

    def validateEquation(self):
        # Check for the empty Equation
        if len(self.equation) == 0:
            self.plot_status = PlotStatus.no0.value
        else:
            self.equation = self.equation.replace('^', "**")
            self.equation = self.equation.replace('X', "x")

            # Check for the any char isn't x
            for i in range(len(self.equation)):
                if self.equation[i] == " ":
                    continue
                if not (str(self.equation[i]).isdigit()) and self.equation[i] not in self.ops and self.equation[
                    i] not in self.brc and self.equation[i] != 'x':
                    self.plot_status = PlotStatus.no5.value
                    return

    def validate(self, equation, minLimit, maxLimit):
        self.validateMinMax(minLimit, maxLimit)
        self.equation = equation
        self.validateEquation()

        return self.plot_status

    def plotFunction(self, minLimit, maxLimit):
        minLimit = int(minLimit)
        maxLimit = int(maxLimit)
        x = np.linspace(minLimit, maxLimit, 100)
        parsed_equation = f"0*x+" + self.equation
        try:
            y = eval(parsed_equation)
        except:
            self.plot_status = PlotStatus.no4.value

        fig = Figure(figsize=(8, 4))
        plot1 = fig.add_subplot(111)
        plot1.plot(x, y)

        return fig
