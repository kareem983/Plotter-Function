import enum


class PlotStatus(enum.Enum):
    no0 = "Please Enter the Empty Cell."
    no1 = "Done"
    no2 = "Min/Max X Limit Must be Digit."
    no3 = "Min X Limit must be less than Max X Limit."
    no4 = "Mathematical Equation Must be in X and uses \n(+, -, *, /, ^) operation, e.g., 5*x^3 + 2*x" \
          ".\nPlease Check the Equation Input."
    no5 = "Mathematical Equation Must be in X.\nPlease Check the Equation Input."
