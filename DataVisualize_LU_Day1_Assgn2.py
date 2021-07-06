#Assignment No:2
import numpy as np
import pandas as pd
import matplotlib as mplt
import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7] #Day of the week
y=[160,150,140,145,175,165,180] #sales
plt.title('Sales in a week')
plt.xlabel('Day No.')
plt.ylabel('Sales')
plt.grid()
plt.plot(x,y,color='green',marker='o')
plt.show()
