# Pie Charts
# Creating pie charts to visualize datasets 
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
series = pd.Series(3 * np.random.rand(4),
index = ['A','B','C','D'],
name = 'series')

print(series)
# visualization
plt.figure()
series.plot.pie(figsize=(6, 6))
plt.show()