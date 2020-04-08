from nsepy import get_history
from datetime import date
from matplotlib import pyplot
import pandas as pd
data = get_history(symbol="ITC", start=date(2005, 1, 1), end=date(2020, 4, 8))
print(data.columns)
data[['Close']].plot()
pyplot.show()


