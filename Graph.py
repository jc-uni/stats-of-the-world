import matplotlib.pyplot as plt 
import numpy as np


from Analysis import Statistics

class Plotting():

    def show_graph(self):
        plt.show()
    
    def plot_averages(self, avg_pop_city, avg_pop_country):
        np_avg = np.array([avg_pop_city, avg_pop_country])
        plt.bar(["AVG POP CITY","AVG POP COUNTRY"],np_avg)

    def plot_medians(self, med_pop_city, med_pop_country):
        np_avg = np.array([med_pop_city, med_pop_country])
        plt.bar(["MEDIAN POP CITY","MEDIAN POP COUNTRY"],np_avg)
