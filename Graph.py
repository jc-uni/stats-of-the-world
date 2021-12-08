import matplotlib.pyplot as plt 
import numpy as np

class Plotting():
    def __init__(self):
        np_avg = np.array([350468.2236, 31562208.8542])
        plt.bar(["AVG POP CITY","AVG POP COUNTRY"],np_avg)
        plt.show()
