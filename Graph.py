import matplotlib.pyplot as plt 
import numpy as np

class Plotting():

    def show_graph(self):
        plt.show()
    
    def plot_averages(self, avg_pop_city, avg_pop_country):
        np_avg = np.array([avg_pop_city, avg_pop_country])
        plt.bar(["Avg pop city","Avg pop country"],np_avg, color = 'y')
        plt.text(0,np_avg[0],np_avg[0],ha='center',fontsize=8)
        plt.text(1,np_avg[1],np_avg[1],ha='center',fontsize=8)
        plt.xticks(fontsize=8)

    def plot_medians(self, med_pop_city, med_pop_country):
        np_med = np.array([med_pop_city, med_pop_country])
        plt.bar(["Median pop city","Median pop country"],np_med, color = 'g')
        plt.text(2,np_med[0],np_med[0],ha='center',fontsize=8)
        plt.text(3,np_med[1],np_med[1],ha='center',fontsize=8)
        plt.xticks(fontsize=8)