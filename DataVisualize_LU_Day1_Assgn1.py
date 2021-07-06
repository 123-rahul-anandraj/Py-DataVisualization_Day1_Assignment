#Assignment No:1
import numpy as np
import pandas as pd
import matplotlib as mplt
import matplotlib.pyplot as plt

x=np.arange(0,10)
y=x*x
plt.title('Simple Line Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.plot(x,y,linewidth=2,linestyle='dashed')
plt.show()
