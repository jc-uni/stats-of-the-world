import matplotlib.pyplot as plt 
import numpy as np

class Plotting():

    def show_graph(self):
        plt.show()
    
    def plot_averages(self, avg_pop_city, avg_pop_country):
        np_avg = np.array([avg_pop_city, avg_pop_country])
        plt.bar(["Avg pop city","Avg pop country"],np_avg)


    def plot_medians(self, med_pop_city, med_pop_country):
        np_med = np.array([med_pop_city, med_pop_country])
        plt.bar(["Median pop city","Median pop country"],np_med)
