import numpy as np
from stock_price_analyzer.data import price

highest = np.max(price)
print("Highest price :",highest)