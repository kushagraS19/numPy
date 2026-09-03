import numpy as np
from stock_price_analyzer.data import price

lowest = np.min(price)
print("Lowest price :",lowest)